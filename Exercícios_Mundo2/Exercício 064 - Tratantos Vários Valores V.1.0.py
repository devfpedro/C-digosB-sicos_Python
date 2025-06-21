#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero= 0
numeros= 0
soma= 0

while numero != 999:
    numero= int(input(f"Digite quantos números inteiros e positivos quiser.\nQuando quiser que o programa pare, digite '999'.\nDigite um número: "))

    if numero != 999:
        numeros= numeros + 1
        soma= soma + numero

if numeros > 1:
    print(f"No total, foram digitados {numeros} números\nA soma desses números é igual a {soma}")
else:
    print(f"Apenas {numeros} número foi digitado.\nA 'soma' desse único número é ele mesmo: {soma}.")
