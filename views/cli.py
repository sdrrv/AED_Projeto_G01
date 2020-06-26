from controllers.controller import Controller


def CLI():
    controller = Controller()

    while True:
        line = input()
        if line == "":
            exit()
        commands = line.split()

        # Resgistar Profissional-----------------------"RP Categoria Nome"
        if (commands[0] == "RP"):
            if controller.has_professional(commands[2]):
                print("Profissional existente.")

            elif not controller.has_categoria(commands[1]):
                print("Categoria inexistente.")

            else:
                controller.registar_profissional(commands[2])
                print("Profissional registado com sucesso.")

        # Resgistar Utente------------------------------"RU Nome FaixaEtária"
        elif (commands[0] == "RU"):

            if controller.has_utente(commands[1]):
                print("Utente existente.")

            elif not controller.has_faixa_etaria(commands[2]):
                print("Faixa etária inexistente.")

            else:
                controller.registar_utente(commands[1])
                print("Utente registado com sucesso.")

        # Resgistar Familia-----------------------------"RF NomeFamilia"
        elif(commands[0] == "RF"):

            pass

        # Associar utente a familia---------------------"AF Nome NomeFamiia"
        elif(commands[0] == "AF"):
            pass

        # Desassociar utende de familia------------------"DF Nome"
        elif(commands[0] == "DF"):
            pass

        # Listar Profissionais---------------------------"LP"
        elif(commands[0] == "LP"):
            pass

        # Listar Utentes---------------------------------"LU"
        elif(commands[0] == "LU"):
            pass

        # Listar Familias--------------------------------"LF"
        elif(commands[0] == "LF"):
            pass

        # Mostrar Familia--------------------------------"MF NomeFamila"
        elif(commands[0] == "MF"):
            pass

        # Marcar ciudados a utente-----------------------"MC Nome // Serviço // Categoria Nome Profissional"
        elif(commands[0] == "MC"):
            pass

        # Cancelar cuidados a utente---------------------"CC Nome"
        elif(commands[0] == "CC"):
            pass

        # Listar cuidados marcados a utente -------------"LCU Nome"
        elif(commands[0] == "LCU"):
            pass

        # Listar cuidados marcados a Familia -------------"LCF NomeFamilia"
        elif(commands[0] == "LCU"):
            pass

        # Listar serviços marcados a profissional----------"LSP Categoria NomeProfissional"
        elif(commands[0] == "LSP"):
            pass

        # Listar marcações por tipo de serviço--------------"LMS Serviço"
        elif(commands[0] == "LMS"):
            pass

        #Gravar---------------------------------------------"G[ NomeDoFicheiro]"
        elif(commands[0] == "G"):
            pass

        #Ler-------------------------------------------------"L[ NomeDoFicheiro]"
        elif(commands[0] == "L"):
            pass
        # ------------------------------------------------------------------------------------------------
        else:
            print("Instrução inválida")
