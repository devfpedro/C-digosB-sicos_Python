#Escreva um programa que pergunte a quantidade de Km percforridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

d_alugados= int(input("Por quantos dias o carro será alugado? \033[1m"))
km_percorridos= float(input("\033[0mQuantos quilômetros o carro percorreu?\033[m \033[1m"))
print(f"\033[0mComo o carro será alugado por\033[m \033[2m{d_alugados}\033[m, o aluguel será de \033[4mR${d_alugados * 60:.2f}\033[m. \nE como o carro percorreu \033[1m{km_percorridos}km\033[m, será gasto \033[1mR${km_percorridos * 0.15:.2f}\033[m com a gasolina. \nEntão o total será de \033[1mR${(d_alugados * 60) + (km_percorridos * 0.15):.2f}\033[m.")
