from ModelPersistencia import Persistencia


class Model:
    # Inicializando a persistencia em disco
    def __init__(self) -> None:

        self.modelPersistencia = Persistencia()

        self.dict = self.modelPersistencia.contact_data

    def sair(self):
        self.modelPersistencia.sair(self.dict)

    def salvar_contato(self, nome: str, telefone: str, tipo: str, favorito: bool) -> None:
        self.dict[nome] = nome, telefone, tipo, favorito
        self.modelPersistencia.gravar_agenda()

    def remover_contato(self, nome: str) -> None:
        try:
            del self.dict[nome]
        except KeyError:
            raise ValueError('Contato não encontrado.')

    def buscar_contato(self, nome: str) -> dict:

        if nome in self.dict:
            return nome, self.dict[nome]
        else:
            raise ValueError('Contato não encontrado.')
