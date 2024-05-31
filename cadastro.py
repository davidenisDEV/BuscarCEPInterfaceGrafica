from PySimpleGUI import PySimpleGUI as sg
from pycep import PyCep

#Layout
sg.theme('DarkAmber')
layout = [
    [sg.Text('Digite seu CEP'), sg.Input(key='cep')],
    [sg.Checkbox('Salvar CEP?')],
    [sg.Button('Buscar')],
    [sg.Text('', key='resultado', size=(50,5))]
]

# Window
janela = sg.Window('Busca CEP', layout)

#Eventos
while True:
    eventos, valores = janela.read()

    #Break Loop
    if eventos == sg.WINDOW_CLOSED:
        break;
    
    #Evento inicia ao clicar no botao de Buscar
    if eventos == 'Buscar':
        cep_input = valores['cep']
        cep = PyCep(cep_input)
        retorno = cep.dadosCep

        if retorno:
            cepDaRua = retorno['cep']
            uf = retorno['uf']
            cidade = retorno['localidade']
            bairro = retorno['bairro']
            rua = retorno['logradouro']

            resultado_texto = (f'CEP: {cepDaRua}\n'
                               f'UF: {uf}\n'
                               f'Cidade: {cidade}\n'
                               f'Bairro: {bairro}\n'
                               f'O nome da rua: {rua}')
        else:
            resultado_texto = 'CEP não encontrado ou inválido.'

        #Retorna a nova janela apos clicar no botao de Buscar com os resultados da busca
        janela['resultado'].update(resultado_texto)

janela.close()