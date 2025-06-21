#Crie um programa que tenha uma função chamada "voto()", que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto "NEGADO", "OPCIONAL" ou "OBRIGATÓRIO" nas eleições.

from datetime import date

def confirmação(info):
    while True:
        confirmar= str(input((f"=" * 40) + f"\nA resposta '{info}', como seu ano de nascimento, está correta?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir Novamente\nSua reposta: ").lower().strip())
        if confirmar.capitalize() == "Sim" or confirmar.capitalize() == "Não" or confirmar.capitalize() == "Nao":
            if confirmar.capitalize() == "Não" or confirmar.capitalize() == "Nao":
                info= int(input((f"=" * 40) + f"\nInforme seu ano de nascimento: "))
            else:
                break
        else:
            print((f"=" * 40) + f"\nA informação '{confirmar}' não corresponde a nehuma das opções possíveis.\nPor favor, tente novamente.")
    return info

def voto(nascimento):
    idade= date.today().year - nascimento
    if idade == 16 or idade == 17 or idade > 65:
        r= f"Com {idade} anos, o seu voto é opcional."
    elif idade >= 18 and idade <= 65:
        r= f"Com {idade} anos, o seu voto é obrigatório."
    elif idade <= 15:
        r= f"Com {idade} " + (f"anos" if idade > 1 else f"ano") + f", você não precisa votar."
    return print((f"=" * 40) + f"\n{r}")

voto(confirmação(int(input((f"=" * 40) + f"\nInforme seu ano de nascimento: "))))
