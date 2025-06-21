#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma= 0

for par in range(6):
    num= int(input("Digite um número: "))

    if num % 2 == 0:
        soma= soma + num

if soma >= 1:
    print(f"O valor da soma dos números pares é: {soma}")
elif soma == 0:
    print(f"Nenhum número par foi digitado.")
