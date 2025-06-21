#Desenvolva um programa que leia o primeiro número e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1= int(input("Digite o primeiro termo (número) da PA: "))
razao= int(input("Digite a razão desta PA: "))
num_base= a1

for pa in range(1, 11):
    print(f"{num_base} ", end= "")
    num_base= a1 + (razao * pa)
