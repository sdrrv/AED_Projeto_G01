from .tad_familia import Tad_Familia
from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList


class Familia(Tad_Familia):
    def __init__(self, nome):
        self.nome = nome
        self.membros = HashTable()
        self.membros_que_teem_cuidados = SinglyLinkedList()
        self.fetaria = HashTable()
        self.fetaria.insert('Jovem', HashTable())
        self.fetaria.insert('Adulto', HashTable())
        self.fetaria.insert('Idoso', HashTable())

    def get_name(self):
        return self.nome

    def get_members(self):
        return self.membros

    def get_jovens(self):
        return self.fetaria.get('Jovem').keys()

    def get_adultos(self):
        return self.fetaria.get('Adulto').keys()

    def get_idosos(self):
        return self.fetaria.get('Idoso').keys()

    def add_member(self, utente):
        self.membros.insert(utente.get_name(), utente)
        self.fetaria.get(utente.get_faixa_etaria()).insert(
            utente.get_name(), utente)

    def remove_member(self, nome):
        self.membros.remove(nome)

    def get_membros_que_teem_cuidados(self):
        return self.membros_que_teem_cuidados

    def has_cuidados(self):  # returns true if the list is not empty
        return not self.get_membros_que_teem_cuidados().is_empty()

