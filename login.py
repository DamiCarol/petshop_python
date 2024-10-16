
from tela import Tela
from principalualual import Principal
# Import da biblioteca de criação de GUI
import tkinter as tk
from tkinter import messagebox as msg

class Login(Tela):
        
    def __init__(self, nome):
        super().__init__(nome)
        


    def criarLogin(self):
            
        #validação
        def validaSenha():
                    
                nome = usuario.get()
                passw =  senha.get()
                    
                if nome == 'admim' and passw == '123':

                    msg.showinfo("Olá",'Bem vindo ao Pet Ual Ual')

                    #comando para fechar a janela atual por completo
                    self.janela.destroy()
                       
                    #nova janela
                    home = Principal('Ual Ual', 'Admim')
                    home.criarHome()
                                
                else:
                    usuario.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    senha.config(highlightbackground='red', highlightthickness=2, highlightcolor='red')
                    msg.showerror('Erro', 'Login incorreto')
                        
        self.criarJanela()
        #itulo da tela
        texto = tk.Label(self.janela ,text='acessar o pet', font=('arial 20'), bg='#aeb1f1', width=100)
        texto.pack(pady=10)
            
        # inputs de login
        lb_usuario = tk.Label(self.janela, text='Nome:*', font=('arial 8'), width=80, anchor='nw')
        lb_usuario.pack(pady=5)
        usuario = tk.Entry(self.janela, width=80, borderwidth=2)
        usuario.pack(pady=10)
        

        lb_senha = tk.Label(self.janela, text='Senha:*', font=('arial 8'), width=80, anchor='nw')
        lb_senha.pack(pady=5)
        senha = tk.Entry(self.janela, show='*', width=80, borderwidth=2)
        senha.pack(pady=10)

        # Criando o botão de validação
        botao = tk.Button(self.janela, text="fazer login", command=validaSenha, background='#2a356a', fg='white', padx=20, pady=10,borderwidth=0, relief='flat')
        botao.pack(padx=10, pady=10)

        self.exibirJanela()