from pessoa import Pessoa


class Utente(Pessoa):
    def __init__(self, nome):
        self.nome = nome
        # self.dicionario = hashtable(20)
