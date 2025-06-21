#Faça um programa que tenha uma função "notas()" que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#>A quantidade de notas;
#>A maior nota;
#>A menor nota;
#>A média da turma;
#>A situação (opcional).
#Adicione também as docstrings da função.

from time import sleep

def confirmar_dados():
    """
    Função "def confirmar_dados()": Recebe a quantidade de notas que serão digitadas, as notas dos alunos da turma e guarda as notas em um dicionário, mas apenas se os valores forem do tipo int ou float. Além disso, faz a confirmação dos dados, perguntando se a quantidade de notas que serão digitadas está correta e se as notas que foram inseridas tammbém foram digitadas corretamente, exibindo-as em uma pequena tabela para visualização enquanto isso. Caso o usuário deixe a quantidade de notas em branco, a função perguntará se deseja continuar mesmo assim, sabendo que a resposta será salva como "Não" e, consequentemente, nenhuma nota poderá ser inserida.
    > A função não recebe parâmetros;
    > :param return: Retorna um dicionário com todas as notas da turma, cada uma registrada com o aluno "da vez", como "Nota do 1° Aluno", por exemplo.
    """
    while True:
        total_notas= str(input(f"=" * 30 + f"\nQuantas notas de alunos deseja inserir?\n=> ").strip().lower())
        num_confirmado= True

        if total_notas != "":
            for conf in total_notas:
                if conf not in "0123456789":
                    print(f"=" * 30 + f"\nApenas números podem ser digitados.\nPor favor, tente novamente.")
                    num_confirmado= False
                    break
            if num_confirmado:
                while True:
                    confirmar= str(input(f"=" * 30 + f"\nEstá certo de que irá inserir " + (f"{total_notas} notas de {total_notas} alunos?" if total_notas != "1" else f"uma nota de 1 aluno") + f"?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Informar Outra Quantidade\n=> ").strip().lower())
                    if confirmar == "sim" or confirmar == "não" or confirmar == "nao":
                        break
                    print(f"=" * 30 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")
                if confirmar == "sim":
                    total_notas= int(total_notas)
                    if total_notas == 0:
                        while True:
                            total_zero= str(input(f"=" * 30 + f"\nDeseja prosseguir com a informação de '0 notas para inserir'?\nCaso sim, nenhuma nota poderá ser inserida e os dados e situação da turma não serão exibidos.\nDigite 'Sim' para Confirmar\nDigite 'Não' para Informar Outra Quantidade\n=> ").strip().lower())
                            if total_zero == "sim" or total_zero == "não" or total_zero == "nao":
                                break
                            print(f"=" * 30 + f"\n'{total_zero}' não é uma opção disponível.\nPor favor, tente novamente.")
                        if total_zero == "sim":
                            break
                    else:
                        break
        else:
            while True:
                confirmar= str(input(f"=" * 30 + f"\nDeixando a quantidade de notas em branco, o programa contabilizará a informação como 0.\nAssim, notas não poderão ser inseridas e o programa não exibirá os dados da turma.\nDeseja prosseguir mesmo assim?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir a Quantidade de Notas\n=> ").strip().lower())
                if confirmar == "sim" or confirmar == "não" or confirmar == "nao":
                    break
                print(f"=" * 30 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")
            if confirmar == "sim":
                break
    
    if total_notas != "":
        cont= 1
        info_aluno= {}
        guardar_total_notas= total_notas
        while total_notas > 0:
            inserir_notas= str(input(f"=" * 30 + f"\nInforme a nota do {cont}° aluno: ").strip().lower())
            numero_conferido= True

            pontos= 0
            if inserir_notas != "":
                for conf in inserir_notas:
                    if conf == ".":
                        pontos= pontos + 1

                    if conf not in "0123456789.":
                        print(f"=" * 30 + f"\n{inserir_notas} é inválido como nota.\nPor favor, tente novamente.")
                        numero_conferido= False
                        break
            else:
                print(f"=" * 30 + f"\nPor favor, insira sua nota.")
                numero_conferido= False
            
            if numero_conferido and pontos < 2:
                if float(inserir_notas) >= 0 and float(inserir_notas) <= 10:    
                    if pontos > 0:
                        if inserir_notas[0] != "." and inserir_notas[-1] != ".":
                            inserir_notas= float(inserir_notas)
                            total_notas= total_notas - 1
                        else:
                            print(f"=" * 30 + f"\n{inserir_notas} é inválido como nota.\nPor favor, tente novamente.")
                            numero_conferido= False
                    else:
                        inserir_notas= int(inserir_notas)
                        total_notas= total_notas - 1

                else:
                    print(f"=" * 30 + f"\nA nota inserida deve estar no intervalo de 0 à 10.\nPor favor, tente novamente.")
                    numero_conferido= False
                
                if numero_conferido:
                    info_aluno["Nota do(a) " + str(cont) + "° Aluno(a)"]= inserir_notas
                    cont= cont + 1
                
                if total_notas == 0:
                    while True:
                        sleep(1)
                        print(f"=" * 30 + f"\n" + (f"Todas as {guardar_total_notas} notas inseridas estão corretas?" if guardar_total_notas > 1 else f"A nota inserida está correta?") + f"\n" + f"-" * 30 + f"\nNotas da Turma:")
                        for mostrar_notas in range(1, len(info_aluno.items()) + 1):
                            sleep(1)
                            print(f"> Nota do(a) {mostrar_notas}° Aluno(a): {info_aluno['Nota do(a) ' + str(mostrar_notas) + '° Aluno(a)']}")
                        sleep(1)
                        confirmar= str(input(f"-" * 30 + f"\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir " + (f"as Notas" if guardar_total_notas > 1 else f"a Nota") + f" Novamente\n=> ").strip().lower())
                        if confirmar == "sim" or confirmar == "não" or confirmar == "nao":
                            break
                        print(f"=" * 30 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")
                    if confirmar == "sim":
                        return info_aluno
                    else:
                        total_notas= guardar_total_notas
                        cont= 1

            elif numero_conferido and pontos > 1:
                print(f"=" * 30 + f"\n{inserir_notas} é inválido como nota.\nPor favor, tente novamente.")
    else:
        return total_notas

def visualizar_situ():
    """
    Função "visualizar_situ()": Pergunta ao usuário se deve exibir a situação da turma com base em sua média geral, apenas encerrando ao obter a resposta "sim" ou "não" ou, se o usuário deixar a resposta em branco, "" (mas, antes, pergunta se o usuário deseja prosseguir, mesmo sabendo que a informação será salva como "não" neste caso).
    > A função não recebe parâmetros;
    > :param return: Retorna "True", caso o usuário tenha escolhido por visualizar a situação da turma, ou "False", caso o usuário tenha escolhido não visualizar a situação da turma.
    """
    while True:
        visualizar= str(input(f"=" * 30 + f"\nDeseja visualizar a situação da turma com base em sua média geral?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Negar\n=> ").strip().lower())
        if visualizar == "sim" or visualizar == "não" or visualizar == "nao" or visualizar == "":
            if visualizar == "":
                while True:
                    confirmar= str(input(f"=" * 30 + f"\nDeixando a informação em branco, o programa contabilizará como 'Não'.\nAssim, a situação da turma não será exibida.\nDeseja prosseguir mesmo assim?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir a Informação Correta\n=> ").strip().lower())
                    if confirmar == "sim" or confirmar == "não" or confirmar == "nao":
                        break
                    print(f"=" * 30 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")
                if confirmar == "sim":
                    break
            else:
                break
        else:
            print(f"=" * 30 + f"\n'{visualizar}' não é uma opção disponível.\nPor favor, tente novamente.")
    
    if visualizar == "sim":
        visualizar= True
    else:
        visualizar= False

    return visualizar

def notas(info, visu_situaçao= False):
    """
    Função "def notas(info, visu_situaçao= False)": Recebe o dicionário e a informação de exibir a situação da turma ou não, adicionando tudo em um dicionário que conterá a quantidade de notas da turma, a maior nota turma, a menor nota da turma, a média da turma e, em caso de "True" para a visualização da situação da turma, a situação da turma com base na média geral.
    > A função recebe os parâmetros "info" e "visu_situaçao";
    > :param info: Recebe as notas de todos os alunos da turma;
    > :param visu_situaçao: Recebe a informação de se deve exibir a situação da turma ou não. Caso o valor esteja em branco ou nenhum dado tenha sido passado, receberá "False" como argumento;
    > :param return: Retorna todos os dados - Quantidade de Notas, Maior Nota, Menor Nota, Média da Turma e, caso visu_situaçao receber True como argumento, Situação da Turma - em um dicionário.
    """
    perfil_turma= {"Quantidade de Notas": len(info)}

    for maior_menor in range(0, len(info)):
        if maior_menor == 0:
            perfil_turma["Maior Nota"]= info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"]
            perfil_turma["Menor Nota"]= info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"]
        else:
            if info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"] > perfil_turma["Maior Nota"]:
                perfil_turma["Maior Nota"]= info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"]
            if info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"] < perfil_turma["Menor Nota"]:
                perfil_turma["Menor Nota"]= info["Nota do(a) " + str(maior_menor+1) + "° Aluno(a)"]

    media= 0
    for somar in range(0, len(info)):
        media= media + info["Nota do(a) " + str(somar+1) + "° Aluno(a)"]
    media= media / len(info)
    perfil_turma["Média da Turma"]= media
    
    if visu_situaçao:
        if perfil_turma["Média da Turma"] <= 3.9:
            situaçao_turma= "Ruim"
        elif perfil_turma["Média da Turma"] <= 6.9:
            situaçao_turma= "Razoável"
        elif perfil_turma["Média da Turma"] >= 7.0:
            situaçao_turma= "Boa"
        perfil_turma["Situação da Turma"]= situaçao_turma

    return perfil_turma

dados_turma= confirmar_dados()
if dados_turma != "":
    observar_turma= visualizar_situ()
    turma= notas(dados_turma, observar_turma)

    for exibir in range(0, (4 if len(turma) == 4 else 5)):
        sleep(1)
        if exibir == 0:
            print(f"=" * 30 + f"\n" + (f"Dados da Turma".center(30) if len(turma) == 4 else f"Dados da Turma e Situação".center(30)) + f"\n" + f"=" * 30)
            print(f"-Total de Notas: " + f"{turma['Quantidade de Notas']}".rjust(13))
        elif exibir == 1:
            print(f"-Maior Nota da Turma:" + f"{turma['Maior Nota']:.1f}".rjust(9))
        elif exibir == 2:
            print(f"-Menor Nota da Turma: " + f"{turma['Menor Nota']:.1f}".rjust(8))
        elif exibir == 3:
            print(f"-Média Geral da Turma: " + f"{turma['Média da Turma']:.1f}".rjust(7))
        elif len(turma) == 5 and exibir == 4:
            print(f"-Situação da Turma: " + f"{turma['Situação da Turma']}".rjust(10))

print(f"-" * 30) if dados_turma != "" else print(f"=" * 30)
sleep(1)
print(f"Encerrando...")
sleep(1)
