#Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#a) Quantas pessoas foram cadastradas.
#b) A média de idade do grupo.
#c) Uma lista com todas as mulheres.
#d) Uma lista com todas as pessoas com idade acima da média.

grupo= []
pessoas= {}

cont_pessoa= 0
while True:
    print(f"=" * 65 + f"\n" + f"Preencher Dados".center(65) + f"\n" + f"=" * 65)

    cont_pessoa= cont_pessoa + 1
    while True:
        pessoas['Nome da pessoa']= str(input(f"Informe o nome da {cont_pessoa}° pessoa: ").strip())
        caractere_num= "Não"
        for num in range(0, len(pessoas['Nome da pessoa'])):
            if pessoas['Nome da pessoa'][num] in "0123456789/?:;.>,<~^`´}]{[ª°º\|!@#$%¨&*)(_-+=§'":
                caractere_num= "Sim"
        if caractere_num == "Sim":
            print(f"-" * 65 + f"\nNome de pessoa não pode possuir números ou caracteres especiais.\nPor favor, tente novamente.")
        else:
            while True:
                print(f"-" * 65 + f"\nO nome '", end= "")
                for conf_nome in range(0, len(pessoas['Nome da pessoa'])):
                    if conf_nome == 0 or pessoas['Nome da pessoa'][conf_nome-1] == " ":
                        if pessoas['Nome da pessoa'][conf_nome] in "dD" and pessoas['Nome da pessoa'][conf_nome-1] == " " and (pessoas['Nome da pessoa'][conf_nome+2] == " " or pessoas['Nome da pessoa'][conf_nome+3] == " "):
                            print(f"{pessoas['Nome da pessoa'][conf_nome]}".lower(), end= "")
                        else:
                            print(f"{pessoas['Nome da pessoa'][conf_nome]}".upper(), end= "")
                    else:
                        print(f"{pessoas['Nome da pessoa'][conf_nome]}".lower(), end= "")
                confirmar= str(input(f"' está correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir o nome novamente\nSua resposta: ").lower().strip())
                if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Não" or confirmar.capitalize() == "Nao":
                    break
                print(f"-" * 65 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
            if confirmar.capitalize() == "Sim":
                break
        
    while True:
        pessoas['Sexo da pessoa']= str(input(f"-" * 65 + f"\nInforme seu sexo digitando uma das opções:\nMasculino / Feminino\nSua resposta: ").lower().strip())
        caractere_num= "Não"
        for num in range(0, len(pessoas['Sexo da pessoa'])):
            if pessoas['Sexo da pessoa'][num] in "0123456789/?:;.>,<~^`´}]{[ª°º\|!@#$%¨&*)(_-+=§'":
                caractere_num= "Sim"
        if caractere_num == "Sim":
            print(f"-" * 65 + f"\nSexo de pessoa não pode possuir números ou caracteres especiais.\nPor favor, tente novamente.")
        elif pessoas['Sexo da pessoa'].capitalize() == "Feminino" or pessoas['Sexo da pessoa'].capitalize() == "Masculino":
            while True:
                print(f"-" * 65 + f"\nO sexo '", end= "")
                for conf_sexo in range(0, len(pessoas['Sexo da pessoa'])):
                    if conf_sexo == 0 or pessoas['Sexo da pessoa'][conf_sexo-1] == " ":
                        print(f"{pessoas['Sexo da pessoa'][conf_sexo]}".upper(), end= "")
                    else:
                        print(f"{pessoas['Sexo da pessoa'][conf_sexo]}".lower(), end= "")
                confirmar= str(input(f"' informado está correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir o sexo novamente\nSua resposta: ").lower().strip())
                if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                    break
                print(f"-" * 65 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
            if confirmar.capitalize() == "Sim":
                break
        else:            
            print(f"-" * 65 + f"\nA informação '{pessoas['Sexo da pessoa']}' não condiz com nenhuma das opções possíveis.\nPor favor, tente novamente.")
    
    while True:
        pessoas['Idade da pessoa']= str(input(f"-" * 65 + f"\nInforme a idade da {cont_pessoa}° pessoa: "))
        letra= "Não"
        for car in range(0, len(pessoas['Idade da pessoa'])):
            if (pessoas['Idade da pessoa'][car]).lower() in "abcçdefghijklmnopqrstuvwxyz/?:;.>,<~^`´}]{[ª°º\|!@#$%¨&*)(_-+=§'":
                letra= "Sim"
        if letra == "Sim":
            print(f"-" * 65 + f"\nIdade não pode possuir letras ou caraceteres especiais.\nPor favor, tente novamente.")
        else:
            while True:
                confirmar= str(input(f"-" * 65 + f"\nA idade de {pessoas['Idade da pessoa']} " + (f"anos" if int(pessoas['Idade da pessoa']) > 1 else f"ano") + f" está correta?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir a idade novamente\nSua resposta: ").lower().strip())
                if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Nao" or confirmar.capitalize() == "Não":
                    break
                print(f"A informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
            if confirmar.capitalize() == "Sim":
                pessoas['Idade da pessoa']= int(pessoas['Idade da pessoa'])
                break
    
    grupo.append(pessoas.copy())

    while True:
        cont= str(input(f"-" * 65 + f"\nVocê deseja inserir os dados de mais uma pessoa?\nDigite 'Sim' para Continuar\nDigite 'Não' para Encerrar\nSua reposta: ").lower().strip())
        if cont.capitalize() == "Sim" or cont.capitalize() == "Não" or cont.capitalize() == "Nao":
            print()
            break
        print(f"-" * 65 + f"\nA informação '{cont}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if cont.capitalize() in "NãoNao":
        break

print(f"=" * 65 + f"\n" + f"Dados Adquiridos".center(65) + f"\n" + f"=" * 65)
print(f"N° de Pessoas Cadastradas: {len(grupo)}\n" + f"\n" + f"-" * 65)
soma= 0
for media in range(0, len(grupo)):
    soma= soma + grupo[media]['Idade da pessoa']
print(f"Média de Idade do Grupo: {int(soma / len(grupo))} " + (f"anos" if int(soma / len(grupo)) > 1 else "ano") + f"\n" + f"\n" + f"-" * 65)
t_mulheres= 0
for mulheres in range(0, len(grupo)):
    if grupo[mulheres]['Sexo da pessoa'].capitalize() == "Feminino":
        t_mulheres= t_mulheres + 1
print(f"Mulheres no Grupo:")
if t_mulheres > 0:
    for saida_mulheres in range(0, len(grupo)):
        if grupo[saida_mulheres]['Sexo da pessoa'].capitalize() == "Feminino":
            print(f"> ", end= "")
            for nome_mulher in range(0, len(grupo[saida_mulheres]['Nome da pessoa'])):
                if nome_mulher == 0 or grupo[saida_mulheres]['Nome da pessoa'][nome_mulher-1] == " ":
                    if grupo[saida_mulheres]['Nome da pessoa'][nome_mulher] in "dD" and grupo[saida_mulheres]['Nome da pessoa'][nome_mulher-1] == " " and (grupo[saida_mulheres]['Nome da pessoa'][nome_mulher+2] == " " or grupo[saida_mulheres]['Nome da pessoa'][nome_mulher+3] == " "):
                        print(f"{grupo[saida_mulheres]['Nome da pessoa'][nome_mulher]}".lower(), end= "")
                    else:
                        print(f"{grupo[saida_mulheres]['Nome da pessoa'][nome_mulher]}".upper(), end= "")
                else:
                    if nome_mulher < len(grupo[saida_mulheres]['Nome da pessoa']) - 1:
                        print(f"{grupo[saida_mulheres]['Nome da pessoa'][nome_mulher]}".lower(), end= "")
                    else:
                        print(f"{grupo[saida_mulheres]['Nome da pessoa'][nome_mulher]}")
            if t_mulheres == 1:
                print(f"\n" + f"-" * 65)
            t_mulheres= t_mulheres - 1
else:
    print(f"> Nenhuma mulher foi registrada no grupo\n" + f"\n" + f"-" * 65)

soma_idade= 0
for media_idade in range(0, len(grupo)):
    if grupo[media_idade]['Idade da pessoa'] > int(soma / len(grupo)):
        soma_idade= soma_idade + 1
print(f"Pessoas com Idades Acima da Média de Idade do Grupo:")
if soma_idade > 0:
    for idade in range(0, len(grupo)):
        if grupo[idade]['Idade da pessoa'] > int(soma / len(grupo)):
            print(f"> ", end= "")
            for mais_velho in range(0, len(grupo[idade]['Nome da pessoa'])):
                if mais_velho == 0 or grupo[idade]['Nome da pessoa'][mais_velho-1] == " ":
                    if grupo[idade]['Nome da pessoa'][mais_velho] in "dD" and grupo[idade]['Nome da pessoa'][mais_velho-1] == " " and (grupo[idade]['Nome da pessoa'][mais_velho+2] == " " or grupo[idade]['Nome da pessoa'][mais_velho+3] == " "):
                        print(f"{grupo[idade]['Nome da pessoa'][mais_velho]}".lower(), end= "")
                    else:
                        print(f"{grupo[idade]['Nome da pessoa'][mais_velho]}".upper(), end= "")
                else:
                    if mais_velho < len(grupo[idade]['Nome da pessoa']) - 1:
                        print(f"{grupo[idade]['Nome da pessoa'][mais_velho]}".lower(), end= "")
                    else:
                        print(f"{grupo[idade]['Nome da pessoa'][mais_velho]}".lower())
            soma_idade= soma_idade - 1
            if soma_idade == 0:
                print(f"\n" + f"-" * 65)
else:
    print(f"> Não há pessoas com idade superior a média de idade do grupo\n" + f"\n" + f"-" * 65)
