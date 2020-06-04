from abc import ABC, abstractmethod

class Cuidados(ABC):

    #Returns the serviço of the cuidado
    @abstractmethod
    def get_servico(self):
        pass

    #returns the professional in charge of the ciudado
    @abstractmethod
    def get_profissional(self):
        pass

    #returns the categoria of the cuidado
    @abstractmethod
    def get_categoria(self):
        pass
    
    #return the object utente
    @abstractmethod
    def get_utente(self):
        pass