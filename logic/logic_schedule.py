import PySimpleGUI as sg


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