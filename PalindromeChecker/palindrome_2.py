import PySimpleGUI as sg

sg.theme('DarkBlue13')	

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Check'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

def check_palindrome(p):
    ret = ''
    if ((p == p[::-1]) == True):
        ret = p + ' is a palindrome.'
    else:
        ret = p + ' is not a palindrome.'
    return ret

# Event loop 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':	
        break
    if event == 'Check':
         is_palindrome = check_palindrome(values['-IN-']) 
         window['-OUTPUT-'].update(is_palindrome) 

window.close()