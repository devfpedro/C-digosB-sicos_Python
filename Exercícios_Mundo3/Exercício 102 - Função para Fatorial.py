#Crie um programa que tenha uma função "fatorial()" que receba dois parâmetros: o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def confirmar():
    """
    Função "def confirmar()": Pergunta ao usuário se o número inserido está correto e se o calculo do fatorial deve ser exibido.
    > A função não recebe parâmetros;
    > :return: Retorna o número digitado pelo usuário e se o cálculo do fatorial deve ser exibido.
    """
    while True:
        conf_n= str(input(f"=" * 30 + f"\nInsira o número para ver o seu fatorial: ").strip().lower())
        sem_letras= True
        for buscar_l in conf_n:
            if buscar_l in "abcçdefghijklmnopqrstuvwxyz`´^~:;>.<,?/°}]º{[ª]+=§_-'|\!@#$%¨&*() " or buscar_l in '"':
                sem_letras= False
                break
        if sem_letras:
            while True:
                resposta= str(input(f"=" * 30 + f"\nO número {conf_n} está correto?\n" + f"-" * 30 + f"\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir o Número Novamente\nSua resposta: ").strip().lower())
                if resposta == "sim" or resposta == "nao" or resposta == "não":
                    break
                print(f"=" * 30 + f"\nA informação '{resposta}' não condiz com nenhuma das opções possiveis.\nPor favor, tente novamente.")
            if resposta == "sim":
                break

    while True:
        conf_show= str(input(f"=" * 30 + f"\nVocê deseja ver o calculo do fatorial de {conf_n}?\nDigite 'Sim' para Confirmar\nDigite 'Não' ou deixe 'em branco' para Negar\nSua resposta: ").strip().lower())
        if conf_show == "sim" or conf_show == "nao" or conf_show == "não" or conf_show == "":
            break
        print(f"=" * 30 + f"\nA informação '{conf_show}' não condiz com nenhuma das opções possiveis.\nPor favor, tente novamente.")

    return int(conf_n), conf_show

def fatorial(n, show= "não"):
    """
    Função "def fatorial()": Calcula o fatorial de um número e o exibe (apenas o resultado ou o calculo completo, dependendo da escolha do usuário).
    > A função recebe os parâmetros "n" e "show" (este último recebendo "não" como argumento na ausência de um argumento passado como parâmetro pelo usuário));
    > :param n: Recebe o número que será calculado o fatorial;
    > :param show: Recebe a informação para exibir o calculo completo do fatorial ou não;
    > :return: Retorna o calculo completo e o resultado final do fatorial ou apenas o resultado final do fatorial.
    """
    base= 1
    for cal in range(n, 0, -1):
        base= base * cal
    
    print(f"=" * 30)
    if show == "sim":
        if n != 0:
            for mostrar_cal in range(n, 0, -1):
                if mostrar_cal == 1:
                    print(f"{mostrar_cal}!= ", end= "")
                else:
                    print(f"{mostrar_cal} x ", end= "")
        else:
            print(f"0!= ", end= "")

    return print(base)

confirmaçoes= confirmar()
fatorial(confirmaçoes[0], confirmaçoes[1])
