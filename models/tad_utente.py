from abc import ABC, abstractmethod

class Utente(ABC):
    #Returns the faixa etaria of the utente
    @abstractmethod
    def get_faixa_etaria(self):
        pass
    
    #Returns the fila of Medical appointments of the Utente
    @abstractmethod
    def get_cuidados(self):
        pass

    #Adds a Medical appointment to the Utente.
    @abstractmethod
    def add_to_cuidados(self,cuidado):
        pass

    #Removes a Medical appointment of the Utente
    def remove_cuidados(self, cuidados):
        pass