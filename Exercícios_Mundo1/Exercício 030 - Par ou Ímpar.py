#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num= int(input("Digite um \033[2mnúmero\033[m: "))

if num % 2 == 0:
    print(f"{num} é \033[1;31mpar\033[m.")
else:
    print(f"{num} é \033[1;34mímpar\033[m.")
