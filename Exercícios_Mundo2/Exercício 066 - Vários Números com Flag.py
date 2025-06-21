#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor '999', que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont= 0
soma= 0

while True:
    numero= int(input("Digite quantos números quiser:\nCaso queira que o programa seja encerrado, digite '999'.\nNúmero: "))
    
    if numero == 999:
        break
    
    cont= cont + 1
    soma= soma + numero

if cont == 1:
    print(f"Apenas o número {soma} foi digitado.\nEntão a soma de apenas {soma} é ele mesmo: {soma}.")
elif cont > 1:
    print(f"A todo, foram digitados {cont} números.\nA soma desses {cont} números é {soma}.")
