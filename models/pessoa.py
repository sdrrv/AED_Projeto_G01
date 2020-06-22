from .tad_pessoa import Tad_Pessoa


class Pessoa(Tad_Pessoa):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
