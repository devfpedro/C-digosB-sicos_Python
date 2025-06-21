def moeda(formatar_moeda, retornar_format= True):
    if retornar_format:
        formatar_moeda= str(formatar_moeda)
        if formatar_moeda.count(".") == 1:
            if len(formatar_moeda) >= 2 and formatar_moeda[0] != "." and formatar_moeda[-1] != ".":
                if (len(formatar_moeda) - (formatar_moeda.index(".") + 1)) >= 2:
                    separar_n= []

                    for tran in range(0, len(formatar_moeda)):
                        if formatar_moeda[tran] == ".":
                            separar_n.append(",")
                        else:
                            separar_n.append(formatar_moeda[tran])
                    
                    formatar_moeda= ""
                    for ad in separar_n:
                        formatar_moeda= formatar_moeda + ad

                elif (len(formatar_moeda) - (formatar_moeda.index(".") + 1)) == 1:
                    separar_n= []

                    for tran in range(0, len(formatar_moeda)):
                        if formatar_moeda[tran] == ".":
                            separar_n.append(",")
                        else:
                            separar_n.append(formatar_moeda[tran])
                    
                    formatar_moeda= ""
                    for ad in separar_n:
                        formatar_moeda= formatar_moeda + ad
                    formatar_moeda= formatar_moeda + "0"
            else:
                formatar_moeda= formatar_moeda[0:formatar_moeda.index(".")] + f",00"
        else:
            formatar_moeda= formatar_moeda + f",00"

    return formatar_moeda

def aumentar(aumentar_moeda, por_aumento, retornar_format= False):
    aumentar_moeda= aumentar_moeda + ((aumentar_moeda / 100) * por_aumento)
    if retornar_format:
        aumentar_moeda= moeda(aumentar_moeda)

    return aumentar_moeda

def diminuir(diminuir_moeda, por_diminuiçao, retornar_format= False):
    diminuir_moeda= diminuir_moeda - ((diminuir_moeda / 100) * por_diminuiçao)
    if retornar_format:
        diminuir_moeda= moeda(diminuir_moeda)

    return diminuir_moeda

def dobro(dobrar_moeda, retornar_format= False):
    dobrar_moeda= dobrar_moeda * 2
    if retornar_format:
        dobrar_moeda= moeda(dobrar_moeda)

    return dobrar_moeda

def metade(metade_moeda, retornar_format= False):
    metade_moeda= metade_moeda / 2
    if retornar_format:
        metade_moeda= moeda(metade_moeda)

    return metade_moeda

def resumo(valor_moeda= 0, valor_aumento= 0, valor_diminuir= 0):    
    valor_moeda= float(valor_moeda)

    valor_acres= aumentar(valor_moeda, valor_aumento)
    if str(valor_aumento).count(".") == 1:
        valor_aumento= moeda(valor_aumento)
    valor_acres= moeda(valor_acres, True)
    msg_aumento= f"Acréscimo de {valor_aumento}%: " + f"R${valor_acres[0:valor_acres.index(',')+3]}".rjust(31 - (16 + len(str(valor_aumento))))

    valor_desc= diminuir(valor_moeda, valor_diminuir)
    if str(valor_diminuir).count(".") == 1:
        valor_diminuir= moeda(valor_diminuir)
    valor_desc= moeda(valor_desc, True)
    msg_desconto= f"Descontando {valor_diminuir}%: " + f"R${valor_desc[0:valor_desc.index(',')+3]}".rjust(31 - (15 + len(str(valor_diminuir))))

    valor_dobrado= dobro(valor_moeda, True)
    msg_dobro= f"Valor Dobrado: " + f"R${valor_dobrado[0:valor_dobrado.index(',')+3]}".rjust(31 - 15)

    valor_metade= metade(valor_moeda, True)
    msg_metade= f"Metade do Valor: " + f"R${valor_metade[0:valor_metade.index(',')+3]}".rjust(31 - 17)

    valor_moeda= moeda(valor_moeda, True)
    msg_valor_original= f"Preço Original: " + f"R${valor_moeda[0:valor_moeda.index(',')+3]}".rjust(31 - 16)

    return print(f"=" * 31 + f"\n" + f"Alterações no Preço".center(31) + f"\n" + f"-" * 31 + f"\n{msg_valor_original}" + f"\n{msg_aumento}" + f"\n{msg_desconto}" + f"\n{msg_dobro}" + f"\n{msg_metade}" + f"\n" + f"-" * 31)
