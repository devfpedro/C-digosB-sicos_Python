#Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido.

from random import choice
nomes= str(input("\033[3mInsira o nome do primeiro aluno:\033[m ")), str(input("\033[3mInsira o nome do segundo aluno:\033[m ")), str(input("\033[3mInsira o nome do terceiro aluno:\033[m ")), str(input("\033[3mInsira o nome do quarto aluno:\033[m "))
print(f"\033[3mO selecionado para apagar o quadro foi o \033[m\033[1m{choice(nomes)}\033[m!")
