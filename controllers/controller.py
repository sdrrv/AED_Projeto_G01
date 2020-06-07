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
    
    def registar_profissional(self,categoria,name):
        self.profissionais.insert(name, Profissional(name,categoria))
    
    def registar_utente(self,name,FaixaEtaria):
        self.utentes.insert(name, Utente(name, FaixaEtaria))


    def registar_familia(self,NomeFamilia):
<<<<<<< HEAD
        pass
    
    def associar_utente_a_familia(self,nome,NomeFamilia):
        pass
=======
        self.familias.insert(NomeFamilia, Familia(NomeFamilia))
>>>>>>> master
