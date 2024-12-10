import os
from pathlib import Path
import PySimpleGUI as sg
from main_schedule import main_schedule
from main_tasks import main_tasks
from main_form import main_form
import migrations.create_tables


path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, '.\\databases\\resources.db')

if not os.path.exists(db):
    Path(os.path.join(path, '.\\databases')).mkdir(parents=True, exist_ok=True)
    migrations.create_tables.resources(db)
    migrations.create_tables.schedule(db)
    migrations.create_tables.tasks(db)

def main():
    window = sg.Window('Menu', [[sg.Text('Wybierz aplikację do otworzenia')],[sg.Button('Lista zadań'), sg.Button('Formularz dyspozycyjności'), sg.Button('Harmonogram pracy'), sg.Button('Wyjście', key='EXIT')]], finalize=True)

    while True:
        event,_ = window.read()
        if event == 'Lista zadań':
            window.close()
            main_tasks()
            break
        if event == 'Formularz dyspozycyjności':
            window.close()
            main_form()
            break
        if event == 'Harmonogram pracy':
            window.close()
            main_schedule()
            break
        if event in (sg.WIN_CLOSED, 'EXIT'):
            exit()
    main()
main()
