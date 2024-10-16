from tela import Tela
import tkinter as tk
from tkinter import messagebox as msg

class Agendamento(Tela):

    def __init__(self, nome, porte, nomeUsuario):
        super().__init__(nome)
        self.porte = porte
        self.nomeUsuario = nomeUsuario
        
    
    def criarAgendamento(self):

        def confirmaAgendamento():
            msg.showinfo("Sucesso",f'Pré-Agendamento realizado com sucesso! Retornaremos o contato com os horários disponíveis no período escolhido.')

        self.criarJanela()
        
        
         
        #titulo agendamento
        lPorte = tk.Label(self.janela ,text=f'{self.porte}', font=('arial 10'))
        lPorte.pack(pady=10)
        
       
        
        lNomePet = tk.Label(self.janela ,text=f'Nome do Pet: *', font=('arial 10'))
        lNomePet.pack(pady=10)
        nomePet = tk.Entry(self.janela)
        nomePet.pack(pady=5)

        lTelefone = tk.Label(self.janela ,text=f'Telefone de Contato: *', font=('arial 10'))
        lTelefone.pack(pady=10)
        telefone = tk.Entry(self.janela)
        telefone.pack(pady=5)

        hora = ['Manhã', 'Tarde', 'Noite']
        for i in hora:
            b = tk.Button(self.janela ,text=f'{i}',  font=('arial 10'))
            b.pack(pady=10)

        bConfirma = tk.Button(self.janela ,text=f'AGENDAR', command=confirmaAgendamento,  font=('arial 10'))
        bConfirma.pack(pady=10)

        
            

        self.exibirJanela()
