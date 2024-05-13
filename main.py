import PySimpleGUI as sg

# Define the theme
sg.theme('DarkGrey4')

# Define the layout
layout = [
    [sg.Input(size=(20, 1), font=('Helvetica', 20), justification='right', key='input')],
    [sg.Button('C', size=(5, 2)), sg.Button('CE', size=(5, 2)), sg.Button('<-', size=(5, 2)), sg.Button('/', size=(5, 2))],
    [sg.Button('7', size=(5, 2)), sg.Button('8', size=(5, 2)), sg.Button('9', size=(5, 2)), sg.Button('*', size=(5, 2))],
    [sg.Button('4', size=(5, 2)), sg.Button('5', size=(5, 2)), sg.Button('6', size=(5, 2)), sg.Button('-', size=(5, 2))],
    [sg.Button('1', size=(5, 2)), sg.Button('2', size=(5, 2)), sg.Button('3', size=(5, 2)), sg.Button('+', size=(5, 2))],
    [sg.Button('0', size=(5, 2)), sg.Button('.', size=(5, 2)), sg.Button('=', size=(5, 2))],
]

# Create the window
win = sg.Window('Calculator', layout)

# Event loop
while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'C':
        win['input'].update('')
    elif event == '=':
        try:
            result = eval(values['input'])
            win['input'].update(result)
        except Exception as e:
            win['input'].update('ERROR')
    elif event == 'CE':
        current_value = values['input']
        win['input'].update(current_value[:-1])
    else:
        current_value = values['input']
        win['input'].update(current_value + event)

# Close the window
win.close()
