import PySimpleGUI as sg
from consts import keys, months, shift_names, employees, shorter_months 
import controllers.form_controller as controller
import logic.logic_form as logic   

def main_form():
    headings = list(keys.keys())

    layout = [
        [sg.Text('Miesiąc:', size=(6,1), justification='left'), sg.Combo(months,enable_events=True, key='-MONTH-', size=(15, 1), readonly = True, background_color= '#e3af6f'),sg.Text(' '*30), sg.Button('Pobierz dane', key='-INSERT-', disabled=True, tooltip='Tylko koordynator może pobierać dyspozycyjność pracownika w danym miesiącu')],
        [sg.Text('Dyspozycyjność pracownika:', size=(22,1), justification='left'), sg.Combo(employees, key='-EMPLOYEE-', size=(15, 1), readonly = True, background_color= '#e3af6f')],
        [sg.Text('------------------------------------------------------------------------------------------------------------------------------------------------------------', justification='center')],
        [sg.Text('Dzień miesiąca:', size=(18,1), justification='centre'), sg.Text("Wybierz dostępność:", size=(15,1), justification='left'), sg.Text('Dzień miesiąca:', size=(18,1), justification='centre'), sg.Text("Wybierz dostępność:", size=(15,1), justification='left')],
        [sg.Text(headings[0], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[1]), size=(10, 1), readonly = True),  sg.Text(headings[16], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[17]), size=(10, 1), readonly = True)],
        [sg.Text(headings[1], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[2]), size=(10, 1), readonly = True),  sg.Text(headings[17], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[18]), size=(10, 1), readonly = True)],
        [sg.Text(headings[2], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[3]), size=(10, 1), readonly = True), sg.Text(headings[18], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[19]), size=(10, 1), readonly = True)],
        [sg.Text(headings[3], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[4]), size=(10, 1), readonly = True), sg.Text(headings[19], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[20]), size=(10, 1), readonly = True)],
        [sg.Text(headings[4], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[5]), size=(10, 1), readonly = True), sg.Text(headings[20], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[21]), size=(10, 1), readonly = True)],
        [sg.Text(headings[5], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[6]), size=(10, 1), readonly = True), sg.Text(headings[21], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[22]), size=(10, 1), readonly = True)],
        [sg.Text(headings[6], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[7]), size=(10, 1), readonly = True), sg.Text(headings[22], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[23]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[7], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[8]), size=(10, 1), readonly = True), sg.Text(headings[23], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[24]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[8], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[9]), size=(10, 1), readonly = True), sg.Text(headings[24], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[25]), size=(10, 1), readonly = True)],
        [sg.Text(headings[9], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[10]), size=(10, 1), readonly = True),  sg.Text(headings[25], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[26]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[10], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[11]), size=(10, 1), readonly = True), sg.Text(headings[26], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[27]), size=(10, 1), readonly = True)],
        [sg.Text(headings[11], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[12]), size=(10, 1), readonly = True),  sg.Text(headings[27], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[28]), size=(10, 1), readonly = True)],
        [sg.Text(headings[12], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[13]), size=(10, 1), readonly = True), sg.Text(headings[28], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[29]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[13], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[14]), size=(10, 1), readonly = True), sg.Text(headings[29], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[30]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[14], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[15]), size=(10, 1), readonly = True), sg.Text(headings[30], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[31]), size=(10, 1), readonly = True)],        
        [sg.Text(headings[15], size=(22,1), justification='centre'), sg.Combo(shift_names, key=(keys[16]), size=(10, 1), readonly = True)],
        [sg.Text('-------------------------------------------------------------------------------------------------------------------------------------------------------------', justification='center')],
        [sg.Text("Preferowana minimalna liczba godzin:", size=(40,1), justification='center'), sg.Text("Preferowana maksymalna liczba godzin:", size=(40,1), justification='center')],
        [sg.Text(' ', size=(12,1)), sg.Input(key='-MIN_H-', size=(10,1), justification='center'),sg.Text(' ', size=(30,1)), sg.Input(key='-MAX_H-', size=(10,1), justification='center')],
        
        [sg.Button('Zapisz zmiany',disabled=False), sg.Button('Edytuj', key='-EDIT-', disabled=True, tooltip='Tylko koordynator może edytować dyspozycyjność pracownika w danym miesiącu'), sg.Button('Wyjście')]
    ]

    window_form = sg.Window('Dyspozycyjność',layout, finalize=True)
    is_coordinator = False
    set_default = 0
    while True:
    #Wstawianie 'brak' do kazdego z pol za pierwszym uruchomieniem, wyswietlenie okna do sprawdzenia permisji
        if set_default == 0:
            sg.theme('LightGrey1')
            logic.check_permissions([window_form['-EDIT-'], window_form['-INSERT-']])
            for key in keys.values():
                window_form[key].update(value='brak')
            set_default = 1
        event,values = window_form.read()
        
    #Zapisywanie wartości 
        if event == 'Zapisz zmiany':
            sg.theme('LightGrey1')
            valid_fields = logic.are_values_valid(values, months)
            if valid_fields:
                shifts = []
                for key in keys.values():
                    if len(values[key]) < 1:
                        break
                    shifts.append(shift_names.index(values[key]))
                choice, _ = sg.Window('Kontynuować?', [[sg.Text('Czy na pewno chcesz zapisać swoją dyspozycyjność na ten miesiąc?')], [sg.Yes(button_text = "Tak", s=10), sg.No(button_text = "Nie", s=10)]], disable_close=True).read(close=True)
                if choice == 'Tak':
                    controller.insert_info(values['-EMPLOYEE-'], months.index(values['-MONTH-']), shifts, values['-MIN_H-'], values['-MAX_H-']) 
                    sg.popup('Pomyślnie zapisano!')
            
    #Edytowanie istniejacej dyspozycyjnosci danych
        if event == '-EDIT-':
            sg.theme('LightGrey1')
            valid_fields = logic.are_values_valid(values, months, [0,0])
            if type(valid_fields) == list:
                shifts = []
                for key in keys.values():
                    if len(values[key]) < 1:
                        break
                    shifts.append(shift_names.index(values[key]))
                controller.update_info(values['-EMPLOYEE-'], months.index(values['-MONTH-']), shifts, values['-MIN_H-'], values['-MAX_H-'])
                sg.popup('Pomyślnie edytowano!')

    #Wyświetlenie danych z bazy dla danego pracownika i miesiaca
        if event == '-INSERT-':
            sg.theme('LightGrey1')
            valid_fields = logic.are_values_valid(values, months, [0])
            if type(valid_fields) == list:
                retrieved_data = controller.retrieve_info(values['-EMPLOYEE-'], months.index(values['-MONTH-']))
                if len(retrieved_data) < 1:
                    sg.popup('Ten pracownik jeszcze nie wystawił dyspozycyjności!')
                for index, row in enumerate(retrieved_data):
                    window_form[keys[index+1]].update(value=shift_names[row[2]])
                    window_form['-MIN_H-'].update(value=row[3])
                    window_form['-MAX_H-'].update(value=row[4])
                    
    #Zmiana miesiąca        
        if event == '-MONTH-':
            window_form[keys[31]].update(disabled=False)
            window_form[keys[30]].update(disabled=False)
            window_form[keys[31]].update(value='brak')
            window_form[keys[30]].update(value='brak')
            for index, month in enumerate(months):
                if values['-MONTH-'] == month and index in shorter_months:
                    window_form[keys[31]].update(disabled=True)
                    window_form[keys[31]].update(value='')
                    if index == 1:
                        window_form[keys[30]].update(disabled=True)
                        window_form[keys[30]].update(value='')
                        
    #Wyjście    
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            sg.theme('DarkBlue3')
            break
    window_form.close()
    try:
        main()
    except:
        from main import main
        