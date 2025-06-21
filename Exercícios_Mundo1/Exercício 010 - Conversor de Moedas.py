#Crie um programa que leia quanto dinheiro uma pessoa tem na certeira e mostre quantos dólares ela pode comprar.
#Considere US$1.00 = R$5.67 (Valor atual - 2024)

din= float(input("Informe quanto dinheiro possui: \033[1mR$"))
con= din / 5.67
print(f"\033[0mVocê pode comprar, com \033[1;34mR${din:.2f}\033[m, até \033[1;33mUS${con:.2f}\033[1;35m.")
