#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#a)Quantas vezes apareceu o valor 9;
#b)Em que posição foi digitado o primeiro valor 3;
#c)Quais foram os números pares.

tupla= (int(input("Digite o 1° número: ")), int(input("Digite o 2° número: ")), int(input("Digite o 3° número: ")), int(input("Digite o 4° número: ")))

if tupla.count(9) > 1:
    print(f"O número 9 apareceu {tupla.count(9)} vezes.")
elif tupla.count(9) == 1:
    print(f"O número 9 apareceu {tupla.count(9)} vez.")
else:
    print(f"O número 9 não apareceu nenhumas vez.")

if tupla.count(3) > 1:
    print(f"O número 3 foi inserido pela primeira vez na {tupla.index(3) + 1}° posição.")
elif tupla.count(3) == 1:
    print(f"O número 3 foi inserido pela primeira, e única, vez na {tupla.index(3) + 1}° posição.")
else:
    print(f"O número 3 não foi inserido em nenhuma posição.")

q_pares= 0
for pares in tupla:
    if pares % 2 == 0:
        q_pares= q_pares + 1
if q_pares > 1:
    print(f"Os números pares inseridos foram: ", end= "")
    for listagem in tupla:
        if listagem % 2 == 0 and q_pares > 1:
            print(f"{listagem}, ", end= "")
            q_pares= q_pares - 1
        elif listagem % 2 == 0 and q_pares == 1:
            print(f"{listagem}.")
elif q_pares == 1:
    print(f"O único número par inserido foi: ", end= "")
    for par in tupla:
        if par % 2 == 0:
            print(f"{par}.")
else:
    print(f"Nenhum número par foi inserido.")
