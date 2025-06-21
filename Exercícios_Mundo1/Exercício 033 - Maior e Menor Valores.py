#Faça um programa que leia três números e mostre qual é o maior deles e qual é o menor.

n1= float(input("Insira o \033[1mprimeiro número\033[m: "))
n2= float(input("Insira o \033[1msegundo número\033[m: "))
n3= float(input("Insira o \033[1mterceiro número\033[m: "))

maior= n1
menor= n1

if n2 > maior:
    maior= n2
if n3 > maior:
    maior= n3

if n2 < menor:
    menor= n2
if n3 < menor:
    menor= n3

print(f"O maior número foi \033[3;32m{maior:.0f}\033[m")
print(f"O menor número foi \033[3;33m{menor:.0f}\033[m")
