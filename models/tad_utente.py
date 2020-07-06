from abc import ABC, abstractmethod

class Tad_Utente(ABC):
    #Returns the faixa etaria of the utente
    @abstractmethod
    def get_faixa_etaria(self):
        pass
    
    #Returns the fila of Medical appointments of the Utente
    @abstractmethod
    def get_cuidados(self):
        pass

    #Adds a Medical appointment to the Utente.
    @abstractmethod
    def add_to_cuidados(self, cuidado):
        pass

    #Removes all Medical appointments of the Utente
    @abstractmethod
    def remove_cuidados(self, cuidados):
        pass

    @abstractmethod
    def get_familia(self):
        pass
    
    @abstractmethod
    def remove_familia(self):
        pass

    @abstractmethod
    def set_familia(self, nome_familia):
        pass

    @abstractmethod
    def has_familia(self):
        pass

    @abstractmethod
    def has_cuidados(self):
        pass

    @abstractmethod
    def add_to_cuidados(self, cuidado):
        pass

    @abstractmethod
    def get_profissionais_in(self):
        pass

    @abstractmethod
    def add_profissional_in(self, nome_profissional):
        pass

    @abstractmethod
    def remove_profissional_in(self):
        pass

    @abstractmethod
    def get_servicos_in(self, name_servico):
        pass

    @abstractmethod
    def add_servicos_in(self, name_servico):
        pass

    @abstractmethod
    def remove_servicos_in(self):
        pass

