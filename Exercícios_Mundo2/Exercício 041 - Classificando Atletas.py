#A Confedração Nacional de Natação precisa de um programa que leia o ano de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM;
#Até 14 anos: INFANTIL;
#Até 19 anos: JUNIOR;
#Até 25 anos: SÊNIOR;
#Acima: MASTER.

ano_nascimento= int(input("Informe seu ano de nascimento: ").strip())

if ano_nascimento <= 9:
    if ano_nascimento == 1:
        print(f"Como você tem {ano_nascimento} ano, enquadra-se na categoria MIRIM.")
    else:
        print(f"Como você tem {ano_nascimento} anos, enquadra-se na categoria MIRIM.")
elif ano_nascimento <= 14:
    print(f"Como você possui {ano_nascimento} anos, enquadra-se na categoria INFANTIL.")
elif ano_nascimento <= 19:
    print(f"Como você possui {ano_nascimento} anos, enquadra-se na categoria JUNIOR.")
elif ano_nascimento <= 25:
    print(f"Como você possui {ano_nascimento} anos, enquadra-se na categoria SÊNIOR.")
else:
    print(f"Como você possui {ano_nascimento} anos, enquadra-se na catehoria MASTER.")
