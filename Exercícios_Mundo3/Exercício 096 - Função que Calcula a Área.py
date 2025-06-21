#Faça um programa que tenha uma função chamada "área()", que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    cal= largura * comprimento
    print(f"Com uma largura de {largura}m e comprimento de {comprimento}m, a área é igual a {cal}m².")

largura= float(input(f"Informe a lagura do terreno em metros: "))
comprimento= float(input(f"Informe o comprimento do terreno em metros: "))
area(largura, comprimento)
