#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimno será negado.

valor_casa= float(input("Informe o valor da casa: R$").strip())
salario_comprador= float(input("Informe o salário do comprador: R$").strip())
pagamento_anos= int(input("Informe em quantos anos deseja quitar a casa: ").strip())

parcela_mensal= float((valor_casa / pagamento_anos) / 12)

limite_salario= float((salario_comprador * 30) / 100)

print(f"A casa custa R${valor_casa:.2f}. Para ser paga em {pagamento_anos} anos, o valor da parcela mensal será de R${parcela_mensal:.2f}")

if parcela_mensal > limite_salario:
    print(f"Sinto muito: O valor de R${parcela_mensal:.2f} excede o limite de 30% com base no seu salário mensal.\nSerá necessário renegociarmos os valores do empréstimo.")
else:
    print(f"Os valores negociados estão dentro dos conformes e, portanto, o empréstimo pode ser feito para a compra da casa.")
