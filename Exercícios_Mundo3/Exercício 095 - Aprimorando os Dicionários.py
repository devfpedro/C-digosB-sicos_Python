#Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from datetime import date
from time import sleep

perfil_jogadores= []

cadastro_jogador= 0
while True:
    dados_jogadores= {}
    cadastro_jogador= cadastro_jogador + 1
    dados_jogadores['N° de cadastro do jogador']= cadastro_jogador

    sleep(1)
    while True:
        print(f"\n" + f"=" * 90 + f"\n" + f"\033[1mPreenchimento dos Dados do Jogador na Temporada {date.today().year}\033[m".center(90) + f"\n" + f"=" * 90)
        nome_jogador= str(input(f"Informe o nome do jogador: ").lower().strip())
        n_ce= "Não"
        for conf_nomejogador in range(0, len(nome_jogador)):
            if nome_jogador[conf_nomejogador] in "1234567890|\!'@#$%¨&*()_-+=§´`{[]}^~<,>.:;?/°ºª":
                n_ce= "Sim"
        if n_ce == "Sim":
            print(f"-" * 90 + f"\nO nome do jogador não pode conter números ou caracteres especiais.\nPor favor, tente novamente.\n" + f"-" * 90)
        else:
            while True:
                print(f"-" * 90 + f"\nO nome do jogador '", end= "")
                for saida_nome in range(0, len(nome_jogador)):
                    if saida_nome == 0 or nome_jogador[saida_nome-1] == " ":
                        if nome_jogador[saida_nome] in "dD" and nome_jogador[saida_nome-1] == " " and (nome_jogador[saida_nome+2] == " " or nome_jogador[saida_nome+3] == " "):
                            print(f"{nome_jogador[saida_nome]}".lower(), end= "")
                        else:
                            print(f"{nome_jogador[saida_nome]}".upper(), end= "")
                    else:
                        print(f"{nome_jogador[saida_nome]}".lower(), end= "")
                    if saida_nome == len(nome_jogador) - 1:
                        print(f"' está correto?")
                confirmar= str(input(f"Digite 'Sim' para Confirmar\nDigite 'Não' para Inserir o nome do jogador novamente\nSua resposta: ").lower().strip())
                if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                    break
                print(f"-" * 90 + f"\nA informação '{confirmar}' não está entre as nenhuma das opções possíveis.\nPor favor, tente novamente.")
            if confirmar.capitalize() == "Sim":
                dados_jogadores['Nome do Jogador']= nome_jogador
                break
        
    while True:
        q_partidas= str(input(f"-" * 90 + f"\nInforme o N° de partidas jogadas na temporada: ").strip())
        if q_partidas[0] not in "1234567890":
            print(f"A informação '{q_partidas}' não pode ser considerada como quantidade de partidas.\nPor favor, tente novamente.")
        else:
            while True:
                confirmar= str(input(f"-" * 90 + f"\nA quantidade de {q_partidas} " + (f"partidas jogadas" if int(q_partidas) > 1 else f"partida jogada") + f" está correta?\nDigite 'Sim' para confirmar\nDigite 'Não' para Inserir novamente a quantidade de partidas jogadas\nSua resposta: ").lower().strip())
                if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                    break
                print(f"-" * 90 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
        if confirmar.capitalize() == "Sim":
            dados_jogadores['N° de Partidas Jogadas']= int(q_partidas)
            break

    while True:
        total_gols= 0
        for dados_partida in range(1, int(q_partidas)+1):
            while True:
                gols_partida= str(input(f"-" * 90 + f"\nQuantidade de Gols marcados na {dados_partida}° partida: ").strip())
                total_gols= total_gols + int(gols_partida)
                if gols_partida[0] not in "1234567890":
                    print(f"-" * 90 + f"\nA informação '{gols_partida}' não pode ser considerada como quantidade de gols para a {dados_jogadores}° partida.\nPor favor, tente novamente.")
                else:
                    dados_jogadores['Gols feitos na partida ' + str(dados_partida)]= int(gols_partida)
                    break
        while True:
            confirmar= str(input(f"-" * 90 + f"\nO número de gols por partida foi digitado corretamente?\nSe não, você pode informá-los novamente. Basta seguir as orienatções:\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir novamente a quantidade de gols por partida\nSua resposta: ").lower().strip())
            if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                break
            print(f"-" * 90 + f"\nA informação '{confirmar}' não está entre as opções possiveis.\nPor favor, tente novamente.")
        if confirmar.capitalize() == "Sim":
            dados_jogadores['Total de Gols feitos na temporada']= int(total_gols)
            break

    perfil_jogadores.append(dados_jogadores.copy())
    del dados_jogadores

    while True:
        continuar= str(input(f"-" * 90 +f"\nDeseja inserir os dados de mais algum jogador?\nDigite 'Sim' para Continuar\nDigite 'Não' para Encerrar\nSua resposta: ").lower().strip())
        if continuar.capitalize() == "Sim" or continuar.capitalize() == "Nao" or continuar.capitalize() == "Não":
            break
        print(f"-" * 90 + f"\nA informação '{continuar.capitalize()}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if continuar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
        break

q_letras= 0
for nome_maior in range(0, len(perfil_jogadores)):
    if len(perfil_jogadores[nome_maior]['Nome do Jogador']) > q_letras:
        q_letras= len(perfil_jogadores[nome_maior]['Nome do Jogador'])

sleep(1)
print(f"\n" + f"=" * 90 + f"\n" + (f"Dados dos Jogadores na Temporada {date.today().year}".center(90) if len(perfil_jogadores) > 1 else f"Dados do Jogador na Temporada {date.today().year}".center(90)) + f"\n" + f"=" * 90)
sleep(1)
print(f"N° de Cadastro" + f" " * 5 + f"Jogador" + f" " * (q_letras - 2) +  f"Total de Gols" + f"\n" + f"-" * 90)
for lista_jogadores in range(0, len(perfil_jogadores)):
    sleep(1)
    print(f"> {perfil_jogadores[lista_jogadores]['N° de cadastro do jogador']}" + f" " * (13 - len(str(perfil_jogadores[lista_jogadores]['N° de cadastro do jogador'])) + 4), end= "")
    for lista_jogadores1 in range(0, len(perfil_jogadores[lista_jogadores]['Nome do Jogador'])):
        if lista_jogadores1 == 0 or perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1-1] == " ":
            if perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1] in "dD" and perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1-1] == " " and  (perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1+2] == " " or perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1+3] == " "):
                print(f"{perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1]}".lower(), end= "")
            else:
                print(f"{perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1]}".upper(), end= "")
        else:
            print(f"{perfil_jogadores[lista_jogadores]['Nome do Jogador'][lista_jogadores1]}".lower(), end= "")
    print((f" " * ((q_letras - len(perfil_jogadores[lista_jogadores]['Nome do Jogador']) if len(perfil_jogadores[lista_jogadores]) < q_letras else 0) + 5)) + f"> {perfil_jogadores[lista_jogadores]['Total de Gols feitos na temporada']} ", end= "")
    print((f"gols em " if perfil_jogadores[lista_jogadores]['Total de Gols feitos na temporada'] > 1 else f"gol em ") + (f"{perfil_jogadores[lista_jogadores]['N° de Partidas Jogadas']} partidas" if perfil_jogadores[lista_jogadores]['N° de Partidas Jogadas'] > 1 else f"{perfil_jogadores[lista_jogadores]['N° de Partidas Jogadas']} partida"))

sleep(1)
while True:
    while True:
        num_jogador= 0
        letras_jogador= 0
        caractere_especial= 0
        sleep(1)
        print(f"\n" + f"=" * 90 + f"\n" + f"Pesquisar Estatísticas do Jogador na Temporada".center(90) + f"\n" + f"=" * 90)
        sleep(1)
        pesquisar_jogador= str(input(f"Para vizualisar as estatísticas de um Jogador, basta informar um dos dados abaixo:\n>|N° de Cadastro\n>|Nome Completo\nPesquisar Jogador: ").lower().strip())
        sleep(1)
        for conf_pesquisa in range(0, len(pesquisar_jogador)):
            if pesquisar_jogador[conf_pesquisa] in "aãâáàbcçdeêéèfghiîíìjklmnoõôóòpqrstuûúùvwxyz ":
                letras_jogador= letras_jogador + 1
            elif pesquisar_jogador[conf_pesquisa] in "1234567890":
                num_jogador= num_jogador + 1
            else:
                print(f"-" * 90 + f"\nO N° de Cadastro ou Nome do Jogador não pode conter caracteres especiais.\nPor favor, tente novamente.")
                caractere_especial= caractere_especial + 1
                break
        if caractere_especial == 0:
            if num_jogador > 0 and letras_jogador > 0:
                print(f"-" * 90 + f"\nO N° de Cadastro ou Nome do Jogador não pode possuir números e letras.\nO N° de Cadastro apenas pode ser composto por números.\nO Nome do Jogador só pode ser composto por letras.\nPor favor, tente novamente.")
            else:
                sleep(1)
                while True:
                    if pesquisar_jogador[0] in "1234567890":
                        print(f"-" * 90 + f"\nO N° de cadastro '{pesquisar_jogador}", end= "")
                    else:
                        print(f"-" * 90 + f"\nO nome do jogador '", end= "")
                        for saida_nome in range(0, len(pesquisar_jogador)):
                            if saida_nome == 0 or pesquisar_jogador[saida_nome-1] == " ":
                                if pesquisar_jogador[saida_nome] in "dD" and pesquisar_jogador[saida_nome-1] == " " and (pesquisar_jogador[saida_nome+2] == " " or pesquisar_jogador[saida_nome+3] == " "):
                                    print(f"{pesquisar_jogador[saida_nome]}".lower(), end= "")
                                else:
                                    print(f"{pesquisar_jogador[saida_nome]}".upper(), end= "")
                            else:
                                print(f"{pesquisar_jogador[saida_nome]}".lower(), end= "")
                    confirmar= str(input(f"' está correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir o nome novamente\nSua resposta: ").lower().strip())
                    if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                        break
                    else:
                        sleep(1)
                        print(f"-" * 90 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
                if confirmar.capitalize() == "Sim":
                    break

    if pesquisar_jogador[0] in "1234567890":
        pesquisar_jogador= int(pesquisar_jogador)
        tipo_pesquisa= "N° de cadastro do jogador"
    else:
        tipo_pesquisa= "Nome do Jogador"

    jogador_encontrado= "Não"
    for pesquisar_dados in range(0, len(perfil_jogadores)):
        if perfil_jogadores[pesquisar_dados][tipo_pesquisa] == pesquisar_jogador:
            jogador_encontrado= "Sim"
            print(f"-" * 90 + f"\n" + f"Nome do Jogador" + (f" " * (len(perfil_jogadores[pesquisar_dados]['Nome do Jogador']) - 13 + 5)) + f"Partidas Jogadas na Temporada" + f" " * 5 + f"Total de Gols")
            print(f"> ", end= "")
            for saida_nome in range(0, len(perfil_jogadores[pesquisar_dados]['Nome do Jogador'])):
                if saida_nome == 0 or perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome-1] == " ":
                    if perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome] in "dD" and perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome-1] == " " and (perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome+2] == " " or perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome+3] == " "):
                        print(f"{perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome]}".lower(), end= "")
                    else:
                        print(f"{perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome]}".upper(), end= "")
                else:
                    print(f"{perfil_jogadores[pesquisar_dados]['Nome do Jogador'][saida_nome]}".lower(), end= "")
            print(f" " * 5 + f"> {perfil_jogadores[pesquisar_dados]['N° de Partidas Jogadas']}", end= "")
            print(f" " * (32 - len(str(perfil_jogadores[pesquisar_dados]['N° de Partidas Jogadas']))) + f"> " + (f"{perfil_jogadores[pesquisar_dados]['Total de Gols feitos na temporada']} gols" if perfil_jogadores[pesquisar_dados]['Total de Gols feitos na temporada'] > 1 else f"{perfil_jogadores[pesquisar_dados]['Total de Gols feitos na temporada']} gol"))
            sleep(1)
            print(f"-" * 90 + f"\nGols feitos " + (f"em cada uma das {perfil_jogadores[pesquisar_dados]['N° de Partidas Jogadas']} partidas" if perfil_jogadores[pesquisar_dados]['N° de Partidas Jogadas'] > 1 else f"na 1 partida da temporada"))
            for gols_partida in range(1, perfil_jogadores[pesquisar_dados]['N° de Partidas Jogadas']+1):
                sleep(1)
                print(f"> { gols_partida:2}° Partida: {perfil_jogadores[pesquisar_dados]['Gols feitos na partida ' + str(gols_partida)]} " + (f"Gols" if perfil_jogadores[pesquisar_dados]['Gols feitos na partida ' + str(gols_partida)] > 1 else f"Gol"))
        elif jogador_encontrado == "Não" and pesquisar_dados == len(perfil_jogadores) - 1:
            if tipo_pesquisa == "N° de cadastro do jogador":
                print(f"-" * 90 + f"\nNenhum jogador com o N° de Cadastro '{pesquisar_jogador}' foi encontrado.")
            elif tipo_pesquisa == "Nome do Jogador":
                print(f"-" * 90 + f"\nNenhum jogador com o nome '", end= "")
                for saida_nome in range(0, len(pesquisar_jogador)):
                    if saida_nome == 0 or pesquisar_jogador[saida_nome-1] == " ":
                        if pesquisar_jogador[saida_nome] in "dD" and pesquisar_jogador[saida_nome-1] == " " and (pesquisar_jogador[saida_nome+2] == " " or pesquisar_jogador[saida_nome+3] == " "):
                            print(f"{pesquisar_jogador[saida_nome]}".lower(), end= "")
                        else:
                            print(f"{pesquisar_jogador[saida_nome]}".upper(), end= "")
                    else:
                        print(f"{pesquisar_jogador[saida_nome]}".lower(), end= "")
                print(f"' foi encontrado.")
    
    while True:
        sleep(1)
        continuar= str(input(f"-" * 90 + f"\nDeseja pesquisar as estatísticas de mais algum jogador?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Encerrar\nSua resposta: ").lower().strip())
        if continuar.capitalize() == "Sim" or continuar.capitalize() == "Nao" or continuar.capitalize() == "Não":
            break
        sleep(1)
        print(f"-" * 90 + f"\nA informação '{continuar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if continuar.capitalize() == "Nao" or continuar.capitalize() == "Não":
        sleep(1)
        print(f"-" * 90 + f"\nEncerrando...")
        sleep(1)
        break
