#Faça um programa que tenha uma função chamada "escreva()", que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adptável.
#Ex: escreva("Olá, Mundo!")
#Saída:
#-------------
# Olá, Mundo!
#-------------

def escreva(txt):
    print((f"=" * (len(txt) + 2)) + f"\n", end= " ")
    for text in range(0, len(txt)):
        if text == 0 or txt[text-1] == " ":
            if txt[text] in "dD" and txt[text-1] == " " and (txt[text+2] == " " or txt[text+3] == " "):
                print(f"{txt[text]}".lower(), end= "")
            else:
                print(f"{txt[text]}".upper(), end= "")
        else:
            print(f"{txt[text]}".lower(), end= "")
    print(f"\n" + (f"=" * (len(txt) + 2)))

escreva(str(input(f"Digite uma mensagem qualquer: ").strip()))
