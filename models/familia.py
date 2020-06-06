from .tad_familia import Familia
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Familia(Familia):
    def __init__(self,nome):
        self.nome=nome
        self.membros= SinglyLinkedList()
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_name(self):
        return self.nome

    def add_member(self, utente):
        self.membros.insert_first(utente)

    def remove_member(self,utente):
        position = self.membros.find(utente)
        self.membros.remove(position)
        

    def get_fila_de_cuidados(self):
        return self.lista_de_cuidados

    def add_to_fila_de_ciudados(self, cuidado): # Duvida, ver em proissionais.
        self.lista_de_cuidados.insert_last(cuidado)
    
    def remove_from_cuidados(self):# duvida ver em prifissionais.
        self.lista_de_cuidados.remove_last()
    
