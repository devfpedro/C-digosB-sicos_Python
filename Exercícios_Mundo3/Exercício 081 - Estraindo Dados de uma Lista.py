#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#a)Quantos números foram digitados;
#b)A lista de valores, ordenados de forma descrecente.
#c)Se o valor 5 foi digitado e está ou não na lista.

numeros= []
while True:
    n= float(input("Digite um número: "))
    numeros.append(n)

    while True:
        cont= str(input(f"Deseja inserir mais um número?\n[S] -> Sim\n[N] -> Não\nSua reposta: ").strip())
        if cont[0] in "sSnN":
            break
        else:
            print(f"'{cont}' não está entre as opções possíveis.\nPor favor, tente novamente.")
    if cont in "nN":
        break

if len(numeros) > 1:
    print(f"Foram digitados {len(numeros)} números.")
    print(f"Lista com todos os números digitados em ordem descrecente: ", end= "")
else:
    print(f"Foi digitado apenas {len(numeros)} número.")
    print(f"Lista com o único número digitado: ", end= "")

numeros.sort(reverse= True)
for numero in range(0, len(numeros)):
    if numero <= (len(numeros) - 3):
        print(f"{numeros[numero]}, ", end= "")
    elif numero <= (len(numeros) - 2):
        print(f"{numeros[numero]} e ", end= "")
    elif numero == (len(numeros) - 1):
        print(f"{numeros[numero]}.")

if 5 in numeros:
    print(f"O número 5 foi digitado na lista ", end= "")
    if numeros.count(5) > 1:
        print(f"{numeros.count(5)} vezes.")
    else:
        print(f"{numeros.count(5)} vez.")
else:
    print(f"O número 5 não foi digitado nenhuma vez.")
