from abc import ABC, abstractmethod
from .tad_pessoa import Pessoa

class Profissional(ABC,Pessoa):
    #Returns the Category of the profissional 
    @abstractmethod
    def get_categoria(self):
        pass

    #add to the cuidados list of the professional
    @abstractmethod
    def add_to_cuidados(self,cuidado):
        pass

    #removes a cuidado from the cuidados list    
    @abstractmethod
    def remove_from_cuidados(self,cuidado):
        pass

    #returns a the cuidados list
    @abstractmethod
    def get_cuidados(self):
        pass