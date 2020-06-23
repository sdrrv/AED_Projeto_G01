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
        self.serviços = HashTable()
        #------------------categorias-----------------
        self.categorias.insert("Medicina",HashTable())
        self.categorias.insert("Enfermagem",HashTable())
        self.categorias.insert("Auxiliar",HashTable())
        #-------------------Faixas-Etárias-------------
        self.faixasetarias.insert("Medicina",SinglyLinkedList())
        self.faixasetarias.insert("Enfermagem",SinglyLinkedList())
        self.faixasetarias.insert("Auxiliar",SinglyLinkedList())
        #----------------------Serviços-----------------------------
        #Temos de decidir como implementar os serviços.

    #--------------------------------Checks-------------------------------------------
    def has_professional(self,nome): #returns true if there´s a professional with that name
        return self.profissionais.has_key(nome)

    def has_categoria(self,categoria): #returns true if there´s a categorua with that name
        return self.categorias.has_key(categoria)

    def has_utente(self,nome): #returns true if there´s a utente with that name
        return self.utentes.has_key(nome)

    def has_familia(self,NomeFamilia): #returns true if there´s a familia with that name
        return self.familias.has_key(NomeFamilia)
    
    def has_faixa_etaria(self,FaixaEtaria):#returns true if there´s a Faixa Etária with that name
        return self.faixasetarias.has_key(FaixaEtaria)
    
    def has_serviço(self,servico): #returns true if there´s a serviço with that name
        return self.serviços.has_key(servico)
    
    def has_utente_a_familia(self,nome): #Returns true if the utente is in a familia
        utente= self.utentes.get(nome)
        return utente.has_familia()
    
    def has_profissionais(self): # returns true if there´s at least one professional
        return self.profissionais.size() != 0
    
    def has_utentes(self): # returns true if there´s at least one utente
        return self.utentes.size() != 0
    
    def has_familias(self): # returns true if there´s at least one utente
        return self.familias.size() != 0

    def has_utente_any_cuidados(self,nome): #returns true if there´s at least one cuidado in utente
        utente= self.utentes.get(nome)
        return utente.has_cuidados()
    
    def has_profissional_any_cuidados(self,nome): #returns true if there´s at least one cuidado in profissional
        profissional= self.profissionais.get(nome)
        return profissional.has_cuidados()
    
    def has_familia_any_cuidados(self,NomFamilia):#returns true if there´s at least one cuidado in utente in the familia
        familia= self.familias.get(NomFamilia)
        return familia.has_cuidados()

    #---------------------------------------------------------------------------------
    def registar_profissional(self,categoria,name):
        self.profissionais.insert(name, Profissional(name,categoria))
    
    def registar_utente(self,name,FaixaEtaria):
        self.utentes.insert(name, Utente(name, FaixaEtaria))

    def registar_familia(self,NomeFamilia):
        self.familias.insert(NomeFamilia, Familia(NomeFamilia))
    
    def associar_utente_a_familia(self,nome,NomeFamilia):
        familia = self.familias.get(NomeFamilia)
        Utente=self.utentes.get(nome)
        familia.add_member(Utente)
        Utente.set_familia(NomeFamilia)
        
    def desassociar_utente_a_familia(self,nome):
        utente = self.utentes.get(nome)
        familia = self.familias.get(utente.get_familia())
        utente.remove_familia()
        familia.remove_member(nome)   

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