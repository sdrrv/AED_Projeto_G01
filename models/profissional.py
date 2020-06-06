from .tad_profissional import Profissional
from .pessoa import Pessoa
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Profissional(Profissional,Pessoa):
    def __init__(self, nome, categoria):
        Pessoa.__init__(self,nome)
        self.categoria=categoria
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_categoria(self):
        return self.categoria
    
    def add_to_cuidados(self, cuidado):
        self.lista_de_cuidados.insert_last(cuidado)

    def remove_from_cuidados(self, cuidado): # Duvida, quando removemos um cuidado, temos de remover todos os cuidados adicionados ao mesmo tempo?
        self.lista_de_cuidados.remove_last()

    def get_cuidados(self):
        return self.lista_de_cuidados
    
