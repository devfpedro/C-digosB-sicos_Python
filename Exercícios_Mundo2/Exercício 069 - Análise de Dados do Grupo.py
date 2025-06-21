#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não quer continuar. No final, mostre: 
#a) Quantas pessoas têm mais de 18 anos.
#b) Quantos homens foram cadastrados.
#c) Quantas mulheres têm menos de 20 anos.

from time import sleep

soma_maioridade= 0
soma_homens= 0
mulheres_jovens= 0
pessoas= 0

while True:
    print(f"=" * 22)
    print(f" " + f"Cadastros de Pessoas" + f" ")
    print(f"=" * 22)
    while True:
        idade= int(input("Informe a sua idade: "))
        if idade >= 0:
            break
        else:
            print(f"A informação '{idade}' é inválida como idade possível.\nPor favor, tente novamente.")
    while True:
        sexo= str(input(f"Informe o seu sexo:\n[M] = Masculino\n[F] = Feminino\nSua resposta: ").upper().strip())
        if sexo == "M" or sexo == "F":
            break
        else:
            print(f"A informação '{sexo}' inserida não corresponde a nenhuma das opções possíveis.\nPor favor, tente novamente.")

    pessoas= pessoas + 1

    if idade >= 18:
        soma_maioridade= soma_maioridade + 1
    
    if sexo == "M":
        soma_homens= soma_homens + 1
    
    if idade < 20 and sexo == "F":
        mulheres_jovens= mulheres_jovens + 1

    while True:
        continuar= str(input(f"Deseja continuar?\n[S] = Sim\n[N] = Não\nSua resposta: ").upper().strip())
        if continuar == "S" or continuar == "N":
            break
        else:
            print(f"A informação '{continuar}' inserida não corresponde a nenhuma das opções possíveis.\nPor favor, tente novamente.")
    
    if continuar == "N":
        print(f"Encerrando...")
        sleep(1)
        break

if pessoas == 1:
    print(f"-" * 42)
    print(f" " + f"Com apenas uma pessoa cadastrada, temos:" + f" ")
    print(f"-" * 42)
elif pessoas != 1:
    print(f"-" * 38)
    print(f" " + f"Com as {pessoas} pessoas cadastradas, temos:" + f" ")
    print(f"-" * 38)

if soma_maioridade == 1:
    print(f"Apenas uma pessoa tem mais de 18 anos.")
elif soma_maioridade != 1:
    print(f"{soma_maioridade} pessoas têm mais de 18 anos.")

if soma_homens == 1:
    print(f"Apenas um homem foi cadastrado.")
elif soma_homens != 1:
    print(f"{soma_homens} homens foram cadastrados.")

if mulheres_jovens == 1:
    print(f"Apenas um mulher tem menos de 20 anos.")
elif mulheres_jovens != 1:
    print(f"{mulheres_jovens} mulheres têm menos de 20 anos.")
