#Escreva um programa que leia um valor em metros e a exiba convertida em quilômetro, hectômetro, decâmetro, decímetro, centímetro e milímetro.

metros= float(input("Insira a quantidade de metros: \033[1m"))
print(f"\033[0mO valor de\033[m \033[1m{metros}\033[m metros em quilômetros é: \033[3m{metros / 1000}\033[m. \nO valor de \033[1m{metros}\033[m metros em hectômetros é: \033[33m{metros / 100}\033[m. \nO valor de \033[1m{metros}\033[m metros em decâmetros é: \033[35m{metros / 10}\033[m. \nO valor de \033[1m{metros}\033[m metros em dedímetros é: \033[32m{metros * 10}\033[m. \nO valor de \033[1m{metros}\033[m metros em centímetros é: \033[32m{metros * 100}\033[m. \nO valor de \033[1m{metros}\033[m metros em milímetros é: \033[33m{metros * 1000}\033[m.")
