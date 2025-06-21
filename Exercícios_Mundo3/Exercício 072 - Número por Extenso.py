#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#Adicional (Passado no Vídeo do Desáfio): Dê a opção do usuário continuar digitando números quantas vezes quiser.

n_extensos= ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    while True:
        num= int(input("Digite um número de 0 a 20 para saber sua escrita por extenso: "))
        if num >= 0 and num <= 20:
            print(f"O número {num} escrito por extenso é {n_extensos[num]}.")
            break
        else:
            print(f"O número '{num}' não está no intervalo de 0 a 20.\nPor favor, tente novamente.")

    while True:
        continuar= str(input(f"Você deseja inserir mais um número?\n[S] -> Sim\n[N] -> Não\nSua resposta: ").strip())
        if continuar in "nNsS":
            break
        else:
            print(f"'{continuar}' não está entre as opções possíveis.\nPor favor, tente novamente.")
    if continuar in "nN":
        break
