import PySimpleGUI as sg
import controllers.form_controller as controller

#FORM
def are_values_valid(values, months, valid_list=[0,0,0]):
    """Checks if input for name has anythin inside

    Args:
        name (string): Name of the task

    Returns:
        boolean: Valid or not
    """
    data = controller.retrieve_info(values['-EMPLOYEE-'], months.index(values['-MONTH-']))
    if len(values['-MONTH-']) < 1:
        sg.popup('Wybierz miesiąc, na który wystawiana jest dyspozycyjność!', title = "Błąd", button_justification='center')
        return False
    elif len(values['-EMPLOYEE-']) < 1:
        sg.popup('Wybierz pracownika, któremu wystawiana jest dyspozycyjność!', title = "Błąd", button_justification='center')
        return False
    elif len(valid_list) > 1 and (len(values['-MAX_H-']) < 1 or len(values['-MIN_H-']) < 1):
        sg.popup('Pole puste! Proszę wypełnić oba pola!', title = "Błąd", button_justification='center')
        return False
    elif len(valid_list) > 1 and (not str(values['-MAX_H-']).isnumeric() or not str(values['-MIN_H-']).isnumeric()):
        sg.popup('Pole zawiera niedozwolone znaki! Proszę wpisać tylko cyfry!', title = "Błąd", button_justification='center')
        return False
    elif len(valid_list) > 2 and len(data) > 0:
        sg.popup('Już zapisano dyspozycyjność w tym miesiącu, {}!'.format(values['-EMPLOYEE-']), title = "Błąd", button_justification='center')
        return False
    elif len(valid_list) == 2 and len(data) < 1:
        sg.popup('Jeszcze nie zapisano dyspozycyjności w tym miesiącu!', title = "Błąd", button_justification='center')
        return False
    else:
        if len(valid_list) > 2: return True 
        return data

#FORM PERMISSION
def check_permissions(window_elements):
    pass_popup = sg.Window('Podaj haslo koordynatora: ', [[sg.Input(key='-PASSWORD-')],[sg.Yes(button_text='Dalej')]], disable_close=True)
    _, pass_val = pass_popup.read(close=True)
    if pass_val['-PASSWORD-'] == '123':
        window_elements[0].update(disabled=False)
        window_elements[1].update(disabled=False)
        sg.popup('Otworzono jako koordynator grafiku')
        return True
    sg.popup('Otworzono jako pracownik')
    return False
#RESOURCES

#SCHEDULE
