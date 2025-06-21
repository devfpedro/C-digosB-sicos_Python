#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso= 0
maior_p= []
menor_p= []

for pessoas in range(1, 6):
  p_ant= peso
  peso= float(input(f"Informe o peso da {pessoas}ª pessoa (em Kg): "))

  maior_p.append(peso)
  menor_p.append(peso)

for maior in range(5):
  if maior_p[0] > maior_p[-1]:
    maior_p.pop(-1)
  elif maior_p[-1] > maior_p[0]:
    maior_p.pop(0)

for menor in range(5):
  if menor_p[0] < menor_p[-1]:
    menor_p.pop(-1)
  elif menor_p[-1] < menor_p[0]:
    menor_p.pop(0)

print(f"O maior peso informado foi {maior_p[-1]}Kg\nO menor peso informado foi {menor_p[-1]}Kg")
