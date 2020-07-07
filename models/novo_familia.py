from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable


class Familia():
    def __init__(self, nome):
        self.nome = nome
        self.membros = HashTable()

    def get_nome(self):
        return self.nome

    def get_membros(self):
        return self.membros.values()

    def add_member(self, member):
        self.membros.insert(member.get_nome(), member)

    def remove_member(self, member):
        self.membros.remove(member.get_nome())
