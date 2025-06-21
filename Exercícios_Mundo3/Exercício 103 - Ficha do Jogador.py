#Faça um programa que tenha uma função chamada "ficha()", que receba dois parâmetros: o "nome" de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def confirmar_jogador():
    """
    Função "def confirmar_jogador()": Pede ao usuário que insira o nome de um jogador, fazendo a validação do nome para previnir erros de digitação e pergunta ao usuário se o nome digitado está correto.
    > A função não recebe parâmetros;
    > :param return: Retorna o nome do jogador ortograficamente correto.
    """
    while True:
        jogador= str(input(f"=" * 50 + f"\nInforme o nome do jogador: ").strip().lower())
        apenas_letras= True
        for conf in jogador:
            if conf in "1234567890!@#$%¨&*()-_=+§`^´~<,>.:;?/°}]º{]º\|'" or conf in '"':
                print(f"=" * 50 + f"\nO nome do jogador não pode conter números, caracteres especiais ou assentos que não acompanhem letras.\nPor favor, tente novamente.")
                apenas_letras= False
                break
        if apenas_letras:
            nome_confirmado= []
            for letra in range(0, len(jogador)):
                if letra == 0 or jogador[letra-1] == " ":
                    if jogador[letra] in "dD" and (jogador[letra+2] == " " or (jogador[letra+3] == " " and jogador[letra+2] in "sS")):
                        nome_confirmado.append(jogador[letra].lower())
                    else:
                        nome_confirmado.append(jogador[letra].upper())
                else:
                    nome_confirmado.append(jogador[letra].lower())
            jogador= ""
            for ad in nome_confirmado:
                jogador= jogador + ad
            while True:
                confirmar= str(input(f"=" * 50 + (f"\nO nome do jogador '{jogador}' está correto?" if jogador != "" else f"\nTem certeza que deseja deixar o nome do jogador em branco?") + f"\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir o Nome Novamente\nSua resposta: ").strip().lower())
                if confirmar == "sim" or confirmar == "nao" or confirmar == "não":
                    break
                print(f"=" * 50 + f"\nA informação '{confirmar}' não condiz com nenhuma das opções.\nPor favor, tente novamente.")
            if confirmar == "sim":
                return jogador

def confirmar_gols():
    """
    Função "def confirmar_gols()": Pede ao usuário que insira o número de gols feitos pelo jogador na temporada, fazendo a validação dos dados para prevenir erros de digitação e pergunta ao usuário se a quantidade de gols marcados está correta.
    > A função não recebe parâmetros;
    > :paran return: Retorna a quantidade de gols feitos pelo jogador na temporada.
    """
    while True:
        gols= str(input(f"=" * 50 + f"\nInforme quantos gols o jogador " + (f"{nome}" if nome != "" else f"<desconhecido>") + f" marcou na temporada: ").strip().lower())
        apenas_num= True
        for conf in gols:
            if conf not in "0123456789":
                print(f"=" * 50 + f"\nLetras, caracteres especiais ou assentos não podem ser inseridos como quantidade de gols.\nPor favor, tente novamente.")
                apenas_num= False
                break
        if apenas_num:
            while True:
                confirmar= str(input(f"=" * 50 + (f"\nO jogador " + (f"{nome}" if nome != "" else f"<desconhecido>") + f" marcou {gols} " + (f"gols" if gols != "1" else f"gol") + f" na temporada?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir a Quantidade de Gols Marcados Novamente\nSua resposta: " if gols != "" else f"\nTem certeza que deseja deixar a quantidade de gols marcados em branco?\nDigite 'Sim' para Confirmar\nDigite 'Não' para Inserir Novamente\nSua resposta: ")).strip().lower())
                if confirmar == "sim" or confirmar == "não" or confirmar == "nao":
                    break
                print(f"=" * 50 + f"\nA informação '{confirmar}' não condiz com nenhuma das opções possiveis.\nPor favor, tente novamente.")
            if confirmar == "sim":
                gols= int(gols) if gols != "" else f""
                return gols

def ficha(jogador= "", gols_marcados= ""):
    """
    Função "def ficha(jogador= '', gols_marcados= '')": Recebe o nome do jogador (ou a informação "<desconhecido>", em caso de ausência do nome) e a quantidade de gols feitos pelo jogador na temporada, exibindo as informações na saída de dados no terminal organizadamente de acordo com o nome do jogador e a quantidade de gols marcados.
    > A função recebe os parâmetros "jogador" e "gols_marcados";
    > :param jogador: Recebe o nome do jogador como argumento ou uma string vázia - "" - na falta de um argumento;
    > :param gols_marcados: Recebe a quantidade de gols como argumento ou uma string vázia - "" - na falta de um argumento;
    """
    print(f"=" * (10 + (len(jogador) if jogador != "" else 14) + 8 + (6 if gols_marcados == "" else (len(str(gols_marcados)) + 5) if gols_marcados != 1 else (len(str(gols_marcados)) + 4)) + 16))
    print(f"O jogador " + (f"{jogador}" if jogador != "" else f"<desconhecido>") + f" marcou " + (f"0 gols" if gols_marcados == "" else f"{gols_marcados} gols" if gols_marcados != 1 else f"{gols_marcados} gol") + f" na temporada")
    print(f"-" * (10 + (len(jogador) if jogador != "" else 14) + 8 + (6 if gols_marcados == "" else (len(str(gols_marcados)) + 5) if gols_marcados != 1 else (len(str(gols_marcados)) + 4)) + 16))

nome= confirmar_jogador()
q_gols= confirmar_gols()
ficha(nome, q_gols)
