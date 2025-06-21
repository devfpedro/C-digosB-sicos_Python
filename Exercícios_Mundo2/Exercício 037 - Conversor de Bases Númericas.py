#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário;
#2 para octal;
#3 para hexadecimal.

num= int(input("Digite um número: ").strip())
print("Digite '1', '2' ou '3' para que seja decidido se o número será convertido em binário, octal ou hexadecimal, respectivamente:")
numero_conversor= int(input("Digite o número da coneversão: ").strip())

if numero_conversor == 1:
    print(f"O número {num} convertido para binário é igual a {bin(num) [2:]}")
elif numero_conversor == 2:
    print(f"O número {num} convertido para octal é igual a {oct(num) [2:]}")
elif numero_conversor == 3:
    print(f"O número {num} convertido para hexadecimal é igual a {hex(num) [2:]}")
else:
    print(f"Você não digitou nenhum número que corresponda as opções de conversão. Tente novamente.")
