#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Sousa
#primeiro= Ana
#último= Sousa

nome= str(input("Digite seu \033[1mnome\033[m: ")).strip()
print(f"Analisando o nome '\033[1m{nome}\033[m', chegamos a conclusão que: " f"\nO primeiro nome de '\033[3m{nome}\033[m' é", nome.split()[0], f"\nO último nome de '\033[3m{nome}\033[m' é", nome.split()[-1])
