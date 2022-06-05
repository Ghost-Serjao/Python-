import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key='aceitacartao'),sg.Radio('Não','cartões',key='naoaceitacartao')],
            [sg.Slider(range=(0, 100),default_value=0,orientation='h',size=(15,20),key='slidervelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)
       
    def iniciar(self):
        while True:
            #Extrair dados da tela
            self.button, self.values = self.janela.read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitacartao']
            nao_aceita_cartao = self.values['naoaceitacartao']
            velocidade_script = self.value['slidervelocidade']

            print(f'Nome:{nome}')
            print(f'Idade:{idade}')
            print(f'aceita gmail: {aceita_gmail}') 
            print(f'aceita outlook: {aceita_outlook}') 
            print(f'aceita yahoo: {aceita_yahoo}') 
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartâo: {nao_aceita_cartao}')
            print(f'Velocidade script: {velocidade_script}')
        
tela = TelaPython()
tela.iniciar()

