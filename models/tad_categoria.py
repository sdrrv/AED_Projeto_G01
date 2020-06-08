from abc import ABC, abstractmethod

class Categoria(ABC):
    #returns professionals in the categoria
    @abstractmethod
    def get_members(self):
        pass

    # adds a professional to the categoria
    @abstractmethod
    def add_member(self,professional):
        pass