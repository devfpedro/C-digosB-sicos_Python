#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinheiro/cheque: 10% de desconto;
#À vista no cartão: 5% de desconto;
#Em até 2x no cartão: Preço normal;
#3x ou mais no cartão: 20% de juros.

valor_produto= float(input("Informe o valor do produto: ").strip())
print(f"Digite uma das opções abaixo, para que possamos dar seguimento a sua compra:\nPara selecionar o pagamento via dinheiro (10% de desconto), digite '1'.\nPara selecionar o pagamento via PIX (10% de desconto), digite '2'.\nPara selecionar o pagamento à vista via cartão (5% de desconto), digite '3'.\nPara selecionar o pagamento em até 2x no cartão, digite '4'.\nPara selecionar o pagamento em 3x ou mais no cartão, digite '5'.")
forma_pagamento= int(input("Digite um número de '1' à '5' para selecionar a forma de pagamento, de acordo com as informações da tabela acima: ").strip())

if forma_pagamento == 1:
    print(f"O valor do produto com pagamento via dinheiro, será de R${valor_produto - ((valor_produto * 10) / 100):.2f}")
elif forma_pagamento == 2:
    print(f"O valor do produto com pagamento via PIX, será de R${valor_produto - ((valor_produto * 10) / 100):.2f}")
elif forma_pagamento == 3:
    print(f"O valor do produto à vista via cartão, será de R${valor_produto - ((valor_produto * 5) / 100):.2f}")
elif forma_pagamento == 4:
    print(f"O valor do produto em 2x no cartão, será de R${valor_produto:.2f}\nCada parcela custará R${valor_produto / 2}")
elif forma_pagamento == 5:
    total_parcelas= int(input("Informe em quantas vezes vai parcelar o produto (3x ou mais): ").strip())
    
    if total_parcelas == 3:
        print(f"O valor do produto em 3x no cartão, será de R${valor_produto + ((valor_produto * 20) / 100):.2f}")
        print(f"Cada parcela custurá R${(valor_produto + ((valor_produto * 20) / 100)) / total_parcelas:.2f}")
    elif total_parcelas >= 4:
        print(f"O valor do produto em {total_parcelas}x no cartão, será de R${valor_produto + ((valor_produto * 20) / 100):.2f}")
        print(f"Cada parcela custará R${(valor_produto + (valor_produto * 20) / 100):.2f}")
    else:
        print(f"A informação inserida não corresponde com nenhuma das possibilidades da opção de parcelamento selecionada (3x ou mais).\nPor favor, insira as informações novamente, seguindo as instruções concedidas.")
else:
    print(f"A informação inserida não corresponde com nenhum dos números das opções de pagamento.\nPor favor, insira novamente as informações, seguindo as instruções concedidas.")
