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
        self.assertTrue(self.controller.familias.get("Gil").get_members().has_key("Gilinho"))

    def test_desassociar_utente_a_familia(self):
        self.controller.registar_utente("Gilinho","Idoso")
        self.controller.registar_familia("Gil")
        self.controller.associar_utente_a_familia("Gilinho","Gil")
        self.controller.desassociar_utente_a_familia("Gilinho")
        self.assertFalse(self.controller.familias.get("Gil").get_members().has_key("Gilinho"))
    
    def test_listar_profissionais(self):
        self.controller.registar_profissional("Medicina","Gilinho")
        self.controller.registar_profissional("Auxiliar", "Galinha")
        self.controller.registar_profissional("Medicina","Miguelinho")
        #-------------------------------------------Gilinho----------------------------------------------
        self.assertEqual(self.controller.listar_profissionais().get(0).get_first(),"Medicina")
        self.assertEqual(self.controller.listar_profissionais().get(0).get_last(),"Gilinho")
         #-------------------------------------------Miguelinho----------------------------------------------
        self.assertEqual(self.controller.listar_profissionais().get(1).get_first(),"Medicina")
        self.assertEqual(self.controller.listar_profissionais().get(1).get_last(),"Miguelinho")
        #-------------------------------------------Galinha----------------------------------------------
        self.assertEqual(self.controller.listar_profissionais().get(2).get_first(),"Auxiliar")
        self.assertEqual(self.controller.listar_profissionais().get(2).get_last(),"Galinha")