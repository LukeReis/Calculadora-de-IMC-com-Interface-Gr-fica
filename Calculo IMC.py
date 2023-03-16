import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Informe sua altura (m):'), sg.Input('', key='altura', size=(15, 1))],
    [sg.Text('Informe seu peso (KG):'), sg.Input('', key='peso', size=(15, 1))],
    [sg.Button('Calcula IMC'), sg.Button('Cancelar')],
    [sg.Text('', key='imc')],
]

janela = sg.Window("Calculadora IMC", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Calcula IMC':
        altura_imc = float(valores['altura'])
        peso_imc = float(valores['peso'])
        imc = peso_imc / (altura_imc ** 2)

        if imc <= 18.5:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Abaixo do peso normal.")

        elif imc > 18.5 and imc <= 24.9:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Peso normal.")

        elif imc >= 25 and imc <= 29.9:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Excesso de peso.")

        elif imc >= 30 and imc <= 34.9:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Obesidade Grau I.")

        elif imc >= 35 and imc <= 39.9:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Obesidade Grau II.")

        elif imc >= 40:
            janela['imc'].Update(f"O seu IMC e igual a {imc:.2f} "
                                 f" Obesidade Grau III.")




janela.close()
