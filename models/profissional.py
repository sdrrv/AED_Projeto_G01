from .tad_profissional import Tad_Profissional
from .pessoa import Pessoa
from aed_ds.dictionaries.hash_table import  HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Profissional(Tad_Profissional,Pessoa):
    def __init__(self, nome, categoria):
        Pessoa.__init__(self,nome)
        self.categoria=categoria
        self.lista_de_cuidados = HashTable()
    
    def get_categoria(self):
        return self.categoria
    
    def add_to_cuidados(self, cuidado):
        utente= cuidado.get_utente()
        if not self.get_cuidados().has_key(utente): 
            self.lista_de_cuidados.insert(utente,SinglyLinkedList())

        utente_list = self.get_cuidados().get(utente)
        utente_list.insert_last(cuidado)

    def remove_utente_from_cuidados(self,utente):
        self.get_cuidados().remove(utente)

    def get_cuidados(self):
        return self.lista_de_cuidados
    
    def has_cuidados(self):
        return self.get_cuidados().is_empty()
