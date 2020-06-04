from .tad_profissional import Profissional
from .pessoa import Pessoa

class Profissional(Profissional,Pessoa):
    def __init__(self, nome, categoria):
        Pessoa.__init__(self,nome)
        self.get_categoria=categoria
        #self.lista_de_cuidados = SinglelyList()
    
    def get_categoria(self):
        return self.get_categoria
    
    def add_to_cuidados(self, cuidado):
        pass

    def remove_from_cuidados(self, cuidado):
        pass

    def get_cuidados(self):
        pass
    
