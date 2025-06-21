#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n= int(input("Digite o número inteiro que determinará a sua sequência de fibonacci: "))
rep= 0
f1= 0
f2= 0
soma= 0

while rep < n:
    if rep <= 1:
        print(f"{rep}, ", end= "")
        soma= 1
    elif rep > 1 and rep < (n - 2):
        f1= f2
        f2= soma
        soma= f1 + f2
        print(f"{soma}, ", end= "")
    elif rep == (n - 2):
        f1= f2
        f2= soma
        soma= f1 + f2
        print(f"{soma} e ", end= "")
    else:
        f1= f2
        f2= soma
        soma= f1 + f2
        print(f"{soma}.")

    rep= rep + 1
