from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable


class Utente():
    def __init__(self, nome, faixa):
        self.nome = nome
        self.faixa = faixa
        self.familia = None

    def get_nome(self):
        return self.nome

    def get_faixa(self):
        return self.faixa

    def get_familia(self):
        return self.familia

    def has_familia(self):
        return self.familia == None

    def set_familia(self, name):
        self.familia = name
