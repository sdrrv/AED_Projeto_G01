from .pessoa import Pessoa
from .tad_utente import Utente
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Utente(Pessoa,Utente):
    def __init__(self,nome,Faixa_Etaria):
        Pessoa.__init__(self,nome)
        self.faixa_etaria=Faixa_Etaria 
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_faixa_etaria(self):
        pass

    def get_fila(self):
        pass
    
    def add_to_fila(self, cuidado):
        pass
