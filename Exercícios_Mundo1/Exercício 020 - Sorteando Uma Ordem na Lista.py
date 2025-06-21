#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle

nome1= str(input("\033[3;33mInsira o nome do primeiro aluno:\033[m "))
nome2= str(input("\033[3;34mInsira o nome do segundo aluno:\033[m "))
nome3= str(input("\033[3;35mInsira o nome do terceiro aluno:\033[m "))
nome4= str(input("\033[3;36mInsira o nome do quarto aluno:\033[m "))
sorteio= [nome1, nome2, nome3, nome4]
shuffle(sorteio)
print(f"A ordem de apresentação será: \033[1m{sorteio}\033[m")
