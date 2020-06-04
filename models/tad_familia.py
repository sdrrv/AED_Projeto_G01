from abc import ABC, abstractmethod

class Familia(ABC):

    #Returns the serviço of the cuidado
    @abstractmethod
    def get_name(self):
        pass
    
    #returns the professional in charge of the ciudado
    @abstractmethod
    def get_members(self):
        pass

    #returns the categoria of the cuidado
    @abstractmethod
    def add_member(self,utente):
        pass
    #Remove a member from the familly
    @abstractmethod
    def remove_member(self):
        pass
    #Retruns a List with all the cuidados
    @abstractmethod
    def get_fila_de_cuidados(self):
        pass
    #adds a ciudado to the cuidado list
    @abstractmethod
    def add_to_fila_de_ciudados(self,cuidado):
        pass