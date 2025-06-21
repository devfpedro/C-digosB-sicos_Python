#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço= float(input("Informe o valor do \033[1mproduto\033[m, para saber o valor do desconto: \033[3mR$"))
print(f"\033[0mO valor do produto com\033[m \033[4mdesconto de 5%\033[m será de \033[1mR${preço - ((preço * 5) / 100):.2f}\033[m")
