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
        #------------------------------------------------------------------------------------
        listar = self.controller.listar_profissionais()
        #-------------------------------------------Gilinho----------------------------------------------
        self.assertEqual(listar.get(0).get_first(),"Medicina")
        self.assertEqual(listar.get(0).get_last(),"Gilinho")
         #-------------------------------------------Miguelinho----------------------------------------------
        self.assertEqual(listar.get(1).get_first(),"Medicina")
        self.assertEqual(listar.get(1).get_last(),"Miguelinho")
        #-------------------------------------------Galinha----------------------------------------------
        self.assertEqual(listar.get(2).get_first(),"Auxiliar")
        self.assertEqual(listar.get(2).get_last(),"Galinha")
    
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
        #------------------------------------------------------------------------------------
        listar = self.controller.listar_utentes()
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(listar.get(0).get(0),"Elvas")
        self.assertEqual(listar.get(0).get(1),"Idoso")
        self.assertEqual(listar.get(0).get(2),"Dudas")
        #--------------------------------------Galinha------------------------------------------
        self.assertEqual(listar.get(1).get(0),"Gil")
        self.assertEqual(listar.get(1).get(1),"Jovem")
        self.assertEqual(listar.get(1).get(2),"Galinha")
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(listar.get(2).get(0),"Gil")
        self.assertEqual(listar.get(2).get(1),"Idoso")
        self.assertEqual(listar.get(2).get(2),"Gilinho")
        #--------------------------------------Dudas------------------------------------------
        self.assertEqual(listar.get(3).get(0),"")
        self.assertEqual(listar.get(3).get(1),"Adulto")
        self.assertEqual(listar.get(3).get(2),"Miguelinho")
        #-------------------------------------------------------------------------------------
    
    def test_listar_familias(self):
        #["Gil","Rosario"]
        self.controller.registar_familia("Gil")
        self.controller.registar_familia("Rosario")
        #--------------------------------------------------------------------------------------
        listar= self.controller.listar_familias()
        #--------------------------------------------------------------------------------------
        self.assertEqual(listar.get(0),"Gil")
        #--------------------------------------------------------------------------------------
        self.assertEqual(listar.get(1),"Rosario")
    
    def test_mostrar_familia(self):
        #[["Jovem","Galinha"],["Adulto","Miguelinho"]["Idoso","Gilinho"]]
        self.controller.registar_familia("Gil")
        self.controller.registar_utente("Gilinho","Idoso")
        self.controller.associar_utente_a_familia("Gilinho","Gil")
        self.controller.registar_utente("Galinha","Jovem")
        self.controller.associar_utente_a_familia("Galinha","Gil")
        self.controller.registar_utente("Miguelinho","Adulto")
        self.controller.associar_utente_a_familia("Galinha","Gil")
        #-------------------------------------------------------------------------
        listar = self.controller.mostrar_familia("Gil")
        #----------------------------Galinha---------------------------------------
        self.assertEqual(listar.get(0).get_first(),"Jovem")
        self.assertEqual(listar.get(0).get_last(),"Galinha")
        #----------------------------Miguelinho---------------------------------------
        self.assertEqual(listar.get(1).get_first(),"Adulto")
        self.assertEqual(listar.get(1).get_last(),"Miguelinho")
        #----------------------------Gilinho---------------------------------------
        self.assertEqual(listar.get(2).get_first(),"Idoso")
        self.assertEqual(listar.get(2).get_last(),"Gilinho")
        #---------------------------------------------------------------------------
    
    def marcar_cuidados(self,nome,serviço,categoria,NomeProfissional):
        pass

    def test_marcar_cuidados_a_utente(self):
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_profissional("Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.assertEqual(self.controller.utentes.get("Dudas").get_cuidados().get_first().get_servico(),"Consulta")
    
    def test_cancelar_cuidados_marcados_a_utente(self):
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_profissional("Medicina","Gilinho")
        self.controller.registar_profissional("Medicina","Valéria")
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.controller.cancelar_cuidados_marcados_a_utente("Dudas")
        self.assertTrue(self.controller.utentes.get("Dudas").get_cuidados().is_empty())
    
    def test_listar_cuidados_marcados_a_utente(self):
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_profissional("Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.controller.cancelar_cuidados_marcados_a_utente("Dudas")
        self.assertEqual(self.controller.listar_cuidados_marcados_a_utente("Dudas").get_first().get_servico(),"Consulta")

    def test_listar_cuidados_marcados_a_familia(self):
        #[["Galinha","Consulta","Medicina","Gilinho"],["Dudas,"Consulta,"Medicina","Gilinho"]]
        self.controller.registar_familia("Gil")
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_utente("Galinha","Jovem")
        self.controller.associar_utente_a_familia("Galinha","Gil")
        self.controller.associar_utente_a_familia("Dudas","Gil")
        self.controller.registar_profissional("Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Galinha","Consulta","Medicina","Gilinho")
        listar=self.controller.listar_cuidados_marcados_a_familia("Gil")
        #------------------------------------Galinha-----------------------------------------
        self.assertEqual(listar.get(0).get_first(),"Galinha")
        #------------------------------------Dudas-------------------------------------------
        self.assertEqual(listar.get(1).get_first(),"Dudas")
        #-------------------------------------------------------------------------------------
    
    def test_listar_servicos_marcados_a_profissional(self):
        #[["Consulta","Dudas"],["Consulta","Galinha"]]
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_utente("Galinha","Jovem")
        self.controller.registar_profissional("Medicina","Gilinho")
        #-------------------------------------------------------------------------------------
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Galinha","Consulta","Medicina","Gilinho")
        #-------------------------------------------------------------------------------------
        listar=self.controller.listar_servicos_marcados_a_profissional("Medicina","Gilinho")
        #-----------------------------------------Dudas-----------------------------------------
        self.assertEqual(listar.get(0).get_last(),"Dudas")
        #-----------------------------------------Galinha---------------------------------------
        self.assertEqual(listar.get(1).get_last(),"Galinha")
        #---------------------------------------------------------------------------------------
    
    def test_listar_marcações_por_tipo_de_servico(self):
        #[["Medicina","Gilinho","Dudas"],["Medicina","Gilinho","Galinha"]]
        self.controller.registar_utente("Dudas","Idoso")
        self.controller.registar_utente("Galinha","Jovem")
        self.controller.registar_profissional("Medicina","Gilinho")
        #-------------------------------------------------------------------------------------
        self.controller.marcar_cuidados_a_utente("Dudas","Consulta","Medicina","Gilinho")
        self.controller.marcar_cuidados_a_utente("Galinha","Consulta","Medicina","Gilinho")
        #-------------------------------------------------------------------------------------
        listar=self.controller.listar_marcações_por_tipo_de_servico("Consulta")
        #-----------------------------------------Dudas-----------------------------------------
        self.assertEqual(listar.get(0).get_last(),"Dudas")
        #-----------------------------------------Galinha---------------------------------------
        self.assertEqual(listar.get(1).get_last(),"Galinha")
        #---------------------------------------------------------------------------------------

