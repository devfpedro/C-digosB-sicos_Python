#Crie um programa onde 4 jogadores joguem um jogo e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores= {}

print(f"=" * 30 + f"\n" + f"Lançando os Dados!".center(30) + f"\n")
for num in range(1, 5):
    sleep(1)
    num_dado= randint(1, 6)
    jogadores['Jogador N°' + str(num)]= num_dado
    print(f" => O Jogador N°{num} tirou: {num_dado}")

print(f"\n" + f"=" * 30 + f"\n" + f"[Ranking]".center(30) + f"\n")
lugar= 0
for dado in range(6, 0, -1):
    for jogador in range(1, 5):
        if jogadores['Jogador N°' + str(jogador)] == dado:
            sleep(1)
            lugar= lugar + 1
            print(f"    {lugar}° Lugar: Jogador N°{jogador}")
    if lugar == 4:
        print()
        break
