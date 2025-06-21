#Faça um programa que tenha uma função chamada "maior()", que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def maior(q_sorteados, maior_n):
    sleep(1.5)
    print(f"Foram sorteados {q_sorteados} números." if q_sorteados > 1 else f"Foi sorteado {q_sorteados} número.")
    sleep(1.5)
    print(f"O maior número sorteado foi {maior_n}.")

q_chamadas= randint(1, 10)
for chamadas in range(1, q_chamadas+1):
    q_sorteados= randint(1, 10)
    print((f"=" * 60) + f"\nNúmeros sorteados: " if q_sorteados > 1 else (f"=" * 50) + f"\nNúmero sorteado: ", end= "")
    sleep(1.5)
    for sorteio in range(1, q_sorteados+1):
        sleep(0.5)
        n_sorteado= randint(1, 100)
        if sorteio < (q_sorteados - 1):
            print(f"{n_sorteado}, ", end= "", flush= True)
        elif sorteio < q_sorteados:
            print(f"{n_sorteado} e ", end= "", flush= True)
        elif sorteio == q_sorteados:
            print(f"{n_sorteado}.")
        
        if sorteio == 1:
            maior_n= n_sorteado
        else:
            if n_sorteado > maior_n:
                maior_n= n_sorteado
    maior(q_sorteados, maior_n)
