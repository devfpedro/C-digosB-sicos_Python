#Reescreva a função "leiaInt()" que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num= str(input(f"{msg}"))
            num= int(num)

        except (ValueError):
            print(f"=" * 30 + f"\n\033[31mERRO! '{str(num)}' não é um número inteiro.\033[m")
        
        except (KeyboardInterrupt):
            print(f"\n" + f"=" * 30 + f"\033[34m\nO(A) usuário(a) optou por não digitar um número inteiro.\033[m")
            return 0

        else:
            return int(num)

def leiaFloat(msg):
    while True:
        try:
            num= str(input(f"{msg}"))
            num= float(num)

        except (ValueError):
            print(f"=" * 30 + f"\n\033[31mERRO! '{str(num)}' não é um número real.\033[m")

        except (KeyboardInterrupt):
            print(f"\n" + f"=" * 30 + f"\n\033[34mO(A) usuário(a) optou por não digitar um número real.\033[m")
            return 0
        
        else:
            return float(num)

r_i= leiaInt(f"=" * 30 + f"\nDigite um número inteiro, por favor.\n=> ")
r_f= leiaFloat(f"=" * 30 + f"\nDigite um número real, por favor.\n=> ")
print(f"=" * 30 + f"\nNúmero inteiro: \033[32m{r_i}\033[m\nNúmero real: \033[32m{r_f}\033[m\n" + f"-" * 30)
