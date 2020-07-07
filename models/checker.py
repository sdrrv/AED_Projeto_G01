from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable
import ctypes


class Checker():
    def __init__(self):
        self.checker = HashTable()

        self.checker.insert("Servico", False)
        self.checker.insert("Categoria", False)
        self.checker.insert("Profissional", False)
        self.checker.insert("CInvalida", False)
        self.checker.insert("SInvalida", False)

    def get(self, key):
        return self.checker.get(key)

    def checks_out(self):
        it = self.checker.values().iterator()
        while it.has_next():
            if it.next():
                return False
        return True

    def change_servico(self):
        self.checker.update('Servico', True)

    def change_categoria(self):
        self.checker.update('Categoria', True)

    def change_profissional(self):
        self.checker.update(
            'Profissional', True)

    def change_cinvalida(self):
        self.checker.update('CInvalida', True)

    def change_sinvalida(self):
        self.checker.update('SInvalida', True)
