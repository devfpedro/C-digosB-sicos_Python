#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (considerando que isso acontecerá depois de 35 anos de contribuição - quando a sua carteira de trabalho foi assinada).

from datetime import date
from time import sleep

info_trabalhador= {}

print(f"=" * 50 + f"\n" + f"\033[1m Dados do(a) Trabalhador(a) \033[m".center(57))
while True:
    print(f"=" * 50 if len(info_trabalhador) == 0 else f"-" * 50)
    info_trabalhador['Nome']= str(input("Digite seu nome completo: ").strip())
    print(f"-" * 50 + f"\nO nome '", end= "")
    for nome in range(0, len(info_trabalhador['Nome'])):
        if nome == 0 or info_trabalhador['Nome'][nome-1] == " ":
            if info_trabalhador['Nome'][nome] in "dD" and info_trabalhador['Nome'][nome-1] == " " and (info_trabalhador['Nome'][nome+2] == " " or info_trabalhador['Nome'][nome+3] == " "):
                print(f"{info_trabalhador['Nome'][nome]}".lower(), end= "")
            else:
                print(f"{info_trabalhador['Nome'][nome]}".upper(), end= "")
        else:
            if nome < len(info_trabalhador['Nome']) - 1:
                print(f"{info_trabalhador['Nome'][nome]}".lower(), end= "")
            else:
                print(f"{info_trabalhador['Nome'][nome]}' está correto?".lower())
    while True:
        confirmar= str(input(f"Digite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente seu nome\nSua resposta: ").lower().strip())
        if confirmar.capitalize() in "SimNaoNão":
            break
        print(f"-" * 50 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if confirmar.capitalize() == "Sim":
        break

while True:
    info_trabalhador['Idade']= date.today().year - int(input(f"-" * 50 + f"\nInforme seu ano de nascimento: "))
    while True:
        confirmar= str(input(f"Sua idade é {info_trabalhador['Idade']} " + (f"anos" if info_trabalhador['Idade'] > 1 else f"ano") + f", correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente seu ano de nascimento\nSua resposta: ").lower().strip())
        if confirmar.capitalize() in "SimNaoNâo":
            break
        print(f"-" * 50 + f"\nA informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
    if confirmar.capitalize() == "Sim":
        break

while True:
    info_trabalhador['N° Carteira de Trabalho']= int(input(f"-" * 50 + f"\nInforme o N° (Número) da sua Carteira de Trabalho.\nCaso não possua Carteira de Trabalho, digite '0'.\nN° Carteira de Trabalho: "))
    if len(str(info_trabalhador['N° Carteira de Trabalho'])) == 11 or info_trabalhador['N° Carteira de Trabalho'] == 0:
        while True:
            confirmar= str(input(f"-" * 50 + (f"\nO N° '{info_trabalhador['N° Carteira de Trabalho']}' está correto?" if info_trabalhador['N° Carteira de Trabalho'] != 0 else f"\nSabendo das informações previamente repassadas, você confirma, ao digitar '{info_trabalhador['N° Carteira de Trabalho']}', que não possui Carteira de Trabalho?") + f"\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente.\nSua resposta: ").lower().capitalize())
            if confirmar.capitalize() in "SimNaoNão":
                break
            print(f"-" * 50 + f"A informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
        if confirmar.capitalize() == "Sim":
            break
    print(f"-" * 50 + (f"\nO N° da Carteira de Trabalho é composto por 11 digitos.\nPor favor, tente novamente." if info_trabalhador['N° Carteira de Trabalho'] != 0 else f"\nPrepare-se para informar o N° da sua Carteira de Trabalho."))

if info_trabalhador['N° Carteira de Trabalho'] != 0:
    while True:
        info_trabalhador['Ano de Contratação']= int(input(f"-" * 50 + f"\nInforme seu ano de contratação: "))
        while True:
            confirmar= str(input(f"-" * 50 + f"\nO ano de contratação '{info_trabalhador['Ano de Contratação']}' está correto?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente o ano de contratação\nSua resposta: ").lower().strip())
            if confirmar.capitalize() in "SimNaoNão":
                break
            print(f"-" * 50 + f"A informação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
        if confirmar.capitalize() == "Sim":
            break

    while True:
        info_trabalhador['Salário']= float(input(f"-" * 50 + f"\nInforme seu salário: R$"))
        while True:
            confirmar= str(input(f"-" * 50 + f"\nVocê confirma que R${info_trabalhador['Salário']:.2f} foi o seu primeiro salário em um trabalho de carteira assinada?\nDigite 'Sim' para Confirmar\nDigite 'Não' para inserir novamente\nSua resposta: ").lower().strip())
            if confirmar.capitalize() in "SimNaoNão":
                break
            print(f"-" * 50 + f"A inforamação '{confirmar}' não está entre as opções disponiveis.\nPor favor, tente novamente.")
        if confirmar.capitalize() == "Sim":
            break

    info_trabalhador['Ano de Aposentadoria']= info_trabalhador['Idade'] + 35 - (date.today().year - info_trabalhador['Ano de Contratação'])    

print(f"=" * 50)
print(f"\033[1m Dados do(a) Trabalhador(a) \033[m".center(57) if info_trabalhador['N° Carteira de Trabalho'] > 0 else f"\033[1m Dados da Pessoa \033[m".center(57))
sleep(1)
print(f"-" * 50 + f"\nNome Completo: ", end= "")
sleep(1)
for nome in range(0, len(info_trabalhador['Nome'])):
    if nome == 0 or info_trabalhador['Nome'][nome-1] == " ":
        if info_trabalhador['Nome'][nome] in "dD" and info_trabalhador['Nome'][nome-1] == " " and (info_trabalhador['Nome'][nome+2] == " " or info_trabalhador['Nome'][nome+3] == " "):
            print(f"{info_trabalhador['Nome'][nome]}".lower(), end= "")
        else:
            print(f"{info_trabalhador['Nome'][nome]}".upper(), end= "")
    else:
        if nome < len(info_trabalhador['Nome']) - 1:
            print(f"{info_trabalhador['Nome'][nome]}".lower(), end= "")
        else:
            print(f"{info_trabalhador['Nome'][nome]}".lower())
sleep(1)
print(f"Idade: {info_trabalhador['Idade']} " + (f"anos" if info_trabalhador['Idade'] > 1 else f"ano"))
sleep(1)
print(f"N° Carteira de Trabalho: "  + (f"{info_trabalhador['N° Carteira de Trabalho']}" if info_trabalhador['N° Carteira de Trabalho'] != 0 else f"NÃO POSSUI"))
sleep(1)
if info_trabalhador['N° Carteira de Trabalho'] != 0:
    print(f"Ano de Contratação: {info_trabalhador['Ano de Contratação']}")
    sleep(1)
    print(f"Salário: R${info_trabalhador['Salário']:.2f}")
    sleep(1)
    print(f"Ano de Aposentadoria: {date.today().year + 35 - (date.today().year - info_trabalhador['Ano de Contratação'])}, com {info_trabalhador['Ano de Aposentadoria']} anos")
print()
