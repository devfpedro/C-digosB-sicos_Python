#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

alt= float(input("Informe a \033[4maltura da da parede:\033[m "))
lar= float(input("Informa a \033[4mlargura da parede:\033[m "))
print(f"A parede possui \033[1m{alt * lar:.1f}m²\033[m. Portanto, serão gastos \033[1m{(alt * lar) / 2:.1f}\033[m litros de tinta.")
