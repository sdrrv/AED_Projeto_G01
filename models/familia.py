from .tad_familia import Tad_Familia
from aed_ds.dictionaries.hash_table import HashTable

class Familia(Tad_Familia):
    def __init__(self,nome):
        self.nome=nome
        self.membros = HashTable()
    
    def get_name(self):
        return self.nome
    
    def get_members(self):
        return self.membros

    def add_member(self, utente):
        self.membros.insert(utente.get_name(),utente)

    def remove_member(self,utente):
        position = self.membros.find(utente)
        self.membros.remove(position)
