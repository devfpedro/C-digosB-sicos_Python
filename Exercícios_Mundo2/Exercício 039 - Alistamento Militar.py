#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou o tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
#Adição (colocada no vídeo de resolução do desafio): Pedir que o usuário informe seu gênero - Masculino ou Feminino - e informe se ele(a) tem o dever de se alista ou não.

print(f"Todo jovem do sexo masculino deve se alistar aos 18 anos de idade.")

genero= str(input("Primeiro, informe seu gênero de nascimento (Masculino ou Feminino): ").upper().strip())

if genero == "MASCULINO" or genero == "FEMININO":
    if genero == "MASCULINO":
        print(f"Você é do sexo masculino. Portanto, tem o dever de se alistar aos 18 anos de idade.")
    elif genero == "FEMININO":
        print(f"Você é do sexo feminino. Portanto, não possui o dever de se alistar aos 18 anos.\nPorém, ainda pode se alistar, se assim o quiser.")
        opçao_feminina= str(input("Você deseja se alistar? Digite uma das opções:\n'Sim' = Quero me alistar!\n'Não' = Não quero me alistar.\nDigite: ").upper().strip())
        if opçao_feminina != "SIM" or opçao_feminina != "NÃO":
            print(f"As informações concedidas não estão condizentes com nenhumas das opções.\nPor favor, preencha as informações novamente, seguindo as instruções concedidas.")
    
    if genero == "MASCULINO" or opçao_feminina == "SIM":
        ano_nascimento= int(input("Informe o ano em que você nasceu: ").strip())
        if ano_nascimento == 2024:
            print(f"Você tem 1 ano de idade.")
        elif ano_nascimento < 2024:
            print(f"Você tem {2025 - ano_nascimento} anos de idade.")

        if ano_nascimento >= 2008:
            print(f"Você ainda vai se alistar ao serviço militar quando completar 18 anos.")
            anos_restantes= 2025 - ano_nascimento
            if (18 - anos_restantes) >= 2:
                print(f"Faltam {18 - anos_restantes} anos para você se alistar.")
            else:
                print(f"Falta apenas 1 ano para você se alistar.")
        elif ano_nascimento == 2007:
            print(f"É o momento de se alistar!")
        elif ano_nascimento <= 2006:
            print(f"Já passou da idade de se alistar.")
            if 2007 - ano_nascimento == 1:
                print(f"Você deveria ter se alistado há 1 ano atrás.")
            else:
                print(f"Você deveria ter se alistado há {2007 - ano_nascimento} anos atrás.")
else:
    print(f"As informações concedidas não estão condizentes com nenhumas das opções.\nPor favor, preencha as informações novamente, seguinto as instruções concedidas.")
