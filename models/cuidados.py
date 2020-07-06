from .tad_cuidados import Tad_Cuidados

class Cuidados(Tad_Cuidados):
    def __init__(self,serviço,profissional,categoria,utente):
        self.categoria=categoria
        self.serviço=serviço
        self.profissional= profissional
        self.utente = utente
    
    def get_utente(self):
        return self.utente
    
    def get_categoria(self):
        return self.categoria
    
    def get_profissional(self):
        return self.profissional
    
    def get_serviço(self):
        return self.serviço