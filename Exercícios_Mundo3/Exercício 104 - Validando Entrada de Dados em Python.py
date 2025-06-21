#Crie um programa que tenha a função "leiaInt()", que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
#Ex:
#n= leiaInt("Digite um n")

def leiaInt(possivel_n):
    """
    Função "def leiaInt(possivel_n)": Vai receber um dado inserido pelo usuário e apenas aceitá-lo e exibi-lo em uma mensagem se o valor for do tipo inteiro.
    > A função recebe o parâmetro "possivel_n";
    > :param possivel_n: Recebe a mensagem que pede ao usuário para inserir dados.
    """
    while True:
        info_usuario= str(input(f"{possivel_n}").strip().lower())
        n_confirmado= True if info_usuario.count(".") < 2 else False
        if info_usuario != "" and info_usuario != ".":
            if info_usuario.count(".") == 1:
                if info_usuario[0] != "." and info_usuario[-1] != ".":
                    for conf in range(0, len(info_usuario)):
                        if info_usuario[conf] not in "0123456789.":
                            n_confirmado= False
                            break
            else:
                for conf in range(0, len(info_usuario)):
                    if info_usuario[conf] not in "0123456789":
                        n_confirmado= False
                        break
        else:
            n_confirmado= False

        if n_confirmado:
            info_usuario= int(info_usuario) if info_usuario.count(".") == 0 else float(info_usuario)
            return info_usuario
        print(f"=" * 30 + f"\n\033[31mERRO! O dado inserido não é um número.\033[m\n\033[34mDigite novamente.\033[m")

valor= leiaInt(f"=" * 30 + f"\nDigite um número: ")
print(f"=" * 30 + f"\nO número digitado foi {valor}")
