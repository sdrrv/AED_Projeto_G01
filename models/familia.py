from .tad_familia import Familia
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Familia(Familia):
    def __init__(self,nome):
        self.nome=nome
        self.membros= SinglyLinkedList()
    
    def get_name(self):
        return self.nome

    def add_member(self, utente):
        self.membros.insert_first(utente)

    def remove_member(self,utente):
        position = self.membros.find(utente)
        self.membros.remove(position)
