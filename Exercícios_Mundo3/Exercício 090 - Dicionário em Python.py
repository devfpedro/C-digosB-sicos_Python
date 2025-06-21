#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados_aluno= {}
print(f"=" * 40 + f"\n" + f"Dados do(a) Aluno(a)".center(40) + f"\n" + f"=" * 40)
while True:
    dados_aluno['Nome']= str(input("Digite seu nome completo: ").strip())
    while True:
        print(f"-" * 40 + f"\nO nome do(a) aluno(a) '", end= "")
        for nome_aluno in range(0, len(dados_aluno['Nome'])):
            if nome_aluno == 0 or dados_aluno['Nome'][nome_aluno-1] == " ":
                if dados_aluno['Nome'][nome_aluno] in "dD" and dados_aluno['Nome'][nome_aluno-1] == " " and (dados_aluno['Nome'][nome_aluno+2] == " " or dados_aluno['Nome'[nome_aluno+3]] == " "):
                    print(f"{dados_aluno['Nome'][nome_aluno]}".lower(), end= "")
                else:
                    print(f"{dados_aluno['Nome'][nome_aluno]}".upper(), end= "")
            else:
                print(f"{dados_aluno['Nome'][nome_aluno]}".lower(), end= "")
        confirmar= str(input(f"' está correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir seu nome novamente\nSua resposta: ").lower().strip())
        if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Não" or confirmar.capitalize() == "Nao":
            break
        print(f"-" * 40 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if confirmar.capitalize() == "Sim":
        break
    else:
        print(f"-" * 40)
        
while True:
    dados_aluno['Média']= float(input(f"-" * 40 + f"\nDigite sua média: "))
    if dados_aluno['Média'] > 10:
        print(f"-" * 40 + f"\nO sistemas apenas aceita notas que vão de 0 à 10.\nPor favor, tente novamente.")
    else:
        while True:
            confirmar= str(input(f"-" * 40 + f"\nA média '{dados_aluno['Média']}' está correta?\nSim = Confirmar\nNão = Inserir a Média Novamente\nSua resposta: ").lower().capitalize().strip())
            if confirmar == "Sim" or "Não" or "Nao":
                break
            print(f"-" * 40 + f"\nA informação '{confirmar}' não confiz com nenhuma das opções possíveis.\nPor favor, tente novamente.")
        if confirmar == "Sim":
            break
dados_aluno['Situação']= "Aprovado(a)" if dados_aluno['Média'] >= 7.0 else ("Recuperação" if dados_aluno['Média'] >= 4 else f"Reprovado(a)")

print(f"\n" + f"=" * 40 + f"\n" + f"Boletim do(a) Aluno(a)".center(40) + f"\n" + f"=" * 40 + f"\nNome do(a) Aluno(a):")
for nome in range(0, len(dados_aluno['Nome'])):
    if nome < len(dados_aluno['Nome']) - 1:
        if nome == 0 or dados_aluno['Nome'][nome-1] == " ":
            if dados_aluno['Nome'][nome] in "dD" and dados_aluno['Nome'][nome-1] == " " and (dados_aluno['Nome'][nome+2] == " " or dados_aluno['Nome'][nome+3] == " "):
                print(f"{dados_aluno['Nome'][nome]}".lower(), end= "")
            else:
                print(f"{dados_aluno['Nome'][nome]}".upper(), end= "")
        else:
            print(f"{dados_aluno['Nome'][nome]}".lower(), end= "")
    else:
        print(f"{dados_aluno['Nome'][nome]}".lower())
print(f"-" * 40 + f"\nMédia:" + f" " * 20 + f"Situação:")
print(f"{dados_aluno['Média']}" + f" " * (6 - len(str(dados_aluno['Média'])) + 20) + f"{dados_aluno['Situação']}")
