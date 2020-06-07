from .tad_pessoa import Pessoa


class Pessoa(Pessoa):
    def __init__(self, nome):
        self.nome = nome

    def get_name(self):
        return self.name
