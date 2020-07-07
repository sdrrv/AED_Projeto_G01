from models.checker import Checker
from models.dumper import Dumper
from models.novo_utente import Utente
from models.novo_profissional import Profissional
from models.novo_familia import Familia
from models.novo_cuidado import Cuidado
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
        self.tad_servico = HashTable()
        # ----------------------------------------
        # { "Medicina":{ "Duarte" : Obj_Profissional } }
        self.categorias = HashTable()
        # { "Jovem": { "Duarte" : Obj_Utente } }
        self.faixasetarias = HashTable()
        # { "Consulta": { "Duarte" : [Obj_Cuidados] } }
        self.servicos = HashTable()
        # ------------------Categorias-----------------
        self.categorias.insert("Medicina", HashTable())
        self.categorias.insert("Enfermagem", HashTable())
        self.categorias.insert("Auxiliar", HashTable())
        # -------------------Faixas-Etárias-------------
        self.faixasetarias.insert("Adulto", HashTable())
        self.faixasetarias.insert("Jovem", HashTable())
        self.faixasetarias.insert("Idoso", HashTable())
        # ----------------------Servicos-----------------------------
        self.servicos.insert("Consulta", HashTable())
        self.servicos.insert("PequenaCirurgia", HashTable())
        self.servicos.insert("Enfermagem", HashTable())
        # ----------------------Tad_servico--------------------------
        self.tad_servico.insert("Consulta", HashTable())
        self.tad_servico.insert("PequenaCirurgia", HashTable())
        self.tad_servico.insert("Enfermagem", HashTable())
        self.populate_tad_servico()

    # --------------------------------Checks-------------------------------------------
    # returns true if there´s a professional with that name
    def has_professional(self, nome):
        return self.profissionais.has_key(nome)

    # returns true if there´s a categorua with that name
    def has_categoria(self, categoria):
        return self.categorias.has_key(categoria)

    def has_utente(self, nome):  # returns true if there´s a utente with that name
        return self.utentes.has_key(nome)

    def has_familia(self, NomeFamilia):  # returns true if there´s a familia with that name
        return self.familias.has_key(NomeFamilia)

    # returns true if there´s a Faixa Etária with that name
    def has_faixa_etaria(self, FaixaEtaria):
        return self.faixasetarias.has_key(FaixaEtaria)

    def has_servico(self, servico):  # returns true if there´s a servico with that name
        return self.servicos.has_key(servico)

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
    def servico_has_categoria(self, servico, categoria):
        return self.tad_servico.get(servico).has_key(categoria)

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

    def populate_tad_servico(self):
        self.tad_servico.get("Consulta").insert("Medicina", 1)
        self.tad_servico.get("PequenaCirurgia").insert("Medicina", 1)
        self.tad_servico.get("PequenaCirurgia").insert("Enfermagem", 2)
        self.tad_servico.get("PequenaCirurgia").insert("Auxiliar", 3)
        self.tad_servico.get("Enfermagem").insert("Enfermagem", 1)
        self.tad_servico.get("Enfermagem").insert("Auxiliar", 2)

    # ------------------------------------------------------------------------------------

    def registar_profissional(self, categoria, name):
        profissional = Profissional(name, categoria)
        self.profissionais.insert(name, profissional)
        self.categorias.get(categoria).insert(name, profissional)

    def registar_utente(self, name, FaixaEtaria):
        utente = Utente(name, FaixaEtaria)
        self.utentes.insert(name, utente)
        self.faixasetarias.get(FaixaEtaria).insert(name, utente)

    def registar_familia(self, nome_familia):
        self.familias.insert(nome_familia, Familia(nome_familia))

    def associar_utente_a_familia(self, nome, nome_familia):
        familia = self.familias.get(nome_familia)
        utente = self.utentes.get(nome)
        familia.add_member(utente)
        utente.set_familia(nome_familia)

    def desassociar_utente_a_familia(self, nome):
        utente = self.utentes.get(nome)
        familia = self.familias.get(utente.get_familia())
        utente.set_familia(None)
        familia.remove_member(utente)

    def create_checker(self):
        return Checker()

    def create_dump(self):
        return SinglyLinkedList()

    def create_cuidado(self, utente, servico, categoria, profissional):
        return Cuidado(utente, servico, categoria, profissional)

    def listar_profissionais(self):
        # Returns a List [["Medicina","Gilinho"]]
        pass

    def listar_utentes(self):
        pass

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
        return True
        #utente = self.get_utente(nome)
        #lista_iterator = lista_de_cuidados.iterator()
        # while lista_iterator.has_next():
        #    cuidado = lista_iterator.next()
        #    # --------------to-profissional-----------------
        #    profissional = self.get_profissional(cuidado.get_profissional())
        #    profissional.add_to_cuidados(cuidado)
        #    # ---------------to-servicos--------------------
        #    self.add_cuidados_to_servico(cuidado)
        #    # ----------------to-utente---------------------
        #    utente.add_to_cuidados(cuidado)
        #    utente.add_profissional_in(cuidado.get_profissional())
        #    utente.add_servicos_in(cuidado.get_servico())
        #    # ----------------------------------------------

    # ad#ds a cuidado to the name of the utente in servico
    def add_cuidados_to_servico(self, cuidado):
        servico = self.servicos.get(cuidado.get_servico())
        utente = cuidado.get_utente()
        if not servico.has_key(utente):
            servico.insert(utente, SinglyLinkedList())
        servico.get(utente).insert_last(cuidado)

    def remove_utente_from_servico(self, nome, servico):
        servico = self.servicos.get(servico)
        servico.remove(nome)

    def miga(self):
        pass  # chama no final a func marcar_cuidados_a_utente
    # fazer a func, waiting list que é chamada no cli, e serve como caixote de objetos, cuidados a mandar para mcau.

    def get_object_name(self, objct):
        return objct.get_name()

    def cancelar_cuidados_marcados_a_utente(self, nome):
        utente = self.get_utente(nome)
        profissionais_in = utente.get_profissionais_in().iterator()
        servicos_in = utente.get_servicos_in().iterator()
        # -------------------profissionais------------------
        while profissionais_in.has_next():
            profissional = self.get_profissional(profissionais_in.next())
            profissional.remove_utente_from_cuidados(nome)
        # -------------------servicos-----------------------
        while servicos_in.has_next():
            self.remove_utente_from_servico(nome, servicos_in, next())
        # --------------------------------------------------

        utente.remove_cuidados()

    def listar_cuidados_marcados_a_utente(self, nome):
        utente = self.controller.get_utente(nome)
        return utente.get_cuidados()
        pass  # Returns a list with objects cuidados

    def listar_cuidados_marcados_a_familia(self, NomeFamilia):
        pass  # Returns a list [["Dudas","Consulta","Medicina","Gilinho"]]

    def listar_servicos_marcados_a_profissional(self, Categoria, NomeProfissional):
        pass  # returns a list [["Consulta","Dudas"]]

    def listar_servicos_marcados_a_profissional(self, categoria, nome_profissional):
        pass  # returns a list [["Consulta","Dudas"]]

    def listar_marcacoes_por_tipo_de_servico(self, servico):
        pass  # Returns a list [["Medicina","Gilinho","Dudas"]]

    def is_valid_sequence(self, sequence):
        arr = self.list_to_array(sequence)
        for i in arr:
        clear = 0
        index = 0
        for categoria in arr:
            if categoria == "PequenaCirurgia":
                if self.check_for_consulta_in_range(arr, 0, index):
                    clear += 1
                    if self.check_for_consulta_in_range(arr, index, sequence.size()):
                        clear -= 1
                else:
                    return False
            index += 1
        return clear == 0

    def check_for_consulta_in_range(self, arr, lower, upper):
        for i in range(lower, upper):
            if arr[i] == "Consulta":
                return True
        return False

    def give_checker_error(self, checker):
        if checker.get('Servico') == True:
            return "Serviço inexistente."
        elif checker.get('Categoria') == True:
            return "Categoria inexistente."
        elif checker.get('Profissional') == True:
            return "Profissional de saúde inexistente."
        elif checker.get('CInvalida') == True:
            return "Categoria inválida."
        else:
            return "Sequência inválida."

    # def categorias_to_array(self):
    #    table = (3*ctypes.py_object)()
    #    categorias = self.tad_categorias.keys()
    #    table[0] = self.tad_categorias.
    #    table[1] = categorias.get(1)
    #    table[2] = categorias.get(2)
    #    return table

    # def etarias_to_array(self):
    #    table = (3*ctypes.py_object)()
    #    etarias = self.tad_faixasetarias.keys()
    #    table[0] = etarias.get(0)
    #    table[1] = etarias.get(1)
    #    table[2] = etarias.get(2)
    #    return table
