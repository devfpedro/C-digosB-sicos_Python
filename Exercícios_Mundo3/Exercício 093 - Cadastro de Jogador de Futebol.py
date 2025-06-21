#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep

dados_partidas= {}
print(f"=" * 50 + f"\n" + f"\033[1mInserir Informações do Jogador\033[m".center(57) + f"\n" + f"=" * 50)
while True:
    jogador= str(input(f"Qual o nome do Jogador? ").lower().strip())
    print(f"-" * 50 + f"\nO nome do jogador '", end= "")
    for nome in range(0, len(jogador)):
        if nome == 0 or jogador[nome-1] == " ":
            if jogador[nome] in "dD" and jogador[nome-1] == " " and (jogador[nome+2] == " " or jogador[nome+3] == " "):
                print(f"{jogador[nome]}".lower(), end= "")
            else:
                print(f"{jogador[nome]}".upper(), end= "")
        else:
            if nome < len(jogador) - 1:
                print(f"{jogador[nome]}".lower(), end= "")
            else:
                print(f"{jogador[nome]}' está correto?".lower())
    while True:
        confirmar= str(input(f"Digite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente\nSua reposta: ").lower().strip())
        if confirmar.capitalize() in "SimNaoNão":
            break
        print(f"-" * 50 + f"\nA informação {confirmar} não está entre as opções disponiveis.\nPor favor, tente novamente." + f"\n" + f"-" * 50)
    if confirmar.capitalize() == "Sim":
        dados_partidas['Nome do Jogador']= jogador
        break
    print(f"-" * 50)

while True:
    q_partidas= int(input(f"-" * 50 + f"\nInforme a quantidade de partidas que foram jogadas: "))
    while True:
        confirmar= str(input(f"-" * 50 + f"\nA informação de '{q_partidas} " + (f"partidas jogadas'" if q_partidas > 1 else f"partida jogada'") + f" está correta?" f"\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente a informação\nSua resposta: ").lower().strip())
        if confirmar.capitalize() in "SimNaoNão":
            break
        print(f"-" * 50 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if confirmar.capitalize() == "Sim":
        dados_partidas['N° de Partidas Jogadas']= q_partidas
        break

soma= 0
for partidas in range(1, q_partidas+1):
    dados_partidas['Gols na Partida N°' + str(partidas)] = int(input(f"-" * 50 + f"\nQuantidade de gols que ele fez na {partidas}° partida: "))
    soma= soma + dados_partidas['Gols na Partida N°' + str(partidas)]
dados_partidas['Total de Gols na Temporada']= soma

print(f"\n" + f"=" * 50 + f"\n" + f"\033[1mDados do Jogador\033[m".center(57) + f"\n" + f"=" * 50 + f"\nJogador: ", end= "")
sleep(1)
for nome in range(0, len(jogador)):
    if nome == 0 or jogador[nome-1] == " ":
        if jogador[nome] in "dD" and jogador[nome-1] == " " and (jogador[nome+2] == " " or jogador[nome+3] == " "):
            print(f"{jogador[nome]}".lower(), end= "")
        else:
            print(f"{jogador[nome]}".upper(), end= "")
    else:
        if nome < len(jogador) - 1:
            print(f"{jogador[nome]}".lower(), end= "")
        else:
            print(f"{jogador[nome]}".lower())
sleep(1)
print(f"Partidas jogadas: {dados_partidas['N° de Partidas Jogadas']}" + f"\nGols " + (f"nas partidas" if dados_partidas['N° de Partidas Jogadas'] > 1 else f"na única partida") + f" da temporada: ")
for dados in range(1, q_partidas+1):
    sleep(1)
    print(f" =>{ dados:2}° Partida: {dados_partidas['Gols na Partida N°' + str(dados)]} " + (f"gols" if dados_partidas['Gols na Partida N°' + str(dados)] > 1 else f"gol"))
sleep(1)
print(f"Ao todo, " + (f"foram {dados_partidas['Total de Gols na Temporada']} gols " if dados_partidas["Total de Gols na Temporada"] > 1 else f"foi {dados_partidas['Total de Gols na Temporada']} gol ") + f"na temporada.")
