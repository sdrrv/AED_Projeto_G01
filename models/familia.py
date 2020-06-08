from .tad_familia import Familia
from aed_ds.dictionaries.hash_table import HashTable

class Familia(Familia):
    def __init__(self,nome):
        self.nome=nome
        self.membros = HashTable()
    
    def get_name(self):
        return self.nome
    
    def get_members(self):
        return self.membros

    def add_member(self, utente):
        self.membros.insert_first(utente)

    def remove_member(self,utente):
        position = self.membros.find(utente)
        self.membros.remove(position)
