from .tad_cuidados import Tad_Cuidados

class Cuidados(Tad_Cuidados):
    def __init__(self,serviço,profissional,categoria,utente):
        self.serviço=serviço
        self.profissional= profissional
        self.utente = utente
    
    def get_utente(self):
        return self.utente
    
    
    def get_profissional(self):
        return self.profissional
    
    def get_serviço(self):
        return self.serviço

class Consulta(Cuidados):
    def __init__(self,profissional, categoria, utente):
        Cuidados.__init__("Consulta", profissional, categoria, utente)

class PequenaCirugia(Cuidados):
    def __init__(self,profissional_1,profissional_2,profissional_3,categoria, utente):
        Cuidados.__init__("PequenaCirugia", profissional_1, categoria, utente)
        self.profissional_2= profissional_2
        self.profissional_3= profissional_3
    
    def get_profissional_2(self):
        return self.profissional_2
    
    def get_profissional_3(self):
        return self.profissional_3

class Enfermagem(Cuidados):
    def __init__(self, serviço, profissional_1,profissional_2, categoria, utente):
        Cuidados.__init__("Enfermagem", profissional_1, categoria, utente)
        self.profissional_2=profissional_2
        
    def get_profissional_2(self):
        return self.profissional_2