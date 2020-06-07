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