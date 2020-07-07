from controllers.controller import Controller
from utils.cheapcheat import Cheats
from models.dumper import Dumper


class CLI():
    def __init__(self):
        self.controller = Controller()

        while True:
            line = input()
            if line == "":
                exit()
            commands = line.split()
###########################################################################################
            # Resgistar Profissional
            if (commands[0] == "RP"):
                if self.controller.has_professional(commands[2]):
                    print("Profissional existente.")
                elif not self.controller.has_categoria(commands[1]):
                    print("Categoria inexistente.")

                else:
                    self.controller.registar_profissional(
                        commands[1], commands[2])
                    print("Profissional registado com sucesso.")
###########################################################################################
            elif (commands[0] == "RU"):
                if self.controller.has_utente(commands[1]):
                    print("Utente existente.")

                elif not self.controller.has_faixa_etaria(commands[2]):
                    print("Faixa etária inexistente.")

                else:
                    self.controller.registar_utente(commands[1], commands[2])
                    print("Utente registado com sucesso.")
###########################################################################################
            elif(commands[0] == "RF"):
                if self.controller.has_familia(commands[1]):
                    print("Família existente.")
                else:
                    self.controller.registar_familia(commands[1])
                    print("Família registada com sucesso.")

###########################################################################################
            elif(commands[0] == "AF"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")
                elif not self.controller.has_familia(commands[2]):
                    print("Família inexistente.")
                elif self.controller.has_utente_a_familia(command[1]):
                    print("Utente pertence a família.")
                else:
                    self.controller.associar_utente_a_familia(
                        commands[1], commands[2])
                    print("Utente associado a família.")

###########################################################################################
            elif(commands[0] == "DF"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")
                elif not self.controller.has_utente_a_familia(commands[1]):
                    print("Utente não pertence a família.")
                else:
                    self.controller.desassociar_utente_a_familia(commands[1])
                    print("Utente desassociado de família.")
###########################################################################################
            elif (commands[0] == "LP"):
                if not self.controller.has_profissionais():
                    print("Sem profissionais registados.")
                else:
                    self.controller.listar_profissionais()
