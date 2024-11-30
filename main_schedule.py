import PySimpleGUI as sg
import controllers.schedule_controller as controller
import logic.logic_schedule as logic
from consts import keys, shift_names, months, employees

def main_schedule():

    shift_list = shift_names[1:3]
    
    def show_days(row):
        days = []
        for day in keys.keys():
            frame_layout = [
                [sg.Text('Dzień ' + str(day), size=(23,1), font=('',10,"bold"), justification='center', background_color= '#e3af6f',text_color='#000000')], 
                [sg.Text(shift_list[0].capitalize(), size=(10,1), justification='center'), sg.Push(), sg.Text(shift_list[1].capitalize(), size=(10,1), justification='center')],
                [
                    sg.Combo([], readonly=True, key=keys[day]+shift_list[0]+'-main', disabled=True, size=(10,1), enable_events=True), 
                    sg.Push(),
                    sg.Combo([], readonly=True, key=keys[day]+shift_list[1]+'-main', disabled=True, size=(10,1), enable_events=True)
                 ],
                [
                    sg.Combo([], readonly=True, key=keys[day]+shift_list[0]+'-support', disabled=True, size=(10,1), enable_events=True), 
                    sg.Push(), 
                    sg.Combo([], readonly=True, key=keys[day]+shift_list[1]+'-support', disabled=True, size=(10,1), enable_events=True)
                 ]
            ]
            days.append(sg.Frame('',layout=frame_layout, key=keys[day], pad=(0,0)))
        if row == 1:
            return days[0:7]
        if row == 2:
            return days[7:14]
        if row == 3:
            return days[14:21]
        if row == 4:
            return days[21:28]
        if row == 5:
            for employee in employees:
                days.append(sg.Frame('', layout=[
                    [sg.Text(employee.capitalize(), size=(14,1), justification='center')],
                    [sg.Text('Min: '), sg.Text('', key=employee+'-MIN_H')],
                    [sg.Text('Max: '), sg.Text('', key=employee+'-MAX_H')],
                    [sg.Text('Aktualne: '), sg.Text('', key=employee+'-CURRENT_H')],
                    ], key=employee, pad=(0,12)))
            return days[28:]
    layout = [
        [show_days(1)],
        [show_days(2)],
        [show_days(3)],
        [show_days(4)],
        [show_days(5)],
        [sg.Push(), sg.Text('Wybierz miesiąc:'), sg.Combo(months, key='-MONTH-', readonly=True, enable_events=True)],
        [sg.Button('Zapisz zmiany', disabled=True), sg.Button('Edytuj zmiany', disabled=True), sg.Button('Wyjście')]
    ]
    employee_hours = {}
    employees_chosen = {}
    employees_all_shifts = {}
    window_form = sg.Window('Grafik', layout, finalize=True)
    current_schedule_data = []
    form_data = []
    set_default = False
    is_coordinator = False
    
    while True:
        if set_default == False:
            sg.theme('LightGrey1')
            if logic.check_permissions([window_form['Zapisz zmiany'], window_form['Edytuj zmiany']]):
                is_coordinator = True
                for key in keys.values():
                    window_form[key+shift_list[0]+'-main'].update(disabled=False)
                    window_form[key+shift_list[1]+'-main'].update(disabled=False)
            set_default = True
        event,values= window_form.read()
        if event == '-MONTH-':
            current_schedule_data = controller.retrieve_info_schedule(months.index(values['-MONTH-']))
            form_data = controller.retrieve_info_form(months.index(values['-MONTH-']))
            employee_hours = {employee: 0 for employee in employees}
            employees_chosen = {}
            employees_all_shifts = {key+shift+string: [] for string in ['-main', '-support'] for shift in shift_list for key in keys.values()} 
            if is_coordinator:
                window_form['Zapisz zmiany'].update(disabled=False)         
                window_form['Edytuj zmiany'].update(disabled=False)         
            for key in keys.values():
                window_form[key+shift_list[0]+'-main'].update(value=[], values=[], size=(10,1))
                window_form[key+shift_list[0]+'-support'].update(value=[], values=[], disabled=True, size=(10,1))
                window_form[key+shift_list[1]+'-main'].update(value=[], values=[], size=(10,1))
                window_form[key+shift_list[1]+'-support'].update(value=[], values=[], disabled=True, size=(10,1))
            for employee in employees:
                window_form[employee+'-MIN_H'].update(value='0')
                window_form[employee+'-MAX_H'].update(value='0')
                window_form[employee+'-CURRENT_H'].update(value='0')
                if len(form_data) < 1:
                    continue
                employee_data = form_data.get(employee)
                if employee_data != None:
                    window_form[employee+'-MIN_H'].update(value=employee_data['min'])
                    window_form[employee+'-MAX_H'].update(value=employee_data['max'])
                    for day, shift in employee_data['days'].items():
                        main_morning = list(window_form[keys[int(day)]+shift_list[0]+'-main'].widget['values'])
                        support_morning = list(window_form[keys[int(day)]+shift_list[0]+'-support'].widget['values'])
                        main_evening = list(window_form[keys[int(day)]+shift_list[1]+'-main'].widget['values'])
                        support_evening = list(window_form[keys[int(day)]+shift_list[1]+'-support'].widget['values'])
                        if shift == 1:
                            main_morning.append(employee)
                            support_morning.append(employee)
                            window_form[keys[int(day)]+shift_list[0]+'-main'].update(values = main_morning, size=(10,len(main_morning)))
                            window_form[keys[int(day)]+shift_list[0]+'-support'].update(values = support_morning, size=(10,len(support_morning)))
                            employees_all_shifts[keys[int(day)]+shift_list[0]+'-main'].append(employee)
                            employees_all_shifts[keys[int(day)]+shift_list[0]+'-support'].append(employee)
                        elif shift == 2:
                            main_evening.append(employee)
                            support_evening.append(employee)
                            window_form[keys[int(day)]+shift_list[1]+'-main'].update(values = main_evening, size=(10,len(main_evening)))
                            window_form[keys[int(day)]+shift_list[1]+'-support'].update(values = support_evening, size=(10,len(support_evening)))
                            employees_all_shifts[keys[int(day)]+shift_list[1]+'-main'].append(employee)
                            employees_all_shifts[keys[int(day)]+shift_list[1]+'-support'].append(employee)
                        elif  shift == 3:
                            main_morning.append(employee)
                            support_morning.append(employee)
                            main_evening.append(employee)
                            support_evening.append(employee)
                            window_form[keys[int(day)]+shift_list[0]+'-main'].update(values = main_morning, size=(10,len(main_morning)))
                            window_form[keys[int(day)]+shift_list[0]+'-support'].update(values = support_morning, size=(10,len(support_morning)))
                            window_form[keys[int(day)]+shift_list[1]+'-main'].update(values = main_evening, size=(10,len(main_evening)))
                            window_form[keys[int(day)]+shift_list[1]+'-support'].update(values = support_evening, size=(10,len(support_evening)))
                            employees_all_shifts[keys[int(day)]+shift_list[0]+'-main'].append(employee)
                            employees_all_shifts[keys[int(day)]+shift_list[0]+'-support'].append(employee)
                            employees_all_shifts[keys[int(day)]+shift_list[1]+'-main'].append(employee)
                            employees_all_shifts[keys[int(day)]+shift_list[1]+'-support'].append(employee)
                        else:
                            continue
                print(employees_all_shifts)
            if len(form_data) < 1:
                sg.theme('LightGrey1')
                sg.popup('Brak wystawionej dyspozycyjności w tym miesiącu!')
                continue
            if len(current_schedule_data) > 0:    
                print(current_schedule_data)
                for shift_row in current_schedule_data:
                    if shift_row[0] != '':
                        employee_hours[shift_row[0]] += 5
                        employees_chosen[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-main'] = shift_row[0]
                        window_form[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-main'].update(value=shift_row[0], size=(10,1))
                        window_form[shift_row[0]+'-CURRENT_H'].update(value=employee_hours[shift_row[0]])  
                        combo_new_values = employees_all_shifts[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-support'].copy()
                        if shift_row[1] != '':
                            employee_hours[shift_row[1]] += 5
                            employees_chosen[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-support'] = shift_row[1]
                            window_form[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-support'].update(value=shift_row[1], size=(10,len(combo_new_values)))                              
                            window_form[shift_row[1]+'-CURRENT_H'].update(value=employee_hours[shift_row[1]])
                        try:
                            combo_new_values.remove(shift_row[0])
                        except:
                            print(combo_new_values)
                        window_form[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-support'].update(values=combo_new_values, size=(10,len(combo_new_values)))
                        if is_coordinator:
                            window_form[keys[int(shift_row[2][0:shift_row[2].find('/')])]+shift_list[shift_row[3]-1]+'-support'].update(disabled=False)
        if event.find('-main') != -1 or event.find('-support') != -1:
            if event.find('main') != -1:
                combo_new_values = employees_all_shifts[event[0:event.find('main')]+'support'].copy()
                try:
                    combo_new_values.remove(values[event])
                    employees_chosen[event[0:event.find('main')]+'support'] = values[event[0:event.find('main')]+'support']
                except:
                    print(combo_new_values)
                window_form[event[0:event.find('main')]+'support'].update(values=combo_new_values, disabled=False, size=(10,len(combo_new_values)))
 # tu coś się psuje
                try:   
                    if values[event] == employees_chosen[event[0:event.find('main')]+'support']:
                        employee_hours[str(values[event])] -= 5
                        window_form[values[event]+'-CURRENT_H'].update(value=employee_hours[values[event]])   
                except:
                    print()
          
            try:
                employee_hours[str(values[event])] += 5
                window_form[values[event]+'-CURRENT_H'].update(value=employee_hours[values[event]])   
                if event.find('support') != -1 and employees_chosen[event] == employees_chosen[event[0:event.find('support')]+'main'] and employees_chosen[event] != values[event]:
                    employee_hours[str(employees_chosen[event])] += 5
                    window_form[employees_chosen[event]+'-CURRENT_H'].update(value=employee_hours[employees_chosen[event]])   
                if employees_chosen[event] in employees:
                    employee_hours[employees_chosen[event]] -= 5
                    window_form[employees_chosen[event]+'-CURRENT_H'].update(value=employee_hours[employees_chosen[event]])   
            except:
                print()           
            employees_chosen[event] = values[event] 
            if event.find('main') != -1:
                employees_chosen[event[0:event.find('main')]+'support'] = values[event[0:event.find('main')]+'support'] 
            if event.find('support') != -1:
                employees_chosen[event[0:event.find('support')]+'main'] = values[event[0:event.find('support')]+'main'] 
        if event == 'Zapisz zmiany':
            if len(current_schedule_data) > 0:
                sg.theme('LightGrey1')
                sg.popup('Grafik na ten miesiąc już był ustalany!')
                continue
            days = []
            for key in keys.values():
                days.append([values[key+shift_list[0]+'-main'], values[key+shift_list[0]+'-support'],
                    values[key+shift_list[1]+'-main'], values[key+shift_list[1]+'-support']])
            controller.insert_info(days, months.index(values['-MONTH-']))
        if event == 'Edytuj zmiany':
            days = []
            for key in keys.values():
                days.append([values[key+shift_list[0]+'-main'], values[key+shift_list[0]+'-support'],
                    values[key+shift_list[1]+'-main'], values[key+shift_list[1]+'-support']])
            controller.update_info(days, months.index(values['-MONTH-']))
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            sg.theme('DarkBlue3')
            break
    window_form.close()
    try:
        main()
    except:
        from main import main
