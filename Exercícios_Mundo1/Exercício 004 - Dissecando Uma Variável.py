#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

d= input("Insira algo: \033[1m")
print(f"O tipo primitivo de \033[1m{d}\033[m é \033[1;31m{type(d)}\033[m.")
print(f"\033[1m{d}\033[m é alfábetico? \033[1;32m{d.isalpha()}\033[m.")
print(f"\033[1m{d}\033[m é um número? \033[1;33m{d.isnumeric()}\033[m.")
print(f"\033[1m{d}\033[m é alfanúmerico? \033[1;34m{d.isalnum()}\033[m.")
print(f"\033[1m{d}\033[m está escrito completamente em maíusculo? \033[1;35m{d.isupper()}\033[m.")
print(f"\033[1m{d}\033[m está escrito completamente em minúscula? \033[1;36m{d.islower()}\033[m.")
print(f"\033[1m{d}\033[m está capitalizada? \033[1;37m{d.istitle()}\033[m.")
