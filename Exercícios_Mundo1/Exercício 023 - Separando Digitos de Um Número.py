#Faça um programa que leia um número de 0 a 9999 e mostre cada um dos digitos separados.

#Ex: 
#Digite um número: 1834

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

num= int(input("Insira um número entre 1 e 9999: "))
print(f"O número '\033[1;43m{num}\033[m' está sendo analizado..." f"\nUnidade: \033[3m{(num // 1) % 10}\033[m" f"\nDezena: \033[3m{(num // 10) % 10}\033[m" f"\nCentena: \033[3m{(num // 100) % 10}\033[m" f"\nMilhar: \033[3m{(num // 1000) % 10}\033m")
