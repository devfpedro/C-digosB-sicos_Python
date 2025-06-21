#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.
#OBS: Use cores.

from time import sleep

def resposta():
    while True:
        duvida_usuario= str(input(f"\033[1;30;47m" + f"=" * 95 + f"\nInforme o comando, da Linguagem de Programação Python, que você deseja ver as informações:\nCaso não queira conferir nenhum comando, digite 'Fim'\n=> ").strip().lower())
        comando_possivel= True if duvida_usuario != "fim" else False
        for conf in range(0, len(duvida_usuario)):
            if duvida_usuario[conf] in "0123456789!@#$%¨&*()\|<,>.:;?/°^~`´{[ª}]º_-+=§'" or duvida_usuario[conf] in '"':
                print(f"\033[1;37;41m" + f"=" * 95 + f"\n\033[3m'{duvida_usuario}'\033[1;37;41m não pode ser um comando.\nPor favo, tente novamente.")
                comando_possivel= False
                break

        if comando_possivel:
            if duvida_usuario != "":
                while True:
                    confirmar= str(input(f"\033[m" + f"=" * 95 + f"\n\033[1;37;44mVocê deseja saber mais sobre o comando \033[1;3;37;44m'{duvida_usuario}'\033[m\033[1;37;44m, certo?\nCaso sim, digite 'Sim'\nCaso não, digite 'Não'\n=> ").strip().lower())
                    if confirmar == "sim" or confirmar == "nao" or confirmar == "não":
                        break
                    print(f"\033[1m;37;41m" + f"=" * 95 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.\033[m")
                if confirmar == "sim":
                    sleep(1)
                    print(f"\033[1;37;42m" + f"=" * 95)
                    help(duvida_usuario)
            else:
                while True:
                    confirmar= str(input(f"\033[1;43m" + f"=" * 95 + f"\nNenhum comando foi inserido. O programa entenderá que deve ser encerrado.\nDeseja permanecer sem informar nenhum comando?\nCaso sim, digite 'Sim'\nCaso não, digite 'Não'\n=> ").strip().lower())
                    if confirmar == "sim" or confirmar == "nao" or confirmar == "não":
                        break
                    print(f"\033[m" + f"=" * 95 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")
                if confirmar == "sim":
                    sleep(1)
                    return print(f"\033[1;37;45m" + f"=" * 95 + f"\nNenhum comando inserido. O programa será encerrado." + f"\n" + f"=" * 95 + f"\nEncerrando...\033[m")
        else:
            while True:
                confirmar= str(input(f"\033[1;47m" + f"=" * 95 + f"\nTem certeza que deseja encerrar o programa?\nCaso sim, digite 'Sim'\nCaso não, digite 'Não'\n=> ").strip().lower())
                if confirmar == "sim" or confirmar == "nao" or confirmar == "não":
                    sleep(1)
                    return print(f"\033[1;37;45m" + f"=" * 95 + f"\nEncerrando...")
                print(f"\033[1;37;41m" + f"=" * 95 + f"\n'{confirmar}' não é uma opção disponível.\nPor favor, tente novamente.")

responder_usuario= resposta()
sleep(1)
