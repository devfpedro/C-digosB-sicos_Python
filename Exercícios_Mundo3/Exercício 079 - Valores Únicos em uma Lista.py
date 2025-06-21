#Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

g_numeros= []
while True:
    numero= float(input("Digite um número: "))
    if numero in g_numeros:
        print(f"O número '{numero}' já está na lista.\nPortanto, não será adicionado.")
    else:
        print(f"O número '{numero}' não está na lista.\nPortanto, será adicionado.")
        g_numeros.append(numero)

    while True:
        cont= str(input(f"Deseja continuar inserido números?\n[S] = Sim\n[N] = Não\nSua reposta: ").strip())
        if cont[0] in "sSnN":
            break
        print(f"A resposta '{cont}' não condiz com nenhuma das possibilidades possíveis.\nPor favor, tente novamente.")
    if cont[0] in "nN":
        break

g_numeros.sort()
if len(g_numeros) > 1:
    print(f"Os números registrados na lista: ", end= "")
elif len(g_numeros) == 1:
    print(f"O único número registrado na lista: ", end= "")
for exibiçao in g_numeros:
    if exibiçao == g_numeros[-1]:
        print(f"{exibiçao}.")
    elif exibiçao == g_numeros[-2]:
        print(f"{exibiçao} e ", end= "")
    else:
        print(f"{exibiçao}, ", end= "")
