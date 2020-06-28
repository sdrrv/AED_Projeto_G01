from .pessoa import Pessoa
from .tad_utente import Tad_Utente
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Utente(Pessoa,Tad_Utente):
    def __init__(self,nome,Faixa_Etaria):
        Pessoa.__init__(self,nome)
        self.faixa_etaria=Faixa_Etaria 
        self.lista_de_cuidados = SinglyLinkedList()
        self.familia = None # Sting nome familia
    
    def get_faixa_etaria(self):
        return self.faixa_etaria

    def get_cuidados(self):
        return self.lista_de_cuidados
    
    def add_to_cuidados(self, cuidado):
        self.lista_de_cuidados.insert_last(cuidado)

    def remove_cuidados(self):
        self.lista_de_cuidados.make_empty()
    
    def get_familia(self):
        return self.familia

    def remove_familia(self):
        self.familia= None
    
    def set_familia(self,NomeFamila):
        self.familia = NomeFamila
    
    def has_familia(self): #Returns true if the utente is in a familia
        if self.get_familia():
            return True
        return False
    
    def has_cuidados(self):
        return self.get_cuidados().is_empty()

    def merge_list(self,list_to_merge):
        lista=self.lista_de_cuidados