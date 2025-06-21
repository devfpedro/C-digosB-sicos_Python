#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço 'for'.

#Desafio 009:
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num= int(input("Digite um número para vermos sua tabuada: "))
print(f"A tabuada do número {num} é:")

for tabuada in range(1, 11):
    print(f"{num} x {tabuada:2} = {num * tabuada}")
