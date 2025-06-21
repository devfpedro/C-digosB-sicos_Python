def moeda(formatar_moeda):
    formatar_moeda= str(formatar_moeda)
    if formatar_moeda.count(".") == 1:
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
        
        if (len(formatar_moeda) - (formatar_moeda.index(",") + 1)) > 2:
            formatar_moeda= formatar_moeda[0:formatar_moeda.index(",")+3]
        
    else:
        formatar_moeda= formatar_moeda + f",00"
        
    return formatar_moeda

def aumentar(aumentar_moeda, por_aumento):
    aumentar_moeda= aumentar_moeda + ((aumentar_moeda / 100) * por_aumento)

    return aumentar_moeda

def diminuir(diminuir_moeda, por_diminuiçao):
    diminuir_moeda= diminuir_moeda - ((diminuir_moeda / 100) * por_diminuiçao)

    return diminuir_moeda

def dobro(dobrar_moeda):
    dobrar_moeda= dobrar_moeda * 2

    return dobrar_moeda

def metade(metade_moeda):
    metade_moeda= metade_moeda / 2

    return metade_moeda
