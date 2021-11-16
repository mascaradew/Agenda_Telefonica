import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def donothing():
    pass


class View():
    def __init__(self):
        self.root = tk.Tk()

        self.menu()
        self.tutor()
        self.animal()
        self.pesoDoAnimal()
        self.atendimento()
        self.tipoDeAtendimento()
        self.gerouInternamento()

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
        fileMenu.add_command(label='Novo', command=self.novo)
        fileMenu.add_separator()

        # Cria outro menu, dentro do menu Arquivo
        # Cria o menu
        salvarMenu = tk.Menu(menubar, tearoff=0)

        # Insere o menu Salvar em Arquivo
        fileMenu.add_cascade(label='Salvar', menu=salvarMenu)

        # Insere os comando Salvar e Salvar Como
        salvarMenu.add_command(label='Salvar', command=donothing())
        salvarMenu.add_command(label='Salvar Como', command=donothing())

        # Adiciona um separador
        fileMenu.add_separator()

        #Insere o Comando para Limpar os Dados
        fileMenu.add_command(label='Limpar Dados', command=self.limparDados)
        fileMenu.add_separator()

        # Insere os comandos Imprimir e Sair
        fileMenu.add_command(label='Imprimir', command=self.imprimir)
        fileMenu.add_command(label='Sair', command=self.close)

        # No menu Ajuda, insere os comandos ajuda e sobre
        helpMenu.add_command(label='Ajuda', command=donothing())
        helpMenu.add_command(label='Sobre', command=donothing())

    def tutor(self):
        container = tk.Frame(self.root)
        container.pack()

        # Grid posiciona os componentes como uma tabela, organizados por
        # linhas e colunas
        labelNome = tk.Label(container, width=20, text='Nome:')
        labelNome.grid(column=0, row=0, padx=5, pady=5)

        self.entryNome = tk.Entry(container, width=20)
        self.entryNome.grid(column=1, row=0, padx=5, pady=5)

        labelTelefone=tk.Label(container, width=20, text='Telefonel:')
        labelTelefone.grid(column=0, row=1, padx=5, pady=5)

        self.entryTelefone=tk.Entry(container, width=20)
        self.entryTelefone.grid(column=1, row=1, padx=5, pady=5)

        labelEmail = tk.Label(container, width=20, text='Email:')
        labelEmail.grid(column=0, row=2, padx=5, pady=5)

        self.entryEmail = tk.Entry(container, width=20)
        self.entryEmail.grid(column=1, row=2, padx=5, pady=5)

    def animal(self):
        container = tk.Frame(self.root)
        container.pack()

        labelAnimal = tk.Label(container, width=20, text='Animal:')
        labelAnimal.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para receber o valor do radiobutton
        self.radioValue = tk.StringVar()

        # Cria um radiobutton
        self.radioUm = tk.Radiobutton(container, text='Cão', width=20,
                                      # Associa a variável 'radioValue'
                                      # com a string 'Cão'
                                      variable=self.radioValue, value='Cão',
                                      # Alinha a esqueda 'WEST'
                                      anchor=tk.W)
        # Insere o botão
        self.radioUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioDois = tk.Radiobutton(container, text='Gato', width=20,
                                        variable=self.radioValue,
                                        value='Gato',
                                        anchor=tk.W)
        self.radioDois.grid(column=1, row=1, padx=5, pady=5)

        self.radioTres = tk.Radiobutton(container, text='Outro', width=20,
                                        variable=self.radioValue,
                                        value='Outro',
                                        anchor=tk.W)
        self.radioTres.grid(column=1, row=2, padx=5, pady=5)

    def pesoDoAnimal(self):
        container = tk.Frame(self.root)
        container.pack()

        labelPesoDoAnimal = tk.Label(container, width=20, text='Peso do Animal:')
        labelPesoDoAnimal.grid(column=0, row=1, padx=5, pady=5)

        # Cria uma variável para receber o peso do Animal
        self.peso = tk.DoubleVar()

        # Cria a escala
        escalaPesoAnimal = tk.Scale(container, from_=0, to=50, width=20,
                                 length=200, variable=self.peso,
                                 orient=tk.HORIZONTAL)
        escalaPesoAnimal.grid(column=1, row=1, padx=5, pady=5)

    def atendimento(self):
        container = tk.Frame(self.root)
        container.pack()

        labelAtendimento = tk.Label(container, width=20, text='Atendimento:')
        labelAtendimento.grid(column=0, row=0, padx=5, pady=5)

        # Cria um combobox com as opções: 'Ana, 'Paulo' e 'Carol'
        # Precisa da importação de ttk, que expande o TK
        self.comboAtendimento = ttk.Combobox(container, width=20,
                                            values=['Ana',
                                                    'Paulo',
                                                    'Carol'])
        self.comboAtendimento.grid(column=1, row=0, padx=5, pady=5)

    def tipoDeAtendimento(self):
        container = tk.Frame(self.root)
        container.pack()

        labelTipoAtendimento=tk.Label(container, width=20, text='Tipo de Atendimento:')
        labelTipoAtendimento.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para armazenar o valor do botão
        self.agendamento=tk.BooleanVar()
        self.emergencia=tk.BooleanVar()

        # Cria o botão associado à variavel e alinhado à esquerda
        chkBttn=tk.Checkbutton(container, text='Agendamento', width=20,
                               variable=self.agendamento, anchor=tk.W)
        # Insere o botão
        chkBttn.grid(column=1, row=0, padx=5, pady=5)

        chkBttn=tk.Checkbutton(container, text='Emergência', width=20,
                               variable=self.emergencia, anchor=tk.W)
        chkBttn.grid(column=1, row=1, padx=5, pady=5)

    def gerouInternamento(self):
        container = tk.Frame(self.root)
        container.pack()

        labelGerouInternamento=tk.Label(container, width=20, text='Gerou Internamento?')
        labelGerouInternamento.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para receber o valor do radiobutton
        self.radioResposta=tk.StringVar()

        # Cria um radiobutton
        self.radioRespUm=tk.Radiobutton(container, text='Sim', width=20,
                                    # Associa a variável 'radioResposta'
                                    # com a string 'Cão'
                                    variable=self.radioResposta, value='Sim',
                                    # Alinha a esqueda 'WEST'
                                    anchor=tk.W)
        # Insere o botão
        self.radioRespUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioRespDois=tk.Radiobutton(container, text='Não', width=20,
                                      variable=self.radioResposta,
                                      value='Não',
                                      anchor=tk.W)
        self.radioRespDois.grid(column=1, row=1, padx=5, pady=5)


    def imprimir(self):
        print('Nome:', self.entryNome.get())
        print('Email:', self.entryEmail.get())
        print('Telefone:', self.entryTelefone.get())

        print('Animal:', self.radioValue.get())

        print('Peso:', self.peso.get())

        print('Tipo de Atendimento:')
        print('\tAgendamento:', self.agendamento.get())
        print('\tEmergecia:', self.emergencia.get())

        print('Atendimento:', self.comboAtendimento.get())
        print('Gerou Internamento:', self.radioResposta.get())

    def novo(self):
        # caixa de mensagem tipo Informacao
        # usado para notificar campo não preenchido do Tutor
        if self.entryNome.get() == '':
            msgNome = "Para Criar um novo Cadastro é necessario \n"
            msgNome += "que informe um Nome!"
            messagebox.showinfo("Cadatro de Consulta Aviso!", msgNome)
        elif self.entryTelefone.get() == '':
            msgTelefone = "Para Criar um novo Cadastro é necessario \n"
            msgTelefone += "que informe seu Telefone!"
            messagebox.showinfo("Cadatro de Consulta Aviso!", msgTelefone)
        elif self.entryEmail.get() == '':
            msgEmail = "Para Criar um novo Cadastro é necessario \n"
            msgEmail += "que informe um Email!"
            messagebox.showinfo("Cadatro de Consulta Aviso!", msgEmail)
        # Usado para notifcar que nenhum campo foi selecionado no Animal
        elif self.radioValue.get() == self.radioUm.deselect() or self.radioDois.deselect() or self.radioTres.deselect():
            msgEmail = "Para Criar um novo Cadastro é necessario \n"
            msgEmail += "que informe o Animal !"
            messagebox.showinfo("Cadatro de Consulta Aviso!", msgEmail)
        # notificar que selecione um Atendente
        # elif self.atendimento() == '':
        #     msgAtendente = "Selecione um dos Atendendes!"
        #     messagebox.showinfo("Cadastro de Consulta Aviso!", msgAtendente)
        # elif self.atendimento() != self.comboAtendimento():
        #     msgAte = "Atendente Invalido"
        #     messagebox.showerror("Cadastro de Consulta Erro!", msgAte)

        self.entryNome.delete(0, 100)
        self.entryEmail.delete(0, 100)
        self.entryTelefone.delete(0, 100)
        self.radioUm.deselect()
        self.radioDois.deselect()
        self.radioTres.deselect()
        self.peso.set(0)
        self.agendamento.set(False)
        self.emergencia.set(False)
        self.comboAtendimento.set('')
        self.radioRespUm.deselect()
        self.radioRespDois.deselect()

        print('Nome:', self.entryNome.get())
        print('Email:', self.entryEmail.get())
        print('Telefone:', self.entryTelefone.get())
        print('Animal:', self.radioValue.get())
        print('Peso:', self.peso.get())
        print('Tipo de Atendimento:')
        print('\tAgendamento:', self.agendamento.get())
        print('\tEmergecia:', self.emergencia.get())
        print('Atendimento:', self.comboAtendimento.get())
        print('Gerou Internamento:', self.radioResposta.get())

    def limparDados(self):

        msgDadosLimpos = "Os dados foram limpos comm Sucesso!"
        messagebox.showinfo("Cadatro de Consulta!", msgDadosLimpos)

        self.entryNome.delete(0, 100)
        self.entryEmail.delete(0, 100)
        self.entryTelefone.delete(0, 100)

        self.radioUm.deselect()
        self.radioDois.deselect()
        self.radioTres.deselect()

        self.peso.set(0)

        self.agendamento.set(False)
        self.emergencia.set(False)

        self.comboAtendimento.set('')

        self.radioRespUm.deselect()
        self.radioRespDois.deselect()

        print('Nome:', self.entryNome.get())
        print('Email:', self.entryEmail.get())
        print('Telefone:', self.entryTelefone.get())

        print('Animal:', self.radioValue.get())

        print('Peso:', self.peso.get())

        print('Tipo de Atendimento:')
        print('\tAgendamento:', self.agendamento.get())
        print('\tEmergecia:', self.emergencia.get())

        print('Atendimento:', self.comboAtendimento.get())
        print('Gerou Internamento:', self.radioResposta.get())


    def close(self, evento=None):
        sys.exit()


Janela = View()
