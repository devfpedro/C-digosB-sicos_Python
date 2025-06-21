#Faça um programa que tenha uma lista chamada "números()", e duas funções chamadas "sorteio()" e "somaPar()". A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

def sorteio(numeros):
    print((f"=" * 40) + f"\n" + f"Sorteando Números".center(40) + f"\n" + (f"=" * 40))
    sleep(1)
    print(f"Números sorteados: ", end= "")
    for total in range(0, 5):
        numeros.append(randint(1, 10))
        sleep(1)
        print(f"{numeros[total]}, " if total < 3 else f"{numeros[total]} e " if total == 3 else f"{numeros[total]}.", end= "" if total < 4 else f"\n", flush= True)

def somaPar(soma):
    for pares in range(len(numeros)):
        if numeros[pares] % 2 == 0:
           soma= soma + numeros[pares]
    sleep(1)
    print(f"A soma entre todos os números pares é igual a {soma}")

numeros= []
sorteio(numeros)
somaPar(0)
