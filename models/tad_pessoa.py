from abc import ABC, abstractmethod

class Tad_Pessoa(ABC):
    #Returns the name of the Person
    @abstractmethod
    def get_name(self):
        pass