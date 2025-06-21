def aumentar(aumentar_moeda, por_aumento, retornar_format= True):
    aumentar_moeda= aumentar_moeda + ((aumentar_moeda / 100) * por_aumento)

    return aumentar_moeda

def diminuir(diminuir_moeda, por_diminuiçao, retornar_format= True):
    diminuir_moeda= diminuir_moeda - ((diminuir_moeda / 100) * por_diminuiçao)

    return diminuir_moeda

def dobro(dobrar_moeda, retornar_format= True):
    dobrar_moeda= dobrar_moeda * 2

    return dobrar_moeda

def metade(metade_moeda, retornar_format= True):
    metade_moeda= metade_moeda / 2

    return metade_moeda
