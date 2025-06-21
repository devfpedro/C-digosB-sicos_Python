#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

cateto_oposto= float(input("\033[1mComprimento do cateto opsto:\033[m "))
cateto_adjacente= float(input("\033[1mComprimento do cvateto adjacente:\033[m "))
print(f"Com o cateto oposto sendo \033[3m{cateto_oposto}\033[m e o cateto adjacente sendo \033[3m{cateto_adjacente}\033[m, a hipotenusa será \033[3m{((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2):.2f}\033[m")
