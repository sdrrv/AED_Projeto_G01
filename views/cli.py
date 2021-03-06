from controllers.controller import Controller
from utils.cheapcheat import Cheats


class CLI:
    def __init__(self):
        self.controller = Controller()

        while True:
            line = input()
            if line == "":
                exit()
            commands = line.split()

            # Resgistar Profissional-----------------------"RP Categoria Nome"
            if (commands[0] == "RP"):
                if self.controller.has_professional(commands[2]):
                    print("Profissional existente.")

                elif not self.controller.has_categoria(commands[1]):
                    print("Categoria inexistente.")

                else:
                    self.controller.registar_profissional(
                        commands[1], commands[2])
                    print("Profissional registado com sucesso.")

            # Resgistar Utente------------------------------"RU Nome FaixaEtária"
            elif (commands[0] == "RU"):

                if self.controller.has_utente(commands[1]):
                    print("Utente existente.")

                elif not self.controller.has_faixa_etaria(commands[2]):
                    print("Faixa etária inexistente.")

                else:
                    self.controller.registar_utente(commands[1], commands[2])
                    print("Utente registado com sucesso.")

            # Resgistar Familia-----------------------------"RF NomeFamilia"
            elif(commands[0] == "RF"):

                if self.controller.has_familia(commands[1]):
                    print("Família existente.")
                else:
                    self.controller.registar_familia(commands[1])
                    print("Família registada com sucesso.")

            # Associar utente a familia---------------------"AF Nome NomeFamiia"
            elif(commands[0] == "AF"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")

                elif not self.controller.has_familia(commands[2]):
                    print("Família inexistente.")

                elif self.controller.get_utente(commands[1]).get_familia() != None:
                    print("Utente pertence a família.")
                else:
                    self.controller.associar_utente_a_familia(
                        commands[1], commands[2])
                    print("Utente associado a família.")

            # Desassociar utende de familia------------------"DF Nome"
            elif(commands[0] == "DF"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")

                elif not self.controller.get_utente(commands[1]).has_familia():
                    print("Utente não pertence a família.")

                else:
                    self.controller.desassociar_utente_a_familia(commands[1])
                    print("Utente desassociado de família.")

            # Listar Profissionais---------------------------"LP"
            elif(commands[0] == "LP"):
                if not self.controller.has_profissionais():
                    print("Sem profissionais registados.")
                else:
                    profissionais = self.controller.listar_profissionais()
                    categoria = Cheats().categoria()
                    #categoria = self.controller.categorias_to_array()
                    for i in range(3):
                        for name in profissionais.get(i):
                            print(f"{categoria[i]} {name}.")

            # Listar Utentes---------------------------------"LU"
            elif(commands[0] == "LU"):
                if not self.controller.has_utentes():
                    print("Sem utentes registados.")
                else:
                    utentes = self.controller.listar_utentes()
                    etaria = Cheats().faixas()
                    for i in range(3):
                        for name in utentes.get(i):
                            print(f"{etaria[i]} {name}.")

            # Listar Familias--------------------------------"LF"
            elif(commands[0] == "LF"):
                if not self.controller.has_familias():
                    print("Sem famílias registadas.")
                else:
                    familias = self.controller.listar_familias()
                    for name in familias:
                        print(f'{name}.')

            # Mostrar Familia--------------------------------"MF NomeFamila"
            elif(commands[0] == "MF"):
                if not self.controller.has_familia(commands[1]):
                    print("Família inexistente.")
                else:
                    familia = self.controller.mostrar_familia(commands[1])
                    etaria = Cheats().faixas()
                    for i in range(3):
                        for name in familia.get(0):
                            print(f"{etaria[i]} {name}.")

            # Marcar ciudados a utente-----------------------"MC Nome // Serviço // Categoria Nome Profissional"
            elif(commands[0] == "MC"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")
                else:
                    nome = commands[1]
                    dump = self.controller.create_dump()
                    sequence = self.controller.create_dump()
                    while True:
                        checker = self.controller.create_checker()
                        subline = input()
                        if subline == "":
                            break
                        inp = subline.split()
                        if len(inp) == 1:
                            servico = inp[0]
                            if not self.controller.has_servico(inp[0]):
                                checker.change_servico()
                            else:
                                sequence.insert_last(servico)
                        elif len(inp) == 2:
                            if not self.controller.has_categoria(inp[0]):
                                checker.change_categoria()
                            elif not self.controller.has_professional(inp[1]):
                                checker.change_profissional()
                            else:
                                categoria = inp[0]
                                profissional = inp[1]
                                if not self.controller.servico_has_categoria(servico, categoria):
                                    checker.change_cinvalida()
                                else:
                                    cuidado = self.controller.create_cuidado(
                                        nome, servico, categoria, profissional)
                                    dump.insert_last(cuidado)

                    if not self.controller.is_valid_sequence(sequence):
                        checker.change_sinvalida()
                    if checker.checks_out():
                        self.controller.marcar_cuidados_a_utente(nome, dump)
                        print("Cuidados marcados com sucesso.")
                    else:
                        print(self.controller.give_checker_error(checker))

            # Cancelar cuidados a utente---------------------"CC Nome"
            elif(commands[0] == "CC"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")
                elif not self.controller.has_utente_any_cuidados(commands[1]):
                    print("Utente sem cuidados de saúde marcados.")
                else:
                    self.controller.cancelar_cuidados_marcados_a_utente(
                        commands[1])
                    print("Cuidados de saúde desmarcados com sucesso.")

            # Listar cuidados marcados a utente -------------"LCU Nome"
            elif(commands[0] == "LCU"):
                if not self.controller.has_utente(commands[1]):
                    print("Utente inexistente.")
                elif not self.controller.has_utente_any_cuidados(commands[1]):
                    print("Utente sem cuidados de saúde marcados.")
                else:

                    pass

            # Listar cuidados marcados a Familia -------------"LCF NomeFamilia"
            elif(commands[0] == "LCF"):
                pass

            # Listar serviços marcados a profissional----------"LSP Categoria NomeProfissional"
            elif(commands[0] == "LSP"):
                pass

            # Listar marcações por tipo de serviço--------------"LMS Serviço"
            elif(commands[0] == "LMS"):
                pass

            else:
                print("Instrução inválida.")
