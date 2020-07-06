from aed_ds.lists.singly_linked_list import SinglyLinkedList
from abc import ABC, abstractmethod


class Tad_Dumper(ABC):

    # Adds the item at the end of the list
    @abstractmethod
    def add_item(self, item):
        pass

    # Returns the list that has stored
    @abstractmethod
    def get_items(self):
        pass
