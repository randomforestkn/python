from PySimpleGUI import theme, Text, Button, Exit, Window
from time import time


def Timer():
    theme("DarkAmber")

    gui = [[Text(size=(24, 5), font=("Bahnschrift", 20), justification='center', key='text')],
           [Button('Pause', key='-RUN-PAUSE-'),
            Button('Reset'),
            Exit(button_color=('white', 'firebrick4'))]]

    window = Window('Χρονόμετρο', gui, no_titlebar=False, auto_size_buttons=True)

    i = 0
    paused = False
    start_time = int(round(time() * 100))

    while True:
        button, values = window.read(timeout=10)
        window['text'].update('{:02d}:{:02d}.{:02d}'.format((i//100)//60, (i//100) % 60, i % 100))

        if values is None or button == 'Exit':
            break

        if button == 'Reset':
            i = 0

        elif button == '-RUN-PAUSE-':
            paused = not paused
            window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')

        if not paused:
            i += 1
    window.close()


Timer()
