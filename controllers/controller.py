from models.utente import Utente
from models.profissional import Profissional
from models.familia import Familia
from models.cuidados import Cuidados
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable


class Controller:
    def __init__(self):
        #------------Dicionário-Geral------------
        self.utentes = HashTable()
        self.profissionais = HashTable()
        self.familias = HashTable()
        #----------------------------------------
        self.categorias = HashTable()
        self.faixasetarias = HashTable()
        #------------------categorias-----------------
        self.categorias.insert("Medicina",HashTable())
        self.categorias.insert("Enfermagem",HashTable())
        self.categorias.insert("Auxiliar",HashTable())
        #-------------------Faixas-Etárias-------------
        self.faixasetarias.insert("Medicina",SinglyLinkedList())
        self.faixasetarias.insert("Enfermagem",SinglyLinkedList())
        self.faixasetarias.insert("Auxiliar",SinglyLinkedList())
        #----------------------------------------------

    def registar_profissional(self,categoria,name):
        self.profissionais.insert(name, Profissional(name,categoria))
    
    def registar_utente(self,name,FaixaEtaria):
        self.utentes.insert(name, Utente(name, FaixaEtaria))

    def registar_familia(self,NomeFamilia):
        self.familias.insert(NomeFamilia, Familia(NomeFamilia))
    
<<<<<<< HEAD
    def associar_utente_a_familia(self,name,NomeFamilia):
        pass
=======
    def associar_utente_a_familia(self,nome,NomeFamilia):
        familia = self.familias.get(NomeFamilia)
        familia.add_member(self.utentes.get(nome))
        

    def desassociar_utente_a_familia(self,nome):
        pass

    def listar_profissionais(self):
        pass #Returns a List [["Medicina","Gilinho"]]

    def listar_utentes(self):
        pass #Returns a List[["Gil","Idoso","Gilinho"]]

    def listar_familias(self):
        pass #Returns a list ["Gil","Rosario"]
    
    def mostrar_familia(self,NomeFamilia):
        pass #Retuns a list [["Jovem","Galinha"],["Idoso","Gilinho"]]

    def marcar_cuidados_a_utente(self,nome,servico,categoria,NomeProfissional):
        pass
    
    def cancelar_cuidados_marcados_a_utente(self,nome):
        pass

    def listar_cuidados_marcados_a_utente(self,nome):
        pass #Returns a list with objects cuidados

    def listar_cuidados_marcados_a_familia(self,NomeFamilia):
        pass # Returns a list [["Dudas","Consulta","Medicina","Gilinho"]]

    def listar_servicos_marcados_a_profissional(self,Categoria,NomeProfissional):
        pass # returns a list [["Consulta","Dudas"]]

    def listar_marcações_por_tipo_de_servico(self,servico):
        pass #Returns a list [["Medicina","Gilinho","Dudas"]]
>>>>>>> master
