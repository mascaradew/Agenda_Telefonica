from tkinter import messagebox
from Model import Model


class Controller:
     def __init__(self, AgendaTelefonica):
        self.viewAgenda = AgendaTelefonica
        self.model = Model()

     def Salvar(self, nome, telefone, tipo, favorito):
         try:
            if self.viewAgenda.entryNome.get() == '':
                msgNome = "Nome em Branco!"
                messagebox.showinfo("Cadastro de Contato", msgNome)
            elif self.viewAgenda.entryTelefone.get() == '':
                msgTelefone = "Telefone em Branco!"
                messagebox.showinfo("Cadastro de Contato", msgTelefone)
            elif self.viewAgenda.radioValue.get() == self.viewAgenda.radioComercial.deselect() or self.viewAgenda.radioPessoal.deselect():
                msgTipo = "Para Criar um novo Cadastro é necessario \n"
                messagebox.showinfo("Cadatro de Consulta Aviso!", msgTipo)
            #Chama o model
            else: self.model.salvar_contato(str(nome), str(telefone), str(tipo), str(favorito))
           # else: self.model.salvar_contato(str(self.viewAgenda.entryNome.get()), str(self.viewAgenda.entryTelefone.get()),
           #                           chr(self.viewAgenda.radioGeral.get()), bool(self.viewAgenda.favoritosSim.get()))

         except Exception as erro:
            print(f'Erro em Salvar os Dados {erro.args}')

         else: messagebox.showinfo(title='Salvar Contato', message='Contato Salvo com Sucesso!')


     def Buscar(self, nome):
         try:
            self.model.buscar_contato(nome)
            messagebox.showinfo(title='Contato', message=self.model.dict[nome])
         except:
            messagebox.showerror(title='Erro:', message='Contato não encontrado')

     def Excluir(self, nome):
         try:
            self.model.remover_contato(nome)
            messagebox.showinfo(title='Excluir Contato', message='Contato Excluido com Sucesso!')

         except Exception as erro:
            print(f'Error em Tentar Excluir {erro.args}')
