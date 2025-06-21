#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome= str(input("Digite seu nome: \033[1m")).strip()
print(f"O nome '\033[43m{nome}\033[m' possui o sobrenome 'SILVA'?", f"\n\033[35m{'SILVA' in nome.upper()}\033[m")
