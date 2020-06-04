from .tad_cuidados import Cuidados

class Cuidados(Cuidados):
    def __init__(self,servico,profissional,categoria,utente):
        self.categoria=categoria
        self.servico=servico
        self.profissional= profissional
        self.utente = utente
    
    def get_utente(self):
        return self.utente
    
    def get_categoria(self):
        return self.categoria
    
    def get_profissional(self):
        return self.profissional
    
    def get_servico(self):
        return self.servico