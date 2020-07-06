from abc import ABC, abstractmethod

class Tad_Profissional(ABC):
    #Returns the Category of the profissional 
    @abstractmethod
    def get_categoria(self):
        pass

    #add to the cuidados list of the professional
    @abstractmethod
    def add_to_cuidados(self,cuidado):
        pass

    #removes a utente from the cuidados list    
    @abstractmethod
    def remove_utente_from_cuidados(self,cuidado):
        pass

    #returns a the cuidados list
    @abstractmethod
    def get_cuidados(self):
        pass

    @abstractmethod
    def has_cuidaddos(self):
        pass