import unittest
from controllers.controller import Controller


# Utentes utilizados Nos testes: 
# -Gilinho Idoso da familia Gil
# -Miguelinho Adulto da familia Rosario
# -Galinha Jovem da familia Gil
# -Dudas Idoso da familia Elvas


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
    
    def test_listar_utentes(self):
        #[ ["Elvas","Idoso","Dudas"],["Gil","Jovem","Galinha"],["Gil","Idoso","Gilinho"],["","Adulto","Miguelinho"] ]
        #---------------------Registar-e-associar-utentes-as-familias------------------------
        self.controller.registar_utente("Gilinho","Idoso")
        self.controller.registar_utente("Galinha","Jovem")
        self.controller.registar_familia("Gil")
        self.controller.associar_utente_a_familia("Gilinho","Gil")
        self.controller.associar_utente_a_familia("Galinha","Gil")
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_familia("Elvas")
        self.controller.associar_utente_a_familia("Dudas","Elvas")
        self.controller.registar_utente("Miguelinho","Adulto")
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(self.controller.listar_utentes().get(0).get(0),"Elvas")
        self.assertEqual(self.controller.listar_utentes().get(0).get(1),"Idoso")
        self.assertEqual(self.controller.listar_utentes().get(0).get(2),"Dudas")
        #--------------------------------------Galinha------------------------------------------
        self.assertEqual(self.controller.listar_utentes().get(1).get(0),"Gil")
        self.assertEqual(self.controller.listar_utentes().get(1).get(1),"Jovem")
        self.assertEqual(self.controller.listar_utentes().get(1).get(2),"Galinha")
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(self.controller.listar_utentes().get(2).get(0),"Gil")
        self.assertEqual(self.controller.listar_utentes().get(2).get(1),"Idoso")
        self.assertEqual(self.controller.listar_utentes().get(2).get(2),"Gilinho")
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(self.controller.listar_utentes().get(3).get(0),"")
        self.assertEqual(self.controller.listar_utentes().get(3).get(1),"Adulto")
        self.assertEqual(self.controller.listar_utentes().get(3).get(2),"Miguelinho")
        #-------------------------------------------------------------------------------------
        

