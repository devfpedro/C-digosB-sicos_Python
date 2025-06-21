#Faça um algoritmo que leia o salário de um funcionário e moste seu novo salário, com 15% de aumento.

salario= float(input("\033[1mInforme seu salário atual\033[m: "))
print(f"Seu salário, com o \033[3maumento de 15%\033[m, será de \033[3m{salario + ((salario * 15) / 100):.2f}\033[m")
