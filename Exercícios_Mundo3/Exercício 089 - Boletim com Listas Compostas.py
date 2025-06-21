#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

dados= []
info_aluno= []
notas= []
nome_completo= []

cont_alunos= 0
while True:
    cont_alunos= cont_alunos + 1
    info_aluno.append(cont_alunos)
    nome_aluno= str(input("Informe o nome completo do(a) aluno(a): ").lower().strip())
    info_aluno.append(nome_aluno[:])
    soma_n= 0
    for t_n in range(1, 3):
        info_notas= float(input(f"Informe a {t_n}° nota: "))
        notas.append(info_notas)
        soma_n= soma_n + info_notas
    info_aluno.append(soma_n / 2)
    info_aluno.append(notas[:])
    dados.append(info_aluno[:])
    info_aluno.clear()
    notas.clear()

    while True:
        cont= str(input(f"Deseja continuar inserindo dados de alunos?\nDigite 'Sim' -> Continuar\nDigite 'Não' -> Finalizar\nSua resposta: ").strip())
        if cont.lower() == "sim" or cont.lower() == "não" or cont.lower() == "nao":
            break
        print(f"A informação '{cont}' não condiz com nenhuma das opções possíveis.\nPor favor, tente novamente.")
    if cont.lower() == "não" or cont.lower() == "nao":
        break

q_letras= 0
for m_nome in range(0, len(dados)):
    soma= 0
    for m_nome1 in range(0, len(dados[m_nome][1])):
        soma= soma + 1
    if soma > q_letras:
        q_letras= soma

cal_form= len("N° Registrado: ") + len(str(cont_alunos)) + 5 + (len("Nome Completo:") if len("Nome Completo:") > q_letras else q_letras) + 5 + 11
sleep(1)
print(f"=" * cal_form)
print(f"Boletim dos Alunos".center(cal_form) if cont_alunos > 1 else "Boletim do(a) Aluno(a)".center(cal_form))
print(f"=" * cal_form)
print(f"Cadastro:".ljust((len("N° Registrado: ") + len(str(cont_alunos)) + 5)) + f"Nome Completo:".ljust((len("N° Registrado:") if len("N° Registrado") > q_letras else q_letras) + 5) + f"Média:")
for nomes in range(0, len(dados)):
    print(f"N° Registrado: {dados[nomes][0]}".ljust((len("N° Registrado: ") + len(str(cont_alunos)) + 5)), end= "")
    for nomes1 in range(0, len(dados[nomes][1])):
        if nomes1 < len(dados[nomes][1]) - 1:
            print(dados[nomes][1][nomes1].capitalize() if nomes1 == 0 or dados[nomes][1][nomes1-1] == " " else dados[nomes][1][nomes1], end= "")
        else:
            print(f"{dados[nomes][1][nomes1]}", end= "")
    if len(dados[nomes][1]) == q_letras and (len("Nome Completo:") < q_letras or len("Nome Completo:") == q_letras):
        print(f" " * + 5, end= "")
    elif len("Nome Completo:") < len(dados[nomes][1]) < q_letras:
        print(f" " * (((q_letras - len(dados[nomes][1])) + 5)), end="")
    elif len(dados[nomes][1]) < len("Nome Completo:"):
        print(f" " * ((q_letras - len(dados[nomes][1])) + 5), end= "")
    elif len("Nome Completo:") == len(dados[nomes][1]) or len("Nome Completo:") == q_letras:
        print(f" " * ((q_letras - len(dados[nomes][1])) + 5), end= "")
    print(f"{dados[nomes][2]:.1f}")

sleep(1)
while True:
    print(f"=" * cal_form)
    print(f"Siga as instruções abaixo para conferir as notas dos alunos." if cont_alunos > 1 else "Siga as instruções abaixo para conferir as notas do(a) aluno(a).")
    conf_notas= str(input(f"Para encerrar, digite 'Sair'.\nInforme o Nome Completo do(a) Aluno(a) ou seu Cadastro (N° de Registro): ").lower().strip())
    print("=" * cal_form)
    sleep(1)

    if conf_notas.upper() != "SAIR":
        if conf_notas[0] in "0123456789":
            print(f"Confirme se o N° de Cadastro '{conf_notas}", end="")
        else:
            print(f"Confirme se o Nome do(a) Aluno(a) '", end= "")
            for nome in range(0, len(conf_notas)):
                if nome == 0 or conf_notas[nome-1] == " ":
                    print(f"{conf_notas[nome]}".upper(), end= "")
                else:
                    print(f"{conf_notas[nome]}".lower(), end= "")
        print(f"' está correto.")

        while True:
            confirmar= str(input(f"Digite 'Sim' para Confirmar.\nDigite 'Não' para Inserir Novamente a Informação.\nSua resposta: ").strip())
            sleep(1)
            if confirmar.upper() in "SIM" or confirmar.upper() in "NAONÃO":
                print(f"=" * cal_form)
                print(f"Carregando Informações...\n" if confirmar.upper() in "SIM" else "Prepare-se para Preencher as Informações Novamente...", end= "")
                print(f"=" * cal_form if confirmar.upper() in "SIM" else "")
                sleep(1)
                break
            print(f"A informação '{confirmar}' não corresponde a nenhuma das opções possíveis.\nPor favor, tente novamente.")

        if confirmar.upper() == "SIM":
            if conf_notas[0] in "0123456789":
                conf_notas= int(conf_notas)
                for conf_aluno in range(0, len(dados)):
                    if conf_notas == dados[conf_aluno][0]:
                        print(f"Nome:" + f"Notas:".rjust(cal_form - 10))
                        for nome_notas in range(0, len(dados[conf_aluno][1])):
                            if nome_notas == 0 or dados[conf_aluno][1][nome_notas-1] == " ":
                                print(f"{dados[conf_aluno][1][nome_notas]}".upper(), end= "")
                            else:
                                print(f"{dados[conf_aluno][1][nome_notas]}".lower(), end= "")
                        print(f" " * (cal_form - (q_letras if q_letras == len(dados[conf_aluno][1]) else len(dados[conf_aluno][1])) - 11) + f"{dados[conf_aluno][3][0]} e {dados[conf_aluno][3][1]}")
                        break

                    elif conf_aluno == len(dados) - 1:
                        print(f"Nenhum(a) aluno(a) com o N° de Cadastro '{conf_notas}' foi encontrado.")
            else:
                for conf_aluno in range(0, len(dados)):
                    if dados[conf_aluno][1] == conf_notas:
                        print(f"Nome:" + f"Notas:".rjust(cal_form - 10))
                        for nome_notas in range(0, len(dados[conf_aluno][1])):
                            if nome_notas == 0 or dados[conf_aluno][1][nome_notas-1] == " ":
                                print(f"{dados[conf_aluno][1][nome_notas]}".upper(), end= "")
                            else:
                                print(f"{dados[conf_aluno][1][nome_notas]}".lower(), end= "")
                        print(f" " * (cal_form - (q_letras if q_letras == len(dados[conf_aluno][1]) else len(dados[conf_aluno][1])) - 11) + f"{dados[conf_aluno][3][0]} e {dados[conf_aluno][3][1]}")
                        break

                    elif conf_aluno == len(dados) - 1:
                        print(f"Nenhum(a) aluno(a) com o nome '", end="")
                        for nome_notas in range(0, len(conf_notas)):
                            if nome_notas < (len(conf_notas) - 1):
                                if nome_notas == 0 or conf_notas[nome_notas-1] == " ":
                                    print(f"{conf_notas[nome_notas]}".upper(), end= "")
                                else:
                                    print(f"{conf_notas[nome_notas]}".lower(), end= "")
                            else:
                                print(f"{conf_notas[nome_notas]}' foi encontrado.".lower())
    
    elif conf_notas.upper() == "SAIR":
        print(f"Encerrando...")
        break
