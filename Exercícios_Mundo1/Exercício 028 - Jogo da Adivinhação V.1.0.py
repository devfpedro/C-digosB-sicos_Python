#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido por mim.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero_computador= randint(0, 5)
print(f"Eu, o \033[1mcomputador\033[m, estou pensando em um número entre 0 e 5. Que tal tentar adivinhá-lo?")

numero_usuario= int(input("Qual número acha que o computador escolheu? \033[1;45m\033[m"))
print(f"\033[1;34mProcessando os dados...\033[m\033[m")
sleep(3) #Faz com que o programa aguarde por 3 segundos, antes de apresentar o resultado.

if numero_usuario == numero_computador:
    print(f"\033[1;34mTemos um vencedor!\nO número 'pensado' por mim foi {numero_computador}\033[m.")
else:
    print(f"\033[1;35mParece que você errou. Mais sorte da próxima vez.\nO número pensado por mim foi {numero_computador}\033[m.")

# if numero_usuario >= 0 and numero_usuario <= 5:
#     if numero_usuario == numero_computador:
#         print(f"Temos um vencedor!\nO número 'pensado' por mim foi {numero_computador}.")
#     else:
#         print(f"Parece que você errou. Mais sorte da próxima vez.\nO número pensado por mim foi {numero_computador}.")
# else:
#     print(f"O número que você digitou não consta como uma das possíveis escolhas do computador.\nPossíveis escolhas: 0, 1, 2, 3, 4 e 5.")
