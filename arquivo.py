# janela-no-python
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add um toque de cor
# todas as coisas dentro da sua janela.
layout = [  [sg.Text('algum texto na linha 1')],
            [sg.Text('digite algo na linha 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# criar janela
window = sg.Window('titulo da janela', layout)
# Event Loop para processar "eventos"e obter ps "valores" do input
while True:  # valor verdadeiro
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': #  se o usuario fechar a janela ou cancelar
        break
    print('You entered ', values[0])
