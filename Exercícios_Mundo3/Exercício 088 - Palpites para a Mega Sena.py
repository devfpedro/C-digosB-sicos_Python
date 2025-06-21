#Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

jogo_completo= []
while True:
    n_jogos= int(input("Informe a quantidade de jogos que você deseja adquirir: "))
    if n_jogos == 0:
        while True:
            confirmaçao= str(input(f"Tem certeza de que não deseja adquirir nenhuma cartela?\nSim = Não Adquirir Nenhuma Cartela\nNão = Adquirir Pelo Menos Uma Cartela\nSua resposta: ").strip())
            if confirmaçao.lower() == "sim" or confirmaçao == "não" or confirmaçao.lower() == "nao":
                break
            print(f"A informação '{confirmaçao}' não confiz com nenhuma das opções possíveis.\nPor favor, tente novamente.")
        if confirmaçao.lower() == "sim":
            break
    else:
        break

numeros= []
for g_numeros in range(1, 61):
    numeros.append(g_numeros)

if n_jogos > 0:
    print(f"=" * 32 if n_jogos > 1 else f"=" * 31)
    if n_jogos > 1:
        print(f"-" * 5 + "{" + f"\033[1mSorteando {n_jogos} Cartelas\033[1m" + "}" + f"-" * 5)
    elif n_jogos == 1:
        print(f"-" * 5 + "{" + f"\033[1mSorteando {n_jogos} Cartela\033[m" + "}" + f"-" * 5)
    print(f"=" * 32 if n_jogos > 1 else f"=" * 31)
for q_jogos in range(0, n_jogos):
    jogo_completo.append(sample(numeros, 6))
    sleep(1)
    print(f"Jogo {q_jogos+1}: ", end= "")
    for num in range(0, 6):
        if num < 5:
            print(f"\033[1m{jogo_completo[q_jogos][num]}\033[m, ", end= "")
        else:
            print(f"\033[1m{jogo_completo[q_jogos][num]}\033[m.")
    if q_jogos == n_jogos - 1:
        print(f"_" * 32 if n_jogos > 1 else f"_" * 31)
        sleep(1)
        print(f"Boa sorte e volte sempre!".center(32))
