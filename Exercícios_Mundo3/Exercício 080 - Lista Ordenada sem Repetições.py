#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort). No final, mostre a lista ordenada na tela.

numeros= []
for n in range(1, 6):
    num= float(input(f"Digite o {n}° número: "))
    if n == 1:
        numeros.append(num)
        print(f"'{num}' adicionado na posição 0.")
    else:
        for conf in range(0, len(numeros)):
            if num > numeros[-1]:
                numeros.append(num)
                print(f"'{num}' será adicionado na posição {numeros.index(num)}.")
            elif num < numeros[0]:
                numeros.insert(0, num)
                print(f"'{num}' será adicionado na posição {numeros.index(num)}.")
            elif numeros.count(num) >= 1:
                print(f"'{num}' já foi adicionado na lista ", end= "")
                if numeros.count(num) > 1:
                    print(f"{numeros.count(num)} vezes. ", end= "")
                elif numeros.count(num) == 1:
                    print(f"{numeros.count(num)} vez. ", end= "")
                
                posi_num= numeros.index(num)
                numeros.insert(posi_num, num)
                print(f"Então, '{num}' será adicionado pela {numeros.count(num)}° vez na lista, na posição ", end= "")
                ult_num= 0
                for posiçao in range(0, len(numeros)):
                    if num == numeros[posiçao]:
                        ult_num= ult_num + 1
                    if ult_num == numeros.count(num):
                        ult_num= posiçao
                        break
                print(f"{ult_num}.")
            else:
                for inserir in range(0, len(numeros)-1):
                    if numeros[inserir] < num and num < numeros[inserir+1]:
                        numeros.insert(inserir+1, num)
                        print(f"'{num}' será adicionado na posição {numeros.index(num)}.")
            break

print(f"Lista dos 5 números digitados em ordem crescente: ", end= "")
for saida in range(0, len(numeros)):
    if saida < 3:
        print(f"{numeros[saida]}, ", end= "")
    elif saida < 4:
        print(f"{numeros[saida]} e ", end= "")
    else:
        print(f"{numeros[saida]}.")
