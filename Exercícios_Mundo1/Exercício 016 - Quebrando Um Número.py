#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex:
#Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

num_real= float(input("Informe um número real: \033[1m"))
print(f"\033[0mO número real\033[m \033[3m{num_real}\033[m tem como parte inteira o \033[4m{int(num_real)}\033[m.")
