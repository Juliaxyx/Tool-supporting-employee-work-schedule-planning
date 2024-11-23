import datetime
import PySimpleGUI as sg
import controllers.task_controller as controller


def is_name_valid(name):
    """Checks if input for name has anythin inside

    Args:
        name (string): Name of the task

    Returns:
        boolean: Valid or not
    """
    if len(name) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Nazwa zadania"'), title = "Błąd")
    return True

def date_exists(date):
    """Checks if input for date has anythin inside

    Args:
        date (string): Date of the task

    Returns:
        boolean: Valid or not
    """
    if len(date) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Data wykonania"'), title = "Błąd")
    return True

def if_done_exists(if_done):
    """Checks if input for date has anythin inside

    Args:
        date (string): Date of the task

    Returns:
        boolean: Valid or not
    """
    if len(if_done) < 1:
        return sg.popup(('Błędny formularz: Brak pola "Czy zadanie jest wykonane?"'), title = "Błąd")
    return True

def is_date_valid(date):
    """Checks if selected date is later than today's date

    Args:
        date (str): Date as string 

    Returns:
        True | Popup: Either True or popup with error's info
    """
    if calculate_days_left_for_task(date).days < 1:
        return sg.popup(('Błędny formularz: Wybrana data musi być późniejszą niż dzisiaj!'), title = "Błąd")
    return True


def get_tasks_records():
    """Retrieving function for tasks from database

    Returns:
        tasks_records (list[list]): Returns list of tasks with all their columns from database    
    """
    tasks_records = controller.retrieve_info()
    return tasks_records

def get_table_data_with_additional_column():
    """Merges tasks from database with calculated amount of days for table data
    
    Returns:
        list: List of tasks with added column
    """
    tasks:list[list] = get_tasks_records()
    for task in tasks:
        task.append(calculate_days_left_for_task(task[4]).days)
    return tasks

def calculate_days_left_for_task(end_date: str):
    """Calculates amount of days left before task will be late

    Args:
        end_date (date): Date to which task should have been finished in DD/MM/YYYY formats
    Returns:
        date: Amount of days left
    """
    return datetime.datetime.strptime(end_date, "%d/%m/%Y").date() - datetime.datetime.now().date()

def clean_input_fields(keys: list[str], window: sg.Window):
    """Cleans input fields from app

    Args:
        keys (list[str]): List of input fields' keys
        window (Window): Window on which the operation should be executed
    """
    for key in keys:
        if key == '-TABLE-':
            break
        window[key].update(value='')
    