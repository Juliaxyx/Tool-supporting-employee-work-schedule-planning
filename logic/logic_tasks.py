import datetime
import PySimpleGUI as sg
import controllers.task_controller as controller


def is_name_valid(name):
    if len(name) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Nazwa zadania"'), title = "Błąd")
    return True

def date_exists(date):
    if len(date) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Data wykonania"'), title = "Błąd")
    return True

def if_done_exists(if_done):
    if len(if_done) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Czy zadanie jest wykonane?"'), title = "Błąd")
    return True

def is_date_valid(date):
    if calculate_days_left_for_task(date).days < 1:
        return sg.popup(('Błędny formularz: Wybrana data musi być późniejszą niż dzisiaj!'), title = "Błąd")
    return True


def get_tasks_records():
    tasks_records = controller.retrieve_info()
    return tasks_records

def get_table_data_with_additional_column():
    tasks:list[list] = get_tasks_records()
    for task in tasks:
        task.append(calculate_days_left_for_task(task[4]).days)
    return tasks

def calculate_days_left_for_task(end_date: str):
    return datetime.datetime.strptime(end_date, "%d/%m/%Y").date() - datetime.datetime.now().date()

def clean_input_fields(keys: list[str], window: sg.Window):
    for key in keys:
        if key == '-TABLE-':
            break
        window[key].update(value='')
    