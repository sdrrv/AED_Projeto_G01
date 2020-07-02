from .pessoa import Pessoa
from .tad_utente import Tad_Utente
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable

class Utente(Pessoa,Tad_Utente):
    def __init__(self,nome,Faixa_Etaria):
        Pessoa.__init__(self,nome)
        self.faixa_etaria=Faixa_Etaria 
        self.lista_de_cuidados = SinglyLinkedList()
        self.familia = None # Sting nome familia
        self.profissionais_in = HashTable()
        self.serviços_in= HashTable()
    
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
        
        last_node=lista.get_tail()
        last_node.set_next(list_to_merge.get_head())

        lista.tail=list_to_merge.tail
        lista.count+=list_to_merge.count

    def get_profissionais_in(self):
        return self.profissionais_in.keys() # List with all the profissionais in utente
    
    def add_profissional_in(self,nome_profissional):
        if not self.profissionais_in.has_key(nome_profissional):
            self.profissionais_in.insert(nome_profissional,None)
    
    def remove_profissional_in(self,nome_profissional):
        if self.profissionais_in.has_key(nome_profissional):
            self.profissionais_in.remove(nome_profissional)

    def get_serviços_in(self):
        return self.serviços_in.keys() # List with all the serviços in utente
    
    def add_serviços_in(self,name_serviço):
        if not self.serviços_in.has_key(name_serviço):
            self.serviços_in.insert(name_serviço,None)
    
    def remove_profissional_in(self,name_serviço):
        if self.serviços_in.has_key(name_serviço):
            self.serviços_in.remove(name_serviço)