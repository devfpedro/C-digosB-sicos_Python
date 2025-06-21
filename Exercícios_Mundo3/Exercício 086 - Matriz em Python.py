#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#  _ _ _
#0|_|_|_|
#1|_|_|_|
#2|_|_|_|
#  0 1 2
#No final, mostre a matriz na tela, com a formatação correta.

matriz= []
linha_coluna0= []
linha_coluna1= []
linha_coluna2= []
matriz.append(linha_coluna0)
matriz.append(linha_coluna1)
matriz.append(linha_coluna2)
for linha in range(0, 3):
    for coluna in range(0, 3):
        n= int(input(f"Insira o número da linha {linha} coluna {coluna}: "))
        matriz[linha].append(n)

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
print(f"\n")
