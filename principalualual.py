import tkinter as tk

from tela import Tela
from agendamento import Agendamento

class Principal(Tela):
    def __init__(self, nome, nomeUsuario):
        super().__init__(nome)
        self.nomeUsuario = nomeUsuario
        self.lPrecos = None
        self.tipo = None
       
    def criarHome(self):

        def porteBicho(tipo):

            if tipo == 'Grande':
                precos = ['85,00', '65,00', '60,00' ]
            elif tipo == 'Médio':
                precos = ['75,00', '55,00', '50,00']
            elif tipo == 'Pequeno':
                precos = ['65,00', '45,00', '40,00']
            
            self.lPrecos.config(text=f'Banho e Tosa: R${precos[0]}, Banho: R${precos[1]}, Tosa: R${precos[2]}')
            
            self.tipo = tipo
        
        def confirmaPet():
             #nova janela
                agendar = Agendamento('Pré-Agendamento', self.tipo, self.nomeUsuario)
                agendar.criarAgendamento()



            

        self.criarJanela()

        #itulo da Home 
        texto = tk.Label(self.janela ,text=f'Bem vindo {self.nomeUsuario}', font=('arial 12'))
        texto.pack(pady=10)

        #titulo agendamento
        lAgendamento = tk.Label(self.janela ,text=f' Pré-Agendamento', font=('arial 15'))
        lAgendamento.pack(pady=10)

        lInfo = tk.Label(self.janela ,text=f'Selecione o porte do animal Cachorro/Gato', font=('arial 10'))
        lInfo.pack(pady=10)
         
        porte = ['Grande', 'Médio', 'Pequeno']
        
        controle = 0
        for i in porte:

            b = tk.Button(self.janela ,text=f'{i}', command=lambda t=i: porteBicho(t),  font=('arial 10'))
            b.pack(pady=10)
            controle = controle + 1

        #titulo agendamento
        self.lPrecos = tk.Label(self.janela ,text=f'', font=('arial 10'))
        self.lPrecos.pack(pady=5)

        bConfirma = tk.Button(self.janela ,text=f'CONFIRMAR', command=confirmaPet,  font=('arial 10'))
        bConfirma.pack(pady=10)


        


        self.exibirJanela()



    
