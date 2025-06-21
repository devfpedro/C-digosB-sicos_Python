#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade= float(input("A quantos Km/h o carro estava se movendo? \033[1m"))

if velocidade > 80.0:
    print("\033[1;33mVocê ultrapassou o limite de velocidade permitido. Você será multado!\033[m")
    print(f"A multa custará \033[3mR${float((velocidade - 80) * 7):.2f}\033[m")
else:
    print("\033[4mVocê obedeceu o limite de velocidade. Pode seguir em frente.\033[m")

print(f"\033[1mTenha um bom dia! E diriga com segurança!\033[m")
