import PySimpleGUI as sg
import pyttsx3


engine = pyttsx3.init()


layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Input(key='-TEXT-')],
    [sg.Button('Speak'), sg.Button('Exit')],
    [sg.Text('', key='-STATUS-')],
]


window = sg.Window('Text-to-Speech App', layout)


while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):  
        break
    if event == 'Speak':
        text = values['-TEXT-']
        if text != '':
            
            engine.setProperty('rate', 150)  
            engine.setProperty('volume', 1.0)  
            engine.say(text)
            engine.runAndWait()
            window['-STATUS-'].update('Text spoken!')
        else:
            window['-STATUS-'].update('Please enter some text.')


window.close()