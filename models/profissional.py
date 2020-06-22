from .tad_profissional import Tad_Profissional
from .pessoa import Pessoa
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Profissional(Tad_Profissional,Pessoa):
    def __init__(self, nome, categoria):
        Pessoa.__init__(self,nome)
        self.categoria=categoria
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_categoria(self):
        return self.categoria
    
    def add_to_cuidados(self, cuidado):
        self.lista_de_cuidados.insert_last(cuidado)

    def remove_from_cuidados(self):
        self.lista_de_cuidados.make_empty()

    def get_cuidados(self):
        return self.lista_de_cuidados
    
