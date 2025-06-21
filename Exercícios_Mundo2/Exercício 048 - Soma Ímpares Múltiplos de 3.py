#Faça um programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

num_base= 0
c_n= 0

for soma in range(3, 500, 3):
    if soma % 2 != 0:
        num_base= num_base + soma
        c_n= c_n + 1

print(f"A soma dos {c_n} números {num_base}")
