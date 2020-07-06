from .pessoa import Pessoa
from .tad_utente import Tad_Utente
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.hash_table import HashTable


class Utente(Pessoa, Tad_Utente):
    def __init__(self, nome, Faixa_Etaria):
        Pessoa.__init__(self, nome)
        self.faixa_etaria = Faixa_Etaria
        self.lista_de_cuidados = SinglyLinkedList()
        self.familia = None  # Sting nome familia
        self.profissionais_in = HashTable()
        self.serviços_in = HashTable()

    def get_faixa_etaria(self):
        return self.faixa_etaria

    def get_cuidados(self):
        return self.lista_de_cuidados

    def add_to_cuidados(self, cuidado):
        self.lista_de_cuidados.insert_last(cuidado)

    def remove_cuidados(self):
        self.lista_de_cuidados.make_empty()
        self.remove_profissional_in()
        self.remove_serviços_in()

    def get_familia(self):
        return self.familia

    def remove_familia(self):
        self.familia = None

    def set_familia(self, NomeFamila):
        self.familia = NomeFamila

    def has_familia(self):  # Returns true if the utente is in a familia
        if self.get_familia():
            return True
        return False

    def has_cuidados(self):
        return self.get_cuidados().is_empty()

    def add_to_cuidados(self, cuidado):
        self.get_cuidados.insert_last(cuidado)

    def get_profissionais_in(self):
        return self.profissionais_in.keys()  # List with all the profissionais in utente

    def add_profissional_in(self, nome_profissional):
        if not self.profissionais_in.has_key(nome_profissional):
            self.profissionais_in.insert(nome_profissional, None)

    def remove_profissional_in(self):
        profissionais_in = self.profissionais_in.keys().iterator()
        while profissionais_in.has_next():
            self.profissionais_in.remove(profissionais_in.next())

    def get_servicos_in(self):
        return self.serviços_in.keys()  # List with all the serviços in utente

    def add_servicos_in(self, name_serviço):
        if not self.serviços_in.has_key(name_serviço):
            self.serviços_in.insert(name_serviço, None)

    def remove_serviços_in(self):
        serviços_in = self.serviços_in.keys().iterator()
        while serviços_in.has_next():
            self.serviços_in.remove(serviços_in.next())

