#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais sãos as suas vogais.

tupla_lanches= ("Pedro", "Leticia", "Junior", "Erick", "Gabriel", "Marcos", "Hendrix", "Josy", "Aquila", "Filipe")

for nomes in tupla_lanches:
    q_letras= len(nomes)
    q_vogais= 0

    for conf_vogais in range(q_letras):
        if nomes[conf_vogais] in "aeiouAEIOU":
            q_vogais= q_vogais + 1
    
    if q_vogais > 1:
        print(f"O nome '{nomes}' possui as {q_vogais} vogais: ", end= "")
    elif q_vogais == 1:
        print(f"O nome '{nomes}' possui apenas a vogal: ", end= "")

    if q_vogais > 1:
        vogais_saida= q_vogais
        for vogais in range(q_letras):
            if nomes[vogais] in "aeiouAEIOU" and vogais_saida > 1:
                print(f"{nomes[vogais]}, ", end= "")
                vogais_saida= vogais_saida - 1
            elif nomes[vogais] in "aeiouAEIOU" and vogais_saida == 1:
                print(f"{nomes[vogais]}.")
    elif q_vogais == 1:
        for vogal in range(q_letras):
            if nomes[vogal] in "aeiouAEIOU":
                print(f"{nomes[vogal]}.")
