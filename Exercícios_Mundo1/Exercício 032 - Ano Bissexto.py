#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano= int(input("\033[3mInsira um ano:\033[m "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"\033[3;33m{ano} é ano bissexto.\033[m")
else:
    print(f"\033[3;34m{ano} não é um ano bissexto.\033[m")
