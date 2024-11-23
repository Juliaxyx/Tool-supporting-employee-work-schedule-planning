import PySimpleGUI as sg
import controllers.schedule_controller as controller
from consts import keys, shift_names, months, employees

#tasks_for_table_array = logic.get_table_data_with_additional_column()
def main_schedule():

    shift_list = shift_names[1:3]
    
    def show_days(row):
        days = []
        for day in keys.keys():
            frame_layout = [
                [sg.Text('Dzień ' + str(day), size=(20,1), justification='center')], 
                [sg.Text(shift_list[0], size=(10,1), justification='left'), sg.Push(), sg.Combo([], key=keys[day]+shift_list[0]+'main', size=(5,1))],
                [sg.Push(), sg.Combo([], key=keys[day]+shift_list[0]+'support', size=(5,1))], 
                [sg.Text(shift_list[1], size=(10,1), justification='left'), sg.Push(), sg.Combo([], key=keys[day]+shift_list[1]+'main', size=(5,1))]
            ]
            days.append(sg.Frame('',layout=frame_layout, key=keys[day]))
        if row == 1:
            return days[0:7]
        if row == 2:
            return days[7:14]
        if row == 3:
            return days[14:21]
        if row == 4:
            return days[21:28]
        if row == 5:
            return days[28:31]
    layout = [
        [show_days(1)],
        [show_days(2)],
        [show_days(3)],
        [show_days(4)],
        [show_days(5)],
        [sg.Push(), sg.Combo(months, key='-MONTH-')],
        [sg.Button('Zapisz zmiany',disabled=True), sg.Button('Wyjście')]
    ]

    window_form = sg.Window('Grafik',layout)

    while True:
        event,values= window_form.read()
        form_data = controller.retrieve_info_form(values['-MONTH-'])
    #Wyjście    
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
    window_form.close()
    try:
        main()
    except:
        from main import main
# main_schedule()