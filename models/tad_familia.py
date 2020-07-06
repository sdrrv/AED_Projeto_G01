from abc import ABC, abstractmethod

class Tad_Familia(ABC):

    #Returns the serviço of the cuidado
    @abstractmethod
    def get_name(self):
        pass
    
    #returns the professional in charge of the ciudado
    @abstractmethod
    def get_members(self):
        pass

    @abstractmethod
    def get_jovens(self):
        pass

    @abstractmethod
    def get adultos(self):
        pass

    @abstractmethod
    def get_idosos(self):
        pass

    #returns the categoria of the cuidado
    @abstractmethod
    def add_member(self,utente):
        pass
    #Remove a member from the familly
    @abstractmethod
    def remove_member(self, nome):
        pass

    @abstractmethod
    def get_membros_que_teem_cuidados(self):
        pass

    @abstractmethod
    def has_cuidados(self):
        pass