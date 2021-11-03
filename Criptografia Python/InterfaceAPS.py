import PySimpleGUI as sg # A INTERFACE USADA 
import random # A BIBLIOTECA USADA PARA GERAR O 'EMBARALHAMENTO' DE CARACTERES PARA CRIPTOGRAFIA

class PassGen:       

    def __init__(self):  #AQUI UMA CLASSE E UMA FUNÇÃO QUE DEFINE O INICIO DO CODIGO

        #Layout              
        sg.theme('Dark')
        layout = [ #AQUI DEFINE AS LINHAS DA INTERFACE. LABELS BOTÕES, ETC
            [sg.Text('Usuario'),sg.Input(key='usuario')],   
            [sg.Text('Senha  '),sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar')],
            [sg.Text('', key='d',size=(50,2))],
        ]

        sg.theme('Dark')
        layout2 = [ #AQUI DEFINE AS LINHAS DA INTERFACE. LABELS BOTÕES, ETC
            [sg.Text('Digite a Mensagem:')],
            [sg.InputText('',key='cript')],
            [sg.Button('Criptografar')],
            [sg.Text('Mensagem Criptografada: ')],
            [sg.InputText(key = 'out1',size=(45,1000))],
            [sg.Text('Cole ou digite a Mensagem Criptografada: ')],
            [sg.InputText('',key='decript')],
            [sg.Button('Descriptografar')],
            [sg.Text('Mensagem Descriptografada: ')],
            [sg.Multiline(key='f',size=(50,5))],
            [sg.Text('', key='txt')],
            [sg.Button('Voltar')],
        ]
        #Janela
        self.janela = sg.Window('Login', layout) 
        self.janela2 = sg.Window('Criptografador', layout2)   
        
    def Iniciar(self): 
                       
        while True:
            eventos, valores = self.janela.read()               
            if eventos == sg.WINDOW_CLOSED:
                break
                           
            elif eventos == 'Entrar': 
                cript = ('')
                if valores ['usuario'] == 'admin' and valores ['senha'] == '1234':
                    break
                else:
                    neg = 'Acesso Negado!'
                    self.janela['d'].update(neg)  
                  
        while True:
            if eventos == self.janela.close():
                break
            else:
                eventos, valores = self.janela2.read()
                if eventos == sg.WINDOW_CLOSED:
                    break

                if eventos == 'Criptografar':
                    cript = ('')
                   
                    if valores ['cript'] != cript:
                        new = self.gerar_criptografia()
                        print(new)
                        self.janela2['out1'].update(new)

                if eventos == 'Descriptografar':
                    valor = valores ['cript'] 
                    cripto = valores ['out1']
                    decript = valores ['decript']

                    if decript == cripto:
                        self.janela2['f'].update(valor)
  
                if eventos == 'Voltar':
                 self.janela2.close()   


            
    def gerar_criptografia(self): # AQUI DEFINE A CRIPTOGRAFIA
        cripto = "ABCDEFGHYJKLMNOPQRSTUVWXYZabcdef-=+-*/ghijklmnop$%&qrstuvwxyz1234567890!@*"
        char = random.choices(cripto, k=50)
        join = ''.join(char)
        print(join)
        return join

        

gen = PassGen()
gen.Iniciar()
#FIM
