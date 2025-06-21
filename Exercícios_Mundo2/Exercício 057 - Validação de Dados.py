#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo= ""
while sexo == "":
    sexo= str(input("Informe seu sexo:\n[M] = Masculino\n[F] = Feminino\nSua resposta: ").upper().strip())

    if sexo == "M":
        print(f"Certo. Você é do sexo masculino.")
        sexo= sexo
    elif sexo == "F":
        print(f"Certo. Você é do sexo feminino.")
        sexo= sexo
    else:
        print(f"O caractere inserido não corresponde a nenhuma das opções possíveis.\nPor favor, tente novamente.")
        sexo= ""
