#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario= float(input("Informe o \033[1mseu salário\033[m: R$").strip())

if salario > 1250:
    print(f"O \033[1;34mnovo salario\033[m com aumento de 10% será de \033[3;35mR${salario + ((salario * 10) / 100):.2f}\033[m")
else:
    print(f"O \033[1;34mnovo salário\033[m com aumento de 15% será de \033[3;36mR${salario + ((salario * 15) / 100):.2f}\033[m")
