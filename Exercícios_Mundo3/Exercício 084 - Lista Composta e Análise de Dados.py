#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a)Quantas pessoas foram cadastrados;
#b)Uma listagem com as pessoas mais pesadas;
#c)Uma listagem com as pessoas mais leves.

pessoas= []
dados= []
print(f"=" * 30)
print(f"Preenchimento de Dados".center(30))
while True:
    print(f"=" * 30)
    pessoas.append(str(input(f"Informe seu nome: ").capitalize().strip()))
    pessoas.append(float(input(f"Informe seu peso(em Kg): ")))
    dados.append(pessoas[:])
    pessoas.clear()
    
    while True:
        cont= str(input(f"Deseja inserir mais dados?\nSim -> Continuar\nNão -> Encerrar\nSua resposta: ").strip())
        if cont in "sSnN" or cont.upper() in "SIMNÃONAO":
            break
        print(f"'{cont}' não está entre as opções possíveis.\nPor favor, tente novamente.")
    if cont[0] in "nN" or cont.upper() in "NÃONAO":
        break

print(f"=" * 30)
print(f"Tabela de Dados".center(30))
print(f"=" * 30)
if len(dados) == 1:
    print(f"{len(dados)} pessoa foi cadastrada.")
elif len(dados) > 1:
    print(f"{len(dados)} pessoas foram cadastradas.")

for pesos in range(0, len(dados)):
    if pesos == 0:
        maior_kg= dados[pesos][1]
        menor_kg= dados[pesos][1]
    elif pesos > 0:
        if dados[pesos][1] > maior_kg:
            maior_kg= dados[pesos][1]
        if dados[pesos][1] < menor_kg:
            menor_kg= dados[pesos][1]

q_maior= 0
q_menor= 0
for quilos in range(0, len(dados)):
    if dados[quilos][1] == maior_kg:
        q_maior= q_maior + 1
    if dados[quilos][1] == menor_kg:
        q_menor= q_menor + 1

print(f"O maior peso registrado foi {maior_kg}Kg, com ", end= "")
for peso in range(0, len(dados)):
    if dados[peso][1] == maior_kg:
        if q_maior > 2:
            print(f"{dados[peso][0]}, ", end= "")
            q_maior= q_maior - 1
        elif q_maior > 1:
            print(f"{dados[peso][0]} e ", end= "")
            q_maior= q_maior - 1
        elif q_maior == 1:
            print(f"{dados[peso][0]} tendo esse peso.")

print(f"O menor peso registrado foi {menor_kg}Kg, com ", end= "")
for peso in range(0, len(dados)):
    if dados[peso][1] == menor_kg:
        if q_menor > 2:
            print(f"{dados[peso][0]}, ", end= "")
            q_menor= q_menor - 1
        elif q_menor > 1:
            print(f"{dados[peso][0]} e ", end= "")
            q_menor= q_menor - 1
        elif q_menor == 1:
            print(f"{dados[peso][0]} tendo esse peso.")
