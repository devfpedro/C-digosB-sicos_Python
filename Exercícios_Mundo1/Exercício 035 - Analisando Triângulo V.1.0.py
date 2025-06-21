#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1= float(input("Informe o comprimento da \033[1;30mprimeira reta\033[m: ").strip())
reta2= float(input("Informe o comprimento da \033[1;30msegunda reta\033[m: ").strip())
reta3= float(input("Informe o comprimento da \033[1;30mterceira reta\033[m: ").strip())

if (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2 and (reta1 + reta2) > reta3:
    print(f"As retas \033[1m{reta1}\033[m, \033[1m{reta2}\033[m, \033[1m{reta3}\033[m \033[1;32mpodem formar um triângulo\033[m.")
else:
    print(f"As retas \033[1m{reta1}\033[m, \033[1m{reta2}\033[m, \033[1m{reta3}\033[m \033[1;34mnão podem formar um triângulo\033[m.")
