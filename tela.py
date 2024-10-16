import tkinter as tk

class Tela:
    def __init__(self, nome):
        self.nome = nome 
        self.janela = None

    def criarJanela(self):
        self.janela = tk.Tk()
        self.janela.geometry('800x450')
        self.janela.resizable(False, False)
        self.janela.title(f'{self.nome}')

    def exibirJanela(self):
        # exibindo a janela
        self.janela.mainloop()