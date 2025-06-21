#Crie um programa que vai ler vários valores e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respecivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_n= []
while True:
    num= float(input("Insira um número: "))
    lista_n.append(num)

    while True:
        continuar= str(input(f"Você deseja continuar inserindo números?\n'S' = Sim\n'N' = Não\nSua escolha: ").strip())
        if continuar[0] in "sSnN":
            break
        print(f"A informação '{continuar}' fornecida não está entre as opções possíveis.\nPor favor, tente novamente.")
    if continuar in "nN":
        break

pares= []
impares= []
for numero in lista_n:
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 != 0:
        impares.append(numero)

if len(lista_n) > 1:
    print(f"Lista com todos os números: ", end= "")
else:
    print(f"A lista possui apenas {len(lista_n)} número: ", end= "")
for n in range(0, len(lista_n)):
    if n < (len(lista_n) - 2):
        print(f"{lista_n[n]}, ", end= "")
    elif n < (len(lista_n) - 1):
        print(f"{lista_n[n]} e ", end= "")
    elif n < len(lista_n):
        print(f"{lista_n[n]}.")

if len(pares) == 0:
    print(f"Nenhum número par foi digitado.")
elif len(pares) == 1:
    print(f"A lista de números pares possui apenas {len(pares)} número: {pares[0]}.")
elif len(pares) > 1:
    print(f"Lista com os números pares: ", end= "")
    for par in range(0, len(pares)):
        if par < (len(pares) - 2):
            print(f"{pares[par]}, ", end= "")
        elif par < (len(pares) - 1):
            print(f"{pares[par]} e ", end= "")
        elif par < len(pares):
            print(f"{pares[par]}.")

if len(impares) == 0:
    print(f"Nenhum número ímpar foi digitado.")
elif len(impares) == 1:
    print(f"A lista de números ímpares possui apenas {len(impares)} número: {impares[0]}.")
elif len(impares) > 1:
    print(f"Lista com os números ímpares: ", end= "")
    for impar in range(0, len(impares)):
        if impar < (len(impares) - 2):
            print(f"{impares[impar]}, ", end= "")
        elif impar < (len(impares) - 1):
            print(f"{impares[impar]} e ", end= "")
        elif impar < len(impares):
            print(f"{impares[impar]}.")
