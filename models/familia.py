from .tad_familia import Familia
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Familia(Familia):
    def __init__(self,nome):
        self.nome=nome
        self.membros= SinglyLinkedList()
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_name(self):
        pass

    def add_member(self, utente):
        pass

    def remove_member(self):
        pass

    def get_fila_de_cuidados(self):
        pass

    def add_to_fila_de_ciudados(self, cuidado):
        pass
    
