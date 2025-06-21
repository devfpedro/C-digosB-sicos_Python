#Aprimore o desafio anterior, mostrando no final:
#a)A soma de todos os valores pares digitados;
#b)A soma dos valores da terceira coluna;
#c)O maior valor da segunda linha.

matriz= []
linha_coluna0= []
linha_coluna1= []
linha_coluna2= []
matriz.append(linha_coluna0)
matriz.append(linha_coluna1)
matriz.append(linha_coluna2)
pares= []
soma_coluna2= []
for linha in range(0, 3):
    for coluna in range(0, 3):
        n= int(input(f"Insira o número da linha {linha} coluna {coluna}: "))
        matriz[linha].append(n)

        if n % 2 == 0:
            pares.append(n)
        if coluna == 2:
            soma_coluna2.append(n)

maior_n= 0
for maior in range(0, 3):
    for maior1 in range(0, 3):
        if matriz[maior][maior1] > maior_n:
            maior_n= matriz[maior][maior1]
maior_n= len(str(maior_n))

print(f" " + f"\033[4m \033[m" * maior_n + f" " + f"\033[4m \033[m" * maior_n + f" " + f"\033[4m \033[m" * maior_n)
for saida in range(0, 3):
    for saida1 in range(0, 3):
        cal= maior_n - len(str(matriz[saida][saida1]))
        if saida1 == 0:
            if cal > 0:
                print(f"|" + f"\033[4m " * cal, end= "")
            else:
                print(f"|", end= "")
            print(f"\033[4m{matriz[saida][saida1]}\033[m|", end= "")
        elif saida1 == 1:
            if cal > 0:
                print(f"\033[4m " * cal, end= "")
            print(f"\033[4m{matriz[saida][saida1]}\033[4m|", end= "")
        elif saida1 == 2:
            if cal > 0:
                print(f"\033[4m " * cal, end= "")
            print(f"\033[4m{matriz[saida][saida1]}\033[m|")

if len(pares) > 0:
    if len(pares) == 1:
        print(f"\nFoi digitado apenas {len(pares)} número par: {pares[0]}.")
    else:
        soma= 0
        print(f"\nForam digitados {len(pares)} números pares: ", end= "")
        for par in range(0, len(pares)):
            soma= soma + pares[par]
            if par < (len(pares) - 2):
                print(f"{pares[par]}, ", end= "")
            elif par < (len(pares) - 1):
                print(f"{pares[par]} e ", end= "")
            else:
                print(f"{pares[par]}, cuja a soma desses números é igual a {soma}.")
else:
    print(f"\nNenhum número par foi digitado.")

print(f"Os 3 números da 2° coluna são: ", end= "")
soma= 0
for coluna2 in range(0, len(soma_coluna2)):
    soma= soma + soma_coluna2[coluna2]
    if coluna2 == 0:
        print(f"{soma_coluna2[coluna2]}, ", end= "")
    elif coluna2 == 1:
        print(f"{soma_coluna2[coluna2]} e ", end= "")
    else:
        print(f"{soma_coluna2[coluna2]}, cuja a soma desses números é igual a {soma}.")

print(f"O maior número da 1° linha é {max(matriz[1])}, que se repete {matriz[1].count(max(matriz[1]))} ", end= "")
if matriz[1].count(max(matriz[1])) > 1:
    print(f"vezes.\n")
else:
    print(f"vez.\n")
