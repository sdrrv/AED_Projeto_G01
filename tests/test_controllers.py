import unittest
from controllers.controller import Controller

class Test_Controllers(unittest.TestCase):
    def setUp(self):
        self.controller= Controller()

    def test_registar_profissionais(self):
        self.controller.registar_profissional("Medicina","Gilinho")
        self.assertTrue(self.controller.profissionais.has_key("Gilinho"))
    
    def test_registar_utente(self):
        self.controller.registar_utente("Gilinho","Idoso")
        self.assertTrue(self.controller.utentes.has_key("Gilinho"))
    
    def test_registar_familia(self):
        self.controller.registar_familia("Gil")
        self.assertTrue(self.controller.familias.has_key("Gil"))
    
    def test_associar_utente_a_familia(self):
        self.controller.registar_utente("Gilinho","Idoso")
        self.controller.registar_familia("Gil")
        self.controller.associar_utente_a_familia("Gilinho","Gil")
        familia=self.controller.familias.get("Gil")
        #self.assertTrue(familia)