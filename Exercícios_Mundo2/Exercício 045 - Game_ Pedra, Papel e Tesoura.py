#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print(f"Olá. Sou o computador.\nE lhe desafio para uma partida de Jokenpô! Ou pedra, papel e tesoura, como é mais conhecido.\nBastar escolher uma das opções: 'Pedra', 'Papel' ou 'Tesoura'.\nVamos ver quem ganha!")

escolha_jogador= str(input("Escolha 'Pedra', 'Papel' ou 'Tesoura': ").strip().upper())
opçoes_computador= ("PEDRA", "PAPEL", "TESOURA")
escolha_computador= choice(opçoes_computador)

print(f"JO")
sleep(1)
print(f"KEN")
sleep(1)
print(f"PÔ!")
sleep(1)

if escolha_jogador == "PEDRA" and escolha_computador == "PEDRA":
    print(f"A escolha de ambos foi a mesma: Pedra.\nÉ um empate!")
elif escolha_jogador == "PEDRA" and escolha_computador == "PAPEL":
    print(f"Você, jogador(a), escolheu pedra. O computador escolheu papel.\nO computador venceu!")
elif escolha_jogador == "PEDRA" and escolha_computador == "TESOURA":
    print(f"Você, jogador(a), escolheu pedra. O computador escolheu tesoura.\nO(A) jogador(a) venceu!")
elif escolha_jogador == "PAPEL" and escolha_computador == "PEDRA":
    print(f"Você, jogador(a), escolheu papel. O computador escolheu pedra.\nO(A) jogador(a) venceu!")
elif escolha_jogador == "PAPEL" and escolha_computador == "PAPEL":
    print(f"A escolha de ambos foi a mesma: Pedra.\nÉ um empate!")
elif escolha_jogador == "PAPEL" and escolha_computador == "TESOURA":
    print(f"Você, jogador(a), escolheu papel. O computador escolheu tesoura.\nO computador venceu!")
elif escolha_jogador == "TESOURA" and escolha_computador == "PEDRA":
    print(f"Você, jogador(a), escolheu tesoura. O computador escolheu pedra.\nO computador venceu!")
elif escolha_jogador == "TESOURA" and escolha_computador == "PAPEL":
    print(f"Você, jogador(a), escolheu tesoura. O computador escolheu papel.\nO(A) jogador(a) venceu!")
elif escolha_jogador == "TESOURA" and escolha_computador == "TESOURA":
    print(f"A escola de ambos foi a mesma: Tesoura.\nÉ um empate!")
else:
    print(f"Você não escolheu nenhuma das opções possíveis para participar do jogo.\nReinicie o programa e escolha uma das opções: 'Pedra', 'Papel' ou 'Tesoura'.")
