#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta= "continuar"
soma= 0
numeros= 0
maior= 0
menor= 0
while resposta == "continuar":
    num= int(input("Insira um número inteiro: "))
    numeros= numeros + 1
    soma= soma + num

    if num > maior:
        maior= num

    if numeros == 1:
        menor= num
    elif numeros > 1 and num < menor:
        menor= num

    resp_valida= "resposta invalida"
    while resp_valida == "resposta invalida":
        resposta= str(input("Informe se deseja continuar a inserir valores:\n[S] = Sim\n[N] = Não\nSua resposta: ").upper().strip())
        if resposta == "N":
            resposta= resposta
            resp_valida= resposta
        elif resposta == "S":
            resposta= "continuar"
            resp_valida= resposta
        else:
            resp_valida= "resposta invalida"
            print(f"A resposta inserida não é nenhuma das opções possíveis.\nPor favor, tente novamente.")

if numeros == 1:
    print(f"Apenas um único número foi digitado: {num}\nA média do número é {soma / numeros:.1f}\nO maior número digitado foi {maior}\nO menor número digitado foi {menor}")
else:
    print(f"A média dos {numeros} números digitados foi {soma / numeros:.1f}\nO maior número digitado foi {maior}\nO menor número digitado foi {menor}")
