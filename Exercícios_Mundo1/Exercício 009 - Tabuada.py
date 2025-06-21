#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n= int(input("Insira o número: "))
print("\033[1m-\033[m" * 18)
print(f"A tabuada de \033[1m{n}\033[m é : \n{n} x {1:2} = \033[33m{n * 1}\033[m \n{n} x {2:2} = \033[33m{n * 2}\033[m \n{n} x {3:2} = \033[33m{n * 3} \n{n}\033[m x {4:2} = \033[32m{n * 4}\033[m \n{n} x {5:2} = \033[34m{n * 5}\033[m \n{n} x {6:2} = \033[36m{n * 6}\033[m \n{n} x {7:2} = \033[31m{n * 7}\033[m \n{n} x {8:2} = \033[37m{n * 8}\033[m \n{n} x {9:2} = \033[35m{n * 9}\033[m \n{n} x {10:2} = \033[34m{n  *10}\033[m")
print("\033[1m-\033[m" * 18)
