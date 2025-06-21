#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior;
#O segundo valor é maior;
#Não existe valor maior, os dois são iguais.

num1= int(input("Digite o primeiro número: ").strip())
num2= int(input("Digite o segundo número: ").strip())

if num1 > num2:
    print(f"O primeiro valor é maior.")
elif num2 > num1:
    print(f"O segundo valor é maior.")
else:
    print(f"Não existe valor maior, os dois são iguais.")
