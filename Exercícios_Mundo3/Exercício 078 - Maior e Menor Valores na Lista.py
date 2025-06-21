#Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respcetivas posições na lista.

numeros= []
for n in range(5):
    num= int(input(f"Digite o número da posição {n}: "))
    numeros.append(num)
maior= max(numeros)
menor= min(numeros)

if numeros.count(maior) > 1:
    print(f"O maior número digitado foi {maior}, nas posições ", end= "")
    vezes= numeros.count(maior)
    for posiçao, maiores in enumerate(numeros):
        if maiores == maior and vezes > 2:
            print(f"{posiçao}, ", end= "")
            vezes= vezes - 1
        elif maiores == maior and vezes > 1:
            print(f"{posiçao} e ", end= "")
            vezes= vezes - 1
        elif maiores == maior and vezes == 1:
            print(f"{posiçao}.")
else:
    print(f"O maior número digitado foi {maior}, na posição {numeros.index(maior)}.")

if numeros.count(menor) > 1:
    print(f"O menor número digitado foi {menor}, nas posições ", end= "")
    vezes= numeros.count(menor)
    for posiçao, menores in enumerate(numeros):
        if menores == menor and vezes > 2:
            print(f"{posiçao}, ", end= "")
            vezes= vezes - 1
        elif menores == menor and vezes > 1:
            print(f"{posiçao} ", end= "")
            vezes= vezes - 1
        elif menores == menor and vezes == 1:
            print(f"e {posiçao}.")
else:
    print(f"O menor número digitado foi {menor}, na posição {numeros.index(menor)}.")
