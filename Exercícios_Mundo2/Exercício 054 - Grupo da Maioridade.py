#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda ainda não atingiram a maioridade e quantas jã são maiores.
#Considere que a maioridade é 21 anos.

from datetime import date

pessoas_maiores= 0
pessoas_menores= 0
ano_atual= date.today().year

for pessoas in range(1, 8):
  ano_nascimento= int(input(f"Informe o ano de nascimento da {pessoas}ª pessoa: "))

  if ano_nascimento <= (ano_atual - 21):
    pessoas_maiores= pessoas_maiores + 1
  elif ano_nascimento >= (ano_atual - 20):
    pessoas_menores= pessoas_menores + 1

if pessoas_maiores > 1 and pessoas_menores > 1:
  print(f"Ao todo, {pessoas_maiores} pessoas atingiram a maioridade.\nE {pessoas_menores} pessoas são menores de idade.")
elif pessoas_maiores == 1:
  print(f"Apenas {pessoas_maiores} pessoa atingiu a maioridade.\nE {pessoas_menores} pessoas ainda são menores de idade.")
elif pessoas_menores == 1:
  print(f"Ao todo, {pessoas_maiores} pessoas atingiram a maioridade.\nE {pessoas_menores} pessoa ainda é menor de idade.")
elif pessoas_maiores == 0:
  print(f"Nenhuma pessoa atingiu a maioridade.\nE {pessoas_menores} ainda são menores de idade.")
elif pessoas_menores == 0:
  print(f"Ao todo, {pessoas_maiores} pessoas atingiram a maioridade.\nE nenhuma pessoa é menor de idade.")
