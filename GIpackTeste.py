#
# Autor: William Yamada
#

import sys
import tkinter as tk
from tkinter import messagebox


def donothing():
    pass

class View():
    def __init__(self):
        self.root = tk.Tk()

        self.menu()
        self.contatos()
        self.tipoContatos()
        self.favoritos()

        self.buscarContato()
        self.excluir()
        self.salvar

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def menu(self):
        # Cria o menu principal
        menubar = tk.Menu(self.root)
        # Associa o menu à janela raiz
        self.root.config(menu=menubar)

        # Cria os menus Arquivo e Ajuda
        fileMenu = tk.Menu(menubar, tearoff=0)
        helpMenu = tk.Menu(menubar, tearoff=0)

        # Insere os menus no estilo cascata ao menu principal
        menubar.add_cascade(label='Arquivo', menu=fileMenu)
        menubar.add_cascade(label='Ajuda', menu=helpMenu)

        # Configura o menu Arquivo inserindo o comando Novo
        fileMenu.add_command(label='Buscar Contato', command=self.novoContato())
        fileMenu.add_separator()

        # Cria outro menu, dentro do menu Arquivo
        salvarMenu = tk.Menu(menubar, tearoff=0)

        # Insere o menu Salvar em Arquivo
        fileMenu.add_cascade(label='Salvar', menu=salvarMenu)

        # Insere os comando Salvar e Salvar Como
        salvarMenu.add_command(label='Salvar', command=donothing())

        # Adiciona um separador
        fileMenu.add_separator()

        #Insere o Comando para Limpar os Dados
        fileMenu.add_command(label='Excluir', command=self.excluir())
        fileMenu.add_separator()

        # Insere os comandos Imprimir e Sair
        fileMenu.add_command(label='Buscar Contatos', command=self.buscarContato())
        fileMenu.add_command(label='Sair', command=self.close)

        # No menu Ajuda, insere os comandos ajuda e sobre
        helpMenu.add_command(label='Ajuda', command=donothing())
        helpMenu.add_command(label='Sobre', command=donothing())

    def contatos(self):
        container = tk.Frame(self.root)
        container.pack()

        # Grid posiciona os componentes como uma tabela, organizados por linhas e colunas
        labelNome = tk.Label(container, width=20, text='Nome:')
        labelNome.grid(column=0, row=0, padx=5, pady=5)

        self.entryNome = tk.Entry(container, width=20)
        self.entryNome.grid(column=1, row=0, padx=5, pady=5)

        labelTelefone=tk.Label(container, width=20, text='Telefonel:')
        labelTelefone.grid(column=0, row=1, padx=5, pady=5)

        self.entryTelefone=tk.Entry(container, width=20)
        self.entryTelefone.grid(column=1, row=1, padx=5, pady=5)

    def tipoContatos(self):
        container = tk.Frame(self.root)
        container.pack()

        labelTipo = tk.Label(container, width=20, text='Tipo:')
        labelTipo.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para receber o valor do radiobutton
        self.radioValue = tk.StringVar()

        # Cria um radiobutton
        self.radioUm = tk.Radiobutton(container, text='Comercial', width=20,
                                      # Associa a variável 'radioValue' com a string 'Comercial'
                                      variable=self.radioValue, value='Comercial',
                                      # Alinha a esqueda 'WEST'
                                      anchor=tk.W)
        # Insere o botão
        self.radioUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioDois = tk.Radiobutton(container, text='Pessoal', width=20,
                                        variable=self.radioValue,
                                        value='Pessoal',
                                        anchor=tk.W)
        self.radioDois.grid(column=1, row=1, padx=5, pady=5)

    def favoritos(self):
        container = tk.Frame(self.root)
        container.pack()

        labelTipoAtendimento=tk.Label(container, width=20, text='Adicionar aos Favoritos:')
        labelTipoAtendimento.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para armazenar o valor do botão
        self.respSim=tk.BooleanVar()

        # Cria o botão associado à variavel e alinhado à esquerda
        chkBttn=tk.Checkbutton(container, text='Sim', width=20,
                               variable=self.respSim, anchor=tk.W)
        # Insere o botão
        chkBttn.grid(column=1, row=0, padx=5, pady=5)



    def buscarContato(self):
        print('Nome:', self.entryNome.get())
        print('Telefone:', self.entryTelefone.get())

        print('Tipo:', self.radioValue.get())

        print('Adicionado aos Favavoritos: ', self.respSim.get())

    def novoContato(self):
        # caixa de mensagem tipo Informacao
        # usado para notificar campo não preenchido do Contato
        if self.entryNome.get() == '':
            msgNome = "Para Criar um novo Cadastro é necessario \n"
            msgNome += "que informe um Nome!"
            messagebox.showinfo("Cadatro de Contato Aviso!", msgNome)
        elif self.entryTelefone.get() == '':
            msgTelefone = "Para Criar um novo Cadastro é necessario \n"
            msgTelefone += "que informe seu Telefone!"
            messagebox.showinfo("Cadatro de Contato Aviso!", msgTelefone)

        self.entryNome.delete(0, 100)
        self.entryTelefone.delete(0, 100)

        self.radioUm.deselect()
        self.radioDois.deselect()

        self.respSim.set(False)

        print('Nome:', self.entryNome.get())
        print('Telefone:', self.entryTelefone.get())

        print('Tipo:', self.radioValue.get())

        print('Adicionado aos Favoritos: ', self.respSim.get())

    def excluir(self):

        msgDadosLimpos = "Os dados foram excluidos com Sucesso!"
        messagebox.showinfo("Cadatro de Contatos!", msgDadosLimpos)

        self.entryNome.delete(0, 100)
        self.entryTelefone.delete(0, 100)

        self.radioUm.deselect()
        self.radioDois.deselect()

        self.respSim.set(False)

        print('Nome:', self.entryNome.get())
        print('Telefone:', self.entryTelefone.get())

        print('Tipo:', self.radioValue.get())

        print('Adicionado: ', self.respSim.get() )


    def close(self, evento=None):
        sys.exit()


Janela = View()
