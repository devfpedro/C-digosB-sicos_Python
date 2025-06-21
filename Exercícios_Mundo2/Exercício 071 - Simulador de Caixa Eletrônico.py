#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número a ser sacado) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(f"=" * 50)
print(f"Bem-Vindo(a) ao Banco PH".center(49))
print(f"=" * 50)
while True:
    saque= int(input("Informe o valor que deseja sacar: R$"))
    if saque >= 1:
        break
    else:
        print(f"Para sacar qualquer valor, a quantidade tem de ser maior que R$00,99.\nPor favor, tente novamente.")
print(f"=" * 50)
print(f"Ao sacar o valor de R${saque:.2f}, você receberá:" + f"\n")

if saque // 50 > 0:
    div_50= saque // 50
    saque= saque - (div_50 * 50)
else:
    div_50= 0
    
if saque // 20 > 0:
    div_20= saque // 20
    saque= saque - (div_20 * 20)
else:
    div_20= 0

if saque // 10 > 0:
    div_10= saque // 10
    saque= saque - (div_10 * 10)
else:
    div_10= 0

if saque // 1 > 0:
    div_1= saque // 1
    saque= saque - (div_1 * 1)
else:
    div_1= 0

if div_50 == 1:
    print(f"{int(div_50)} nota de R$50,00")
elif div_50 != 1:
    print(f"{int(div_50)} notas de R$50,00")

if div_20 == 1:
    print(f"{int(div_20)} nota de R$20,00")
elif div_20 != 1:
    print(f"{int(div_20)} notas de R$20,00")

if div_10 == 1:
    print(f"{int(div_10)} nota de R$10,00")
elif div_10 != 1:
    print(f"{int(div_10)} notas de R$10,00")

if div_1 == 1:
    print(f"{int(div_1)} nota de R$1,00")
elif div_1 != 1:
    print(f"{int(div_1)} notas de R$1,00")
print(f"_" * 50)
