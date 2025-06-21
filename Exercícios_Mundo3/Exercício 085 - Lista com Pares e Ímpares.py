#Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

t_numeros= []
pares= []
impares= []
t_numeros.append(pares)
t_numeros.append(impares)
for n in range(1, 8):
    numero= (int(input(f"Digite o {n}° número: ")))
    if numero % 2 == 0:
        t_numeros[0].append(numero)
    else:
        t_numeros[1].append(numero)

t_numeros[0].sort()
if len(t_numeros[0]) > 1:
    print(f"Os números pares digitados foram: ", end= "")
elif len(t_numeros[0]) == 1:
    print(f"O número par digitado foi: ", end= "")
else:
    print(f"Nenhum número par foi digitado.")
for par in range(0, len(t_numeros[0])):
    if par < (len(t_numeros[0]) - 2):
        print(f"{t_numeros[0][par]}, ", end= "")
    elif par < (len(t_numeros[0]) - 1):
        print(f"{t_numeros[0][par]} e ", end= "")
    else:
        print(f"{t_numeros[0][par]}.")

t_numeros[1].sort()
if len(t_numeros[1]) > 1:
    print(f"Os números ímpares digitados foram: ", end= "")
elif len(t_numeros[1]) == 1:
    print(f"O número ímpar digitado foi: ", end= "")
else:
    print(f"Nenhum número par foi digitado.")
for impar in range(0, len(t_numeros[1])):
    if impar < (len(t_numeros[1]) - 2):
        print(f"{t_numeros[1][impar]}, ", end= "")
    elif impar < (len(t_numeros[1]) - 1):
        print(f"{t_numeros[1][impar]} e ", end= "")
    else:
        print(f"{t_numeros[1][impar]}.")
