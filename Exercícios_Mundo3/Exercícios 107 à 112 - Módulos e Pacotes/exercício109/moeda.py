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
