import PySimpleGUI as sg
from main_schedule import main_schedule
from main_tasks import main_tasks
from main_form import main_form

def main():
    window = sg.Window('Menu', [[sg.Text('Wybierz aplikację do otworzenia')],[sg.Button('Lista To-Do'), sg.Button('Dyspozycyjność'), sg.Button('Grafik'), sg.Button('Wyjście', key='EXIT')]], finalize=True)

    while True:
        event,_ = window.read()
        if event == 'Lista To-Do':
            window.close()
            main_tasks()
            break
        if event == 'Dyspozycyjność':
            window.close()
            main_form()
            break
        if event == 'Grafik':
            window.close()
            main_schedule()
            break
        if event in (sg.WIN_CLOSED, 'EXIT'):
            exit()
    main()
main()
