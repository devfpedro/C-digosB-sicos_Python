#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maísculas;
#O nome com todas minúsculas;
#Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome.

nome= str(input("Informe seu nome: ")).strip()
print(f"O nome '\033[1m{nome}\033[m' está sendo analizado...", f"\nO nome todo maísculo é: \033[3;34m{nome.upper()}\033[m\nO nome todo minúsculo é: \033[3;34m{nome.lower()}\033[m", f"\nO nome '\033[1m{nome}\033[m' possui",len(nome) - nome.count(" "),"letras" f"\nO primeiro nome (\033[3;35m{nome.split()[0]}\033[m) possui \033[1;36m{len(nome.split()[0])}\033[m letras")
