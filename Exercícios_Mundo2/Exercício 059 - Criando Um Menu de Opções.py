#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do Programa
#Seu programa deverá realizar a operação solicitada em cada passo.

programa= "funcionando"

while programa == "funcionando":
    n1= float(input("Digite o primeiro número: "))
    n2= float(input("Digite o segundo número: "))

    print(f"Escolha uma das opções para dar seguimento:\n[1] -> Somar\n[2] -> Multiplicar\n[3] -> Maior\n[4] -> Novos Números\n[5] -> Sair do Programa")
    menu= "nenhuma"
    while menu == "nenhuma":
        escolha= int(input("Sua escolha: "))
        if escolha > 0 and escolha < 6:
            if escolha == 1:
                print(f"A opção escolhida foi '1' - Os valores inseridos serão somados.\nResultado: {n1} + {n2} = {n1 + n2}")
            elif escolha == 2:
                print(f"A opção escolhida foi '2' - Os valores inseridos serão multiplicados.\nResultado: {n1} x {n2} = {n1 * n2}")
            elif escolha == 3:
                print(f"A opção escolhida foi '3' - O maior número será exibido.")
                if n1 > n2:
                    print(f"Resultado: O maior número é {n1}")
                elif n2 > n1:
                    print(f"Resultado: O maior número é {n2}")
                else:
                    print(f"Resultado: Não existe número maior, pois ambos possuem o mesmo valor: {n1}")
            elif escolha == 4:
                print(f"A opção escolhida foi '4' - Você poderá digitar novos valores.")
                menu= "escolha"
            elif escolha == 5:
                print(f"A opção escolhida foi '5' - O programa será encerrado.")
                menu= "escolha"
                programa= "encerrado"
            
        else:
            print(f"A opção inserida não corresponde a nenhuma das opções possíveis.\nPor favor, tente novamente e escolha um número de 1 a 5.")
            menu= "nenhuma"
