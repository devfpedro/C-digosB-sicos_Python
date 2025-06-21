#Refaça o Desafio 061, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

p_termo= int(input("Digite o primeiro termo da PA: "))
razão= int(input("Informe a razão da PA: "))
guardar_termo= 0

while guardar_termo < 10:
    if guardar_termo < 8:
        print(f"{p_termo}, ", end= "")
    elif guardar_termo < 9:
        print(f"{p_termo}", end= "")
    else:
        print(f" e {p_termo}.", end= "")
    p_termo= p_termo + razão
    guardar_termo= guardar_termo + 1
