#Faça um programa que tenha uma função chamada "contador()", que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens atráves da função criada:
#a)De 1 até 10, de 1 em 1;
#b)De 10 até 0, de 2 em 2; 
#c)Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    print((f"=" * 70) + f"\nContagem de {inicio} até {fim} de {passo if passo != 0 else 1} em {passo if passo != 0 else 1}: ", end= "")
    if passo == 0:
        passo= 1
    elif passo < 0:
        passo= passo * -1
    sleep(2)
    q_cont= 0
    for contagem in range(inicio, (fim+1 if fim > inicio else fim-1), (-(passo) if inicio > fim else passo)):
        if inicio < fim:
            if q_cont == 0:
                for conf in range(inicio, fim+1, passo):
                    q_cont= q_cont + 1
            sleep(0.5)
            print(f"{contagem}, " if q_cont > 2 else f"{contagem} e " if q_cont == 2 else f"{contagem}.", end= "" if q_cont > 1 else f"\n", flush= True)
            q_cont= q_cont - 1
        else:
            if q_cont == 0:
                for conf in range(inicio, fim-1, -(passo)):
                    q_cont= q_cont + 1
            sleep(0.5)
            print(f"{contagem}, " if q_cont > 2 else f"{contagem} e " if q_cont == 2 else f"{contagem}.", end= "" if q_cont > 1 else f"\n", flush= True)
            q_cont= q_cont - 1

contador(1, 10, 1)
contador(10, 0, 2)
print((f"=" * 70) + f"\nAgora, informe os valores da contagem personalizada:\n" + (f"-" * 70))
contador(int(input("Início (Primeiro N° da Contagem): ")), int(input("Fim (Último N° da Contagem): ")), int(input("Passo (Sequência Númerica): ")))
print(f"=" * 70)
