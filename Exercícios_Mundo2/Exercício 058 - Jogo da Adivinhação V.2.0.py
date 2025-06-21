#Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
print(f"=" * 61)
print(f"Olá, sou eu de novo: O Computador!\nO que acha de uma revanche daquele nosso jogo de adivinhação?\nVai por mim, está mais fácil pra você agora!")
n_computador= randint(0, 10)
print(f"Pronto. Já escolhi meu número.\nAgora é a sua vez: Escolha um número de 0 a 10:")
n_jogador= 11
tentativas= 0
while n_jogador != n_computador:
    n_valido= 11
    print(f"=" * 61)
    while n_valido < 0 or n_valido > 10:
        n_jogador= int(input(f"Seu número: "))
        if n_jogador < 0 or n_jogador > 10:
            print(f"O número inserido não está no intervalo de 0 a 10.\nTente de novo!")
        else:
            n_valido= n_jogador
    tentativas= tentativas + 1
    print(f"Carregando...")
    sleep(1)

    if n_jogador == n_computador:
        print(f"Parabéns! Você ganhou!\nO número pensado pelo computador foi {n_computador}.\nEu não disse que estava mais fácil agora?\nAté a próxima!")
    elif n_jogador < n_computador:
        print(f"O número pensado pelo Computador é maior que {n_jogador}.\nTente de novo!")
    elif n_jogador > n_computador:
        print(f"O número pensado pelo Computador é menor que {n_jogador}.\nTente de novo!")

if tentativas > 1:
    print(f"Foram necessárias {tentativas} tentativas para que você acertasse!")
else:
    print(f"Foi necessária apenas {tentativas} tentativa para que você acertasse.")
