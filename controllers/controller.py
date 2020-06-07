from models.utente import Utente
from models.profissional import Profissional
from models.familia import Familia
from models.cuidados import Cuidados
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable

class Controller:
    def __init__(self):
        self.utentes = HashTable()
        self.profissionais = HashTable()
        self.familias = HashTable()
        #----------------------------------------
        self.categorias = HashTable()
        self.FaixasEtarias = HashTable()
        #----------------------------------------
    
    def registar_profissional(self,categoria,nome):
        self.profissionais.insert(nome, Profissional(nome,categoria))
    
    def registar_utente(self,nome,FaixaEtaria):
        pass

    def registar_familia(self,NomeFamilia):
        pass
