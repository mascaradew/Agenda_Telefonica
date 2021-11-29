#
#   Author: William Yamada
#

import tkinter as tk
import sys
from Controller import Controller
from Model import Model

def donothing():
    pass

# Classe view
class View():
    def __init__(self):
        #inicializando a interface

        self.root = tk.Tk()
        self.root.title("Agenda Telefônica")

        #istanciando o Controller na interface
        self.controller = Controller(self)

        self.model = Model

        self.menu()
        self.contatos()
        self.tipoContatos()
        self.favoritos()

        self.buscarContato()
        self.salvar()
        self.excluir()
        self.sair()


        self.root.bind('Saída', self.close)

        self.root.mainloop()

    def menu(self):
        #Criando o Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        #Cria subMenu Arquivo e Ajuda
        fileMenu = tk.Menu(menubar, tearoff=0)
        helpMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label= 'Arquivo', menu=fileMenu)
        menubar.add_cascade(label= 'Ajuda', menu=helpMenu)

        #Para inserir um Novo Cadastro
        fileMenu.add_command(label='Novo Contato', command=donothing())
        fileMenu.add_separator()
        #Para Salvar o cadastro
        fileMenu.add_cascade(label='Salvar Contato', command=self.clickSalvar)
        fileMenu.add_separator()
        #Para Imprimir o cadastro
        fileMenu.add_command(label='Imprimir Contato', command=donothing())
        fileMenu.add_separator()
        #Para sair da Agenda Telefonica
        fileMenu.add_command(label='Sair', command=self.close)

        # No menu Ajuda, insere os comandos ajuda e sobre
        helpMenu.add_command(label='Ajuda', command=donothing())
        helpMenu.add_separator()
        helpMenu.add_command(label='Sobre', command=donothing())

    def contatos(self):
        container = tk.Frame(self.root)
        container.pack()

        labelNome = tk.Label(container, width=20, text='Nome: ')
        labelNome.grid(column=0, row=0, padx=5, pady=5)
        self.entryNome = tk.Entry(container, width=20)
        self.entryNome.grid(column=1, row=0, padx=5, pady=5)

        labelTelefone=tk.Label(container, width=20, text='Telefone:')
        labelTelefone.grid(column=0, row=1, padx=5, pady=5)
        self.entryTelefone=tk.Entry(container, width=20)
        self.entryTelefone.grid(column=1, row=1, padx=5, pady=5)

    def tipoContatos(self):
        container = tk.Frame(self.root)
        container.pack()

        labelTipoContatos = tk.Label(container, width=20, text='Tipo de Contato:')
        labelTipoContatos.grid(column=0, row=0, padx=5, pady=5)

        #Criando o botao para selecionar
        self.radioValue = tk.StringVar()

        self.radioComercial = tk.Radiobutton(container, text='Comercial', width=20, variable=self.radioValue,
                                             value='comercial', anchor=tk.W)
        self.radioComercial.grid(column=1, row=0, padx=5, pady=5)

        self.radioPessoal = tk.Radiobutton(container, text='Pessoal', width=20, variable=self.radioValue,
                                             value='pessoal', anchor=tk.W)
        self.radioPessoal.grid(column=1, row=1, padx=5, pady=5)

    def favoritos(self):
        container = tk.Frame(self.root)
        container.pack()

        labelFavoritos = tk.Label(container, width=20, text='Adicionar aos Favoritos: ')
        labelFavoritos.grid(column=0, row=0, padx=5, pady=5)

        self.favoritosSim = tk.BooleanVar()

        chkBttn=tk.Checkbutton(container, text='Sim', width=20,
                               variable=self.favoritosSim, anchor=tk.W)
        chkBttn.grid(column=1, row=0, padx=5, pady=5)


    def buscarContato(self):
        container = tk.Frame(self.root)
        container.pack()

        self.buttonBuscarContato = tk.Button(container, width=20, text='Buscar Contato', command=self.clickBuscar)
        self.buttonBuscarContato.pack()

    def clickBuscar(self):
        nome = self.entryNome.get()
        self.controller.Buscar(nome)

    def salvar(self):
        container = tk.Frame(self.root)
        container.pack()

        self.buttonSalvar = tk.Button(container, width=20, text='Salvar Contato', command=self.clickSalvar)
        self.buttonSalvar.pack()

    def clickSalvar(self):
        nome = self.entryNome.get()
        telefone = self.entryTelefone.get()
        tipo = self.radioValue.get()
        favorito = self.favoritosSim.get()
        self.controller.Salvar(nome, telefone, tipo, favorito)


    def excluir(self):
        container = tk.Frame(self.root)
        container.pack()

        self.buttonExcluir = tk.Button(container, width=20, text='Excluir Contato', command=self.clickExcluir)
        self.buttonExcluir.pack()

    def clickExcluir(self):
        nome = self.entryNome.get()
        self.controller.Excluir(nome)

    def sair(self):
        container = tk.Frame(self.root)
        container.pack()

        self.buttonAlterar = tk.Button(container, width=20, text='Sair', command=self.close)
        self.buttonAlterar.pack()

    #def imprimir(self):
       # print('Nome:', self.entryNome.get())
       # print('Telefone:', self.entryTelefone.get())
       # print('Tipo:', self.radioValue.get())
       # print('Favorito:', self.favoritosSim.get())

    def close(self, evento=None):
        self.controller.model.sair()
        sys.exit()


Janela = View()
