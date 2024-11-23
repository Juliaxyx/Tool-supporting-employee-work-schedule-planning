import PySimpleGUI as sg
import controllers.task_controller as controller
import logic.logic_tasks as logic    
def main_tasks():
    tasks_for_table_array = logic.get_table_data_with_additional_column()

    keys = ['-NAME-', '-DESCRIPTION-', '-EMPLOYEE-', '-PRIORITY-', '-DATE_DONE-', '-IF_DONE-', '-TABLE-']
    headings = ['Nazwa zadania', 'Opis zadania', 'Przypisany pracownik', 'Poziom piorytetu', 'Data wykonania', 'Czy zrobione?', 'Dni pozostałe']

    layout = [
        [sg.Text("Wpisz nazwę zadania:", size=(22,1)), sg.Input(key='-NAME-', size=(30, 1), disabled_readonly_background_color='grey')],
        [sg.Text("Wpisz opis zadania:", size=(22,1)), sg.Input(key='-DESCRIPTION-', size=(40, 1))],
        [sg.Text("Wybierz pracownika:", size=(22,1)), sg.Combo(['Julia', 'Anna', 'Alicja', 'Magda', 'Marta', 'Monika'], key='-EMPLOYEE-', size=(10, 1), readonly = True)],
        [sg.Text("Wybierz piorytet:", size=(22,1)), sg.Combo(['niski', 'średni', 'wysoki'], key='-PRIORITY-', size=(10, 1), readonly = True)],
        [
            sg.Text("Wybierz datę wykonania:", size=(22,1)), 
            sg.Input(key='-DATE_DONE-', size=(10, 1), readonly=True),
            sg.Button('Wybierz', key='DatePicker')
        ],
        [sg.Text("Czy zadanie jest wykonane?", size=(22,1)), sg.Combo(['TAK','NIE'], key='-IF_DONE-', size=(10, 1), readonly = True)],
        [sg.Button('Dodaj zadanie'), sg.Button('Edytuj zadanie'),sg.Button('Zapisz zmiany',disabled=True), sg.Button('Usuń zadanie'), sg.Button('Wyjście')],
        [sg.Table(
            values = tasks_for_table_array,
            headings = headings, 
            max_col_width = 35,
            auto_size_columns = True,
            display_row_numbers = True,
            starting_row_number = 1,
            justification = 'center',
            num_rows = 10,
            key = '-TABLE-',
            row_height = 35,
            tooltip = 'Tasks Table'
        )]
    ]

    window = sg.Window('Lista zadań',layout, finalize=True)

    global last_selected_row
    last_selected_row = []
    global last_selected_row_id
    last_selected_row_id = -1
    check_if_done_run = 1

    #Oznaczanie zrobionych zadań
    def check_if_done():
        if check_if_done_run == 1:
            new_row_colors = [(i, "green") for i, row in enumerate(tasks_for_table_array) if "TAK" in row[5]]
            window['-TABLE-'].update(row_colors = new_row_colors)
        
    while True:
        check_if_done()
        event,values= window.read()
        window['-TABLE-'].update(values=tasks_for_table_array)
    #Kalendarz
        if event == 'DatePicker':
            while True:
                sg.theme('LightGrey1')
                chosen_date = sg.popup_get_date()
                print(chosen_date)
                if chosen_date == None:
                    break
                else:
                    date_string = str(chosen_date[1]) + '/' + str(chosen_date[0]) + '/' + str(chosen_date[2])
                    date_valid = logic.is_date_valid(date_string)
                    if type(date_valid) == bool:
                        window['-DATE_DONE-'].update(value=date_string)
                        sg.theme('DarkBlue3')
                        break
    #Dodaj zadanie
        elif event == 'Dodaj zadanie':
            sg.theme('LightGrey1')
            name_valid = logic.is_name_valid(values['-NAME-'])
            date_valid = logic.date_exists(values['-DATE_DONE-'])
            if_done_valid = logic.if_done_exists(values['-IF_DONE-'])
            if type(name_valid) == bool and type(date_valid) == bool and type(if_done_valid) == bool:
                controller.insert_info(values['-NAME-'], values['-DESCRIPTION-'], values['-EMPLOYEE-'], values['-PRIORITY-'], values['-DATE_DONE-'], values['-IF_DONE-'])
                tasks_for_table_array.append([values['-NAME-'], values['-DESCRIPTION-'], values['-EMPLOYEE-'], values['-PRIORITY-'], values['-DATE_DONE-'], values['-IF_DONE-'], logic.calculate_days_left_for_task(values['-DATE_DONE-']).days])
                window['-TABLE-'].update(values = tasks_for_table_array) 
                sg.popup(("Informacje zapisane!"), title = "Informacja")
                logic.clean_input_fields(keys, window)
    #Edycja zadania
        if event == 'Edytuj zadanie' or event == 'Zapisz zmiany':
            sg.theme('LightGrey1')
            if len(values['-TABLE-']) < 1 and len(last_selected_row) < 1:
                sg.popup(('Nie wybrano zadania'), title = "Informacja")
            elif event == 'Edytuj zadanie':
                sg.popup(('Edytuj wybrane zadanie'), title = "Informacja")
                selected_row = tasks_for_table_array[values['-TABLE-'][0]]
                last_selected_row = selected_row
                last_selected_row_id = values['-TABLE-'][0]
                logic.clean_input_fields(keys, window)
                window['-NAME-'].update(readonly=True)
                window['-DESCRIPTION-'].update(value=selected_row[1])
                window['-EMPLOYEE-'].update(value=selected_row[2])
                window['-PRIORITY-'].update(disabled=True, background_color='grey')
                window['-DATE_DONE-'].update(disabled=True)
                window['DatePicker'].update(disabled=True)
                window['-DATE_DONE-'].widget['disabledbackground'] = 'grey'
                window['-DATE_DONE-'].widget['readonlybackground'] = 'grey'
                window['-IF_DONE-'].update(value=selected_row[5])
                
                window['Zapisz zmiany'].update(disabled=False)
            elif event == 'Zapisz zmiany':
                selected_row = last_selected_row
                controller.update_info(selected_row[1], selected_row[2], selected_row[5], selected_row[0], selected_row[4])
                tasks_for_table_array[last_selected_row_id] = [selected_row[0], values['-DESCRIPTION-'], values['-EMPLOYEE-'], selected_row[3], selected_row[4], values['-IF_DONE-'], selected_row[6]]
                window['-TABLE-'].update(values = tasks_for_table_array)
                sg.popup(("Zedytowano!"), title = "Informacja")
                window['Zapisz zmiany'].update(disabled=True)
                
                window['-NAME-'].update(readonly=False)
                window['-PRIORITY-'].update(disabled=False, background_color='white')
                window['-DATE_DONE-'].update(disabled=False)
                window['DatePicker'].update(disabled=False)
                window['-DATE_DONE-'].update(readonly=True)
                window['-DATE_DONE-'].widget['disabledbackground'] = 'white'
                window['-DATE_DONE-'].widget['readonlybackground'] = 'white'
                
                logic.clean_input_fields(keys, window)
    #Usuwanie zadania
        if event == 'Usuń zadanie':
            if values['-TABLE-']==[]:
                sg.popup(('Nie wybrano zadania'), title = "Informacja")
            else:   
                sg.theme('LightGrey1')
                choice, _ = sg.Window('Kontynuować?', [[sg.Text('Czy na pewno chcesz usunąć to zadanie?')], [sg.Yes(button_text = "Tak", s=10), sg.No(button_text = "Nie", s=10)]], disable_close=True).read(close=True)
                if choice == 'Tak':
                    selected_row = tasks_for_table_array[values['-TABLE-'][0]] 
                    controller.delete_info(selected_row[0], selected_row[4])
                    tasks_for_table_array.pop(values['-TABLE-'][0])
                    window['-TABLE-'].update(values = tasks_for_table_array)
                    sg.popup(('Usunięto!'), title = "Informacja")
                elif choice == 'Nie':
                    window['-TABLE-']
    #Wyjście    
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
    window.close()
    try:
        main()
    except:
        from main import main
# main_tasks()
        