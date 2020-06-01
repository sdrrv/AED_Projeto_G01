from abc import ABC, abstractmethod
from .tad_pessoa import Pessoa

class Utente(ABC,Pessoa):
    #Returns the faixa etaria of the utente
    @abstractmethod
    def get_faixa_etaria(self):
        pass
    
    #Returns the fila of Medical appointments of the Utente
    @abstractmethod
    def get_fila(self):
        pass

    #Adds an Medical appointment to the Utente.
    @abstractmethod
    def add_to_fila(self,cuidado):
        pass

