from models.utente import Utente
from models.profissional import Profissional
from models.familia import Familia
from models.cuidados import Cuidados
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable
from utils.sorting_algorithm import Sorting_Algorithm
import ctypes


class Controller:
    def __init__(self):
        # ------------Dicionário-Geral------------
        self.utentes = HashTable()
        self.profissionais = HashTable()
        self.familias = HashTable()

        # ----------------------------------------
        # { "Medicina":{ "Duarte" : Obj_Profissional } }
        self.categorias = HashTable()
        # { "Jovem": { "Duarte" : Obj_Utente } }
        self.faixasetarias = HashTable()
        # { "Consulta": { "Duarte" : [Obj_Cuidados] } }
        self.serviços = HashTable()
        self.tad_serviços = HashTable()
        self.tad_faixasetarias = HashTable()
        self.tad_categorias = HashTable()
        # -------------------Tads----------------------
        self.tad_categorias.insert("Medicina", 1)
        self.tad_categorias.insert("Enfermagem", 2)
        self.tad_categorias.insert("Auxiliar", 3)

        self.tad_faixasetarias.insert("Jovem", 1)
        self.tad_faixasetarias.insert("Adulto", 2)
        self.tad_faixasetarias.insert("Idoso", 3)

        self.tad_serviços.insert("Consula", 1)
        self.tad_serviços.insert("PequenaCirurgia", 2)
        self.tad_serviços.insert("Enfermagem", 3)
        # ------------------Categorias-----------------
        self.categorias.insert("Medicina", HashTable())
        self.categorias.insert("Enfermagem", HashTable())
        self.categorias.insert("Auxiliar", HashTable())
        # -------------------Faixas-Etárias-------------
        self.faixasetarias.insert("Adulto", HashTable())
        self.faixasetarias.insert("Jovem", HashTable())
        self.faixasetarias.insert("Idoso", HashTable())
        # ----------------------Serviços-----------------------------
        self.serviços.insert("Consulta", HashTable())
        self.serviços.insert("PequenaCirurgia", HashTable())
        self.serviços.insert("Enfermagem", HashTable())
        # Temos de decidir como implementar os serviços.

    # --------------------------------Checks-------------------------------------------
    # returns true if there´s a professional with that name
    def has_professional(self, nome):
        return self.profissionais.has_key(nome)

    # returns true if there´s a categorua with that name
    def has_categoria(self, categoria):
        return self.tad_categorias.has_key(categoria)

    def has_utente(self, nome):  # returns true if there´s a utente with that name
        return self.utentes.has_key(nome)

    def has_familia(self, NomeFamilia):  # returns true if there´s a familia with that name
        return self.familias.has_key(NomeFamilia)

    # returns true if there´s a Faixa Etária with that name
    def has_faixa_etaria(self, FaixaEtaria):
        return self.tad_faixasetarias.has_key(FaixaEtaria)

    def has_servico(self, servico):  # returns true if there´s a serviço with that name
        return self.tad_serviços.has_key(servico)

    # Returns true if the utente is in a familia

    def has_utente_a_familia(self, nome):
        utente = self.utentes.get(nome)
        return utente.has_familia()

    def has_profissionais(self):  # returns true if there´s at least one professional
        return self.profissionais.size() != 0

    def has_utentes(self):  # returns true if there´s at least one utente
        return self.utentes.size() != 0

    def has_familias(self):  # returns true if there´s at least one utente
        return self.familias.size() != 0

    # returns true if there´s at least one cuidado in utente
    def has_utente_any_cuidados(self, nome):
        utente = self.utentes.get(nome)
        return utente.has_cuidados()

    # returns true if there´s at least one cuidado in profissional
    def has_profissional_any_cuidados(self, nome):
        profissional = self.profissionais.get(nome)
        return profissional.has_cuidados()

    # returns true if there´s at least one cuidado in utente in the familia

    def has_familia_any_cuidados(self, NomFamilia):
        familia = self.familias.get(NomFamilia)
        return familia.has_cuidados()
    # ---------------------------------------Gets-----------------------------------------

    def get_utente(self, nome):
        return self.utentes.get(nome)

    def get_familia(self, NomeFamilia):
        return self.familias.get(NomeFamilia)

    def get_profissional(self, nome):
        return self.profissionais.get(nome)

    def get_profissionais_in_categoria(self, categoria):
        return self.categorias.get(categoria).keys()

    def get_utentes_in_faixa_etaria(self, faixa_etaria):
        return self.faixasetarias.get(faixa_etaria).keys()

    # ----------------------------------Lists-to-arrays-------------------------------------
    def list_to_array(self, SinglyList):
        size = SinglyList.size()
        it = SinglyList.iterator()
        i = 0
        result = (size * ctypes.py_object)()
        while it.has_next():
            result[i] = it.next()
            i += 1
        return result
    # ------------------------------------------------------------------------------------

    def registar_profissional(self, categoria, name):
        profissional = Profissional(name, categoria)
        self.profissionais.insert(name, profissional)
        self.categorias.get(categoria).insert(name, profissional)

    def registar_utente(self, name, FaixaEtaria):
        utente = Utente(name, FaixaEtaria)
        self.utentes.insert(name, utente)
        self.faixasetarias.get(FaixaEtaria).insert(name, utente)

    def registar_familia(self, NomeFamilia):
        self.familias.insert(NomeFamilia, Familia(NomeFamilia))

    def associar_utente_a_familia(self, nome, NomeFamilia):
        familia = self.familias.get(NomeFamilia)
        utente = self.utentes.get(nome)
        familia.add_member(utente)
        utente.set_familia(NomeFamilia)

    def desassociar_utente_a_familia(self, nome):
        utente = self.utentes.get(nome)
        familia = self.familias.get(utente.get_familia())
        utente.remove_familia()
        familia.remove_member(nome)

    def listar_profissionais(self):
        # Returns a List [["Medicina","Gilinho"]]
        result = SinglyLinkedList()
        medicina = self.list_to_array(self.categorias.get("Medicina").keys())
        enfermagem = self.list_to_array(
            self.categorias.get("Enfermagem").keys())
        auxiliar = self.list_to_array(self.categorias.get("Auxiliar").keys())
        if self.categorias.get('Medicina').keys().size() != 0:
            medicina = Sorting_Algorithm().sort(
                medicina, self.categorias.get('Medicina').keys().size())
            result.insert_last(medicina)
        if self.categorias.get('Enfermagem').keys().size() != 0:
            enfermagem = Sorting_Algorithm().sort(
                enfermagem, self.categorias.get("Enfermagem").keys().size())
            result.insert_last(enfermagem)
        if self.categorias.get('Auxiliar').keys().size() != 0:
            auxiliar = Sorting_Algorithm().sort(
                auxiliar, self.categorias.get("Auxiliar").keys().size())
            result.insert_last(auxiliar)
        return result

    def listar_utentes(self):
        # Returns a List[["Gil","Idoso","Gilinho"]]
        result = SinglyLinkedList()
        jovem = self.list_to_array(self.faixasetarias.get("Jovem").keys())
        adulto = self.list_to_array(self.faixasetarias.get("Adulto").keys())
        idoso = self.list_to_array(self.faixasetarias.get("Idoso").keys())
        if self.faixasetarias.get('Jovem').keys().size() != 0:
            jovem = Sorting_Algorithm().sort(
                jovem, self.faixasetarias.get('Jovem').keys().size())
            result.insert_last(jovem)
        if self.faixasetarias.get('Adulto').keys().size() != 0:
            adulto = Sorting_Algorithm().sort(
                adulto, self.faixasetarias.get("Adulto").keys().size())
            result.insert_last(adulto)
        if self.faixasetarias.get('Idoso').keys().size() != 0:
            idoso = Sorting_Algorithm().sort(
                idoso, self.faixasetarias.get("Idoso").keys().size())
            result.insert_last(idoso)
        return result

    def listar_familias(self):
        familias = self.list_to_array(self.familias.keys())
        Sorting_Algorithm().sort(familias, self.familias.keys().size())
        return familias

    def mostrar_familia(self, nome_familia):
        # Retuns a list [["Jovem","Galinha"],["Idoso","Gilinho"]]
        familia = self.get_familia(nome_familia)
        result = SinglyLinkedList()
        jovem = self.list_to_array(familia.get_jovens())
        adulto = self.list_to_array(familia.get_adultos())
        idoso = self.list_to_array(familia.get_idosos())
        if familia.get_jovens().size() != 0:
            jovem = Sorting_Algorithm().sort(
                jovem, familia.get_jovens().size())
            result.insert_last(jovem)
        if familia.get_adultos().size() != 0:
            adulto = Sorting_Algorithm().sort(
                adulto, familia.get_adultos().size())
            result.insert_last(adulto)
        if familia.get_idosos().size() != 0:
            idoso = Sorting_Algorithm().sort(
                idoso, familia.get_idosos().size())
            result.insert_last(idoso)
        return result

    # pega na lista do cli adiciona á aos cuidados do utente, atualiza o profissional(antes de dar add), meter na hash table do profissional com o nome do utente

    def marcar_cuidados_a_utente(self, nome, lista_de_cuidados):
        utente = self.get_utente(nome)
        lista_iterator = lista_de_cuidados.iterator()
        while lista_iterator.has_next():
            cuidado = lista_iterator.next()
            # --------------to-profissional-----------------
            profissional = self.get_profissional(cuidado.get_profissional())
            profissional.add_to_cuidados(cuidado)
            # ---------------to-serviços--------------------
            self.add_cuidados_to_serviço(cuidado)
            # ----------------to-utente---------------------
            utente.add_to_cuidados(cuidado)
            utente.add_profissional_in(cuidado.get_profissional())
            utente.add_serviços_in(cuidado.get_serviço())
            # ----------------------------------------------

    # adds a cuidado to the name of the utente in serviço
    def add_cuidados_to_serviço(self, cuidado):
        serviço = self.serviços.get(cuidado.get_serviço())
        utente = cuidado.get_utente()
        if not serviço.has_key(utente):
            serviço.insert(utente, SinglyLinkedList())
        serviço.get(utente).insert_last(cuidado)

    def remove_utente_from_serviço(self, nome, serviço):
        serviço = self.serviços.get(serviço)
        serviço.remove(nome)

    def miga(self):
        pass  # chama no final a func marcar_cuidados_a_utente
    # fazer a func, waiting list que é chamada no cli, e serve como caixote de objetos, cuidados a mandar para mcau.

    def get_object_name(self, objct):
        return objct.get_name()

    def cancelar_cuidados_marcados_a_utente(self, nome):
        utente = self.get_utente(nome)
        profissionais_in = utente.get_profissionais_in().iterator()
        serviços_in = utente.get_serviços_in().iterator()
        # -------------------profissionais------------------
        while profissionais_in.has_next():
            profissional = self.get_profissional(profissionais_in.next())
            profissional.remove_utente_from_cuidados(nome)
        # -------------------serviços-----------------------
        while serviços_in.has_next():
            self.remove_utente_from_serviço(nome, serviços_in, next())
        # --------------------------------------------------

        utente.remove_cuidados()

    def listar_cuidados_marcados_a_utente(self, nome):
        pass  # Returns a list with objects cuidados

    def listar_cuidados_marcados_a_familia(self, NomeFamilia):
        pass  # Returns a list [["Dudas","Consulta","Medicina","Gilinho"]]

    def listar_servicos_marcados_a_profissional(self, Categoria, NomeProfissional):
        pass  # returns a list [["Consulta","Dudas"]]

    def listar_servicos_marcados_a_profissional(self, categoria, nome_profissional):
        pass  # returns a list [["Consulta","Dudas"]]

    def listar_marcacoes_por_tipo_de_servico(self, servico):
        pass  # Returns a list [["Medicina","Gilinho","Dudas"]]
