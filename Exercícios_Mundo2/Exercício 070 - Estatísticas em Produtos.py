#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#a) Qual é o total gasto na compra.
#b) Quantos produtos custam mais de R$1000,00
#c) Qual é o nome do produto mais barato.

from time import sleep

total_gasto= 0
produto_mil= 0
lista_maisbarato= []

while True:
    print(f"=" * 35)
    produto= str(input("Informe o nome do produto: ").capitalize().strip())
    while True:
        preço= float(input("Informe o preço do produto: R$"))
        if preço > 0:
            break
        else:
            print(f"O produto não pode custar R${preço:.2f}.Ele precisa ter algum valor atribuído.\nPor favor, insira novamente o valor.")
    print(f"=" * 35)

    total_gasto= total_gasto + preço

    if preço > 1000:
        produto_mil= produto_mil + 1

    if preço == total_gasto:
        lista_maisbarato.append(produto)
        preço_maisbarato= preço
    else:
        if preço < preço_maisbarato:
            preço_maisbarato= preço
            lista_maisbarato.clear()
            lista_maisbarato.append(produto)
        elif preço == preço_maisbarato:
            lista_maisbarato.append(produto)

    while True:
        continuar= str(input("Você deseja inserir mais algum produto a sua lista?\n[S] -> Sim\n[N] -> Não\nSua resposta: ").upper().strip())
        if continuar == "S" or continuar == "N":
            break
        else:
            print(f"'{continuar}' não é uma informação válida.\nPor favor, tente novamente.")
    
    if continuar == "N":
        print(f"Finalizando lista...")
        print(f"_" * 35)
        sleep(1)
        break

if total_gasto == 1:
    print(f"Ao todo, foi gasto R${total_gasto:.2f}")
elif total_gasto > 1:
    print(f"Ao todo, foram gastos R${total_gasto:.2f}")

if produto_mil == 1:
    print(f"Apenas {produto_mil} produto custou mais de R$1000,00")
elif produto_mil > 1:
    print(f"Ao todo, {produto_mil} produtos custaram mais de R$1000,00")
else:
    print(f"Nenhum produto custou mais de R$1000,00")

leitura_maisbarato= len(lista_maisbarato)
if leitura_maisbarato == 1:
    print(f"O produto mais barato comprado foi: {lista_maisbarato[0]}, por R${preço_maisbarato:.2f}")
elif leitura_maisbarato == 2:
    print(f"Os {leitura_maisbarato} produtos mais baratos comprados foram: {lista_maisbarato[0]} e {lista_maisbarato[1]}, por R${preço_maisbarato:.2f}")
elif leitura_maisbarato > 2:
    print(f"Os {leitura_maisbarato} produtos mais baratos comprados foram: ", end= "")
    for maisbarato in range(1, leitura_maisbarato+1):
        if maisbarato >= 1 and maisbarato < (leitura_maisbarato - 1):
            print(f"{lista_maisbarato[0]}, ", end= "")
            lista_maisbarato.pop(0)
        elif maisbarato == (leitura_maisbarato - 1):
            print(f"{lista_maisbarato[0]} e ", end= "")
            lista_maisbarato.pop(0)
        
    print(f"{lista_maisbarato[0]}, por R${preço_maisbarato:.2f}")
    lista_maisbarato.pop(0)
print(f"_" * 35)
