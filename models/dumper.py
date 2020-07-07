from aed_ds.lists.singly_linked_list import SinglyLinkedList
from .tad_dumper import Tad_Dumper


class Dumper(Tad_Dumper):
    def __init__(self):
        self.lista = SinglyLinkedList()

    def add_item(self, item):
        self.lista.insert_last(item)

    def get_items(self):
        return self.lista

    def get_size(self):
        return self.lista.size()
