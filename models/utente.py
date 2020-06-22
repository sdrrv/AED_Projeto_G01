from .pessoa import Pessoa
from .tad_utente import Tad_Utente
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Utente(Pessoa,Tad_Utente):
    def __init__(self,nome,Faixa_Etaria):
        Pessoa.__init__(self,nome)
        self.faixa_etaria=Faixa_Etaria 
        self.lista_de_cuidados = SinglyLinkedList()
    
    def get_faixa_etaria(self):
        return self.faixa_etaria

    def get_cuidados(self):
        return self.lista_de_cuidados
    
    def add_to_cuidados(self, cuidado):
        self.lista_de_cuidados.insert_last(cuidado)

    def remove_cuidados(self, cuidados):
        self.lista_de_cuidados.make_empty()
