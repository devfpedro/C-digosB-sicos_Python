#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.

from random import randint

tupla_n= (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f"Números sorteados: ", end= "")
for lista in range(0, 5):
    if lista < 4:
        print(f"{tupla_n[lista]}, ", end= "")
    else:
        print(f"{tupla_n[lista]}.")
print(f"O maior número sorteado foi {max(tupla_n)}\nO menor número sorteado foi {min(tupla_n)}")
