#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print(f"=" * 70)
print(f"Olá de novo! Lembra-se de mim? Sou o Computador!\nO que acha de jogarmos um novo jogo? Desta vez, será 'par ou ímpar'.")
vitorias= 0
vencedor= ""

while True:
    print(f"=" * 70)
    n_jogador= int(input("Escolha um número de 0 a 10: "))
    n_computador= randint(0, 11)

    if n_jogador >= 0 and n_jogador < 11:
        while True:
            print(f"=" * 70)
            e_jogador= str(input(f"Escolha par ou ímpar:\n[P] = Par\n[I] = Ímpar\nSua escolha: ").upper().strip())

            if e_jogador == "P" or e_jogador == "I":
                soma= n_computador + n_jogador
                if soma % 2 == 0:
                    resultado= f"par"
                elif soma % 2 != 0:
                    resultado= f"impar"
                
                if e_jogador == "P" and resultado == "par":
                    print(f"A soma dos números escolhidos foi {soma}.\nO(A) jogador(a) venceu!")
                    vencedor= "jogador"
                elif e_jogador == "I" and resultado == "impar":
                    print(f"A soma dos números foi escolhidos foi {soma}.\nO(A) jogador(a) venceu!")
                    vencedor= "jogador"
                else:
                    print(f"A soma dos números escolhidos foi {soma}.\nO Computador venceu!")
                    vencedor= "computador"
                
                if vencedor == "jogador" or vencedor == "computador":
                    if vencedor == "jogador":
                        vitorias= vitorias + 1
                    break
    
    if vencedor == "computador":
        break

if vitorias == 1:
    print(f"Você venceu {vitorias} vez antes de ser derrotado.")
elif vitorias > 1:
    print(f"Você venceu {vitorias} vezes antes de ser derrotado.")
else:
    print(f"Você não venceu nenhumas vez.")
print(f"Estarei te aguardando para uma revanche.\nAte a próxima!")
