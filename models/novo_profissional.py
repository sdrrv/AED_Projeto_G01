from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable


class Profissional():
    def __init__(self, nome, categoria):
        self.name = nome
        self.categoria = categoria
        self.lista_de_cuidados = HashTable()

    def get_categoria(self):
        return self.categoria

    def add_to_cuidados(self, cuidado):
        utente = cuidado.get_utente()
        # ver se passo antes o objecto
        if not self.lista_de_cuidados.has_key(utente):
            pass
