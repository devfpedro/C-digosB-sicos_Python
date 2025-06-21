#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo= float(input("Insira o valor do ângulo: \033[1m"))
print(f"\033[0mO ângulo \033[3m{angulo:.1f}°\033[m possui: \nSeno \033[3m{sin(radians(angulo)):.1f}°\033[m \nCosseno \033[3m{cos(radians(angulo)):.1f}°\033[m \nTangente \033[3m{tan(radians(angulo)):.1f}\033[m")
