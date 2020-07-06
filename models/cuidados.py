from .tad_cuidados import Tad_Cuidados


class Cuidados(Tad_Cuidados):
    def __init__(self, serviço, profissional, categoria, utente):
        self.categoria = categoria
        self.servico = servico
        self.profissional = profissional
        self.utente = utente

    def get_utente(self):
        return self.utente

    def get_categoria(self):
        return self.categoria

    def get_profissional(self):
        return self.profissional

    def get_servico(self):
        return self.serviço

