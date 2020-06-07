from .tad_pessoa import Pessoa


class Pessoa(Pessoa):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
