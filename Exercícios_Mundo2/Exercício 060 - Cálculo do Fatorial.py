#Faça um programa que leia um número qualquer e mostre seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120

n= int(input("Digite um número inteiro e positivo: "))
n_mul= n
guardar_n= n
n_lista= []

if n > 1:
    while n_mul > 1:
        n_mul= n_mul - 1
        n_lista.append(n_mul)
        n= n * n_mul

    print(f"{guardar_n}! = {guardar_n}", end= "")
    while guardar_n > 1:
        guardar_n= guardar_n - 1
        print(f"x{n_lista[0]}", end= "")
        n_lista.pop(0)
    print(f" = {n}")
else:
    print(f"{n}! = 1")

#Desafio Extra do Vídeo de Resolução: Fazer o mesmo programa, mas utilizando a Estrutura de Repetição For.

n= int(input("Digite um número inteiro e positivo: "))
print(f"{n}! = {n}", end= "")
for fatorial in range(n-1, 0, -1):
    n= n * fatorial
    print(f"x{fatorial}", end= "")
print(f" = {n}")
