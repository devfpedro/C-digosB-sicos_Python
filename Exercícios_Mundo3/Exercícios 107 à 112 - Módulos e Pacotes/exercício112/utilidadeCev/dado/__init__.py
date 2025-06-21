def leia_dinheiro(msg):
    while True:
        possivel_valor= str(input(msg).strip().lower())
        numero_aceito= True

        if len(possivel_valor) > 0:
            if possivel_valor.count(".") == 1 or possivel_valor.count(",") == 1:
                if possivel_valor.count(".") == 1 and possivel_valor != "." and possivel_valor[0] != "." and possivel_valor[-1] != ".":
                    for conf in possivel_valor:
                        if conf not in "0123456789.":
                            numero_aceito= False
                            break
                elif possivel_valor.count(",") == 1 and possivel_valor != "," and possivel_valor[0] != "," and possivel_valor[-1] != ",":
                    for conf in possivel_valor:
                        if conf not in "0123456789,":
                            numero_aceito= False
                            break

                    guardar_possivel_valor= possivel_valor
                    possivel_valor= ""
                    for sub in guardar_possivel_valor:
                        if sub == ",":
                            possivel_valor= possivel_valor + "."
                        else:
                            possivel_valor= possivel_valor + sub

                else:
                    numero_aceito= False
            elif possivel_valor.count(".") == 0 and possivel_valor.count(",") == 0:
                for conf in possivel_valor:
                    if conf not in "0123456789":
                        numero_aceito= False
                        break
            else:
                numero_aceito= False
        else:
            print(f"=" * 31 + f"\n\033[34mPor favor, insira um número.\033[m")
            numero_aceito= False
        
        if numero_aceito:
            break
        elif numero_aceito == False and possivel_valor != "":
            print(f"=" * 31 + f"\n\033[31mERRO! Isso não pode ser considerado como número.\033[m" + f"\n\033[34mPor favor, tente novamente.\033[m")

    return possivel_valor
