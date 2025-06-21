#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso;
#Entre 18.5 e 25: Peso Ideal;
#25 até 30: Sobrepeso;
#30 até 40: Obesidade;
#Acima de 40: Obesidade Mórbida.

altura= float(input("Informe a sua altura: ").strip())
peso= float(input("Informe o seu peso: ").strip())

print(f"O resultado do seu IMC é {(peso / (altura ** 2)):.1f}")

if (peso / (altura ** 2)) < 18.5:
    print(f"De acordo com o seu IMC, você está abaixo do peso.")
elif (peso / (altura ** 2)) >= 18.5 and (peso / (altura ** 2)) < 25:
    print(f"De acordo com o seu IMC, você está no peso ideal.")
elif (peso / (altura ** 2)) >= 25 and (peso / (altura ** 2)) < 30:
    print(f"De acordo com o seu IMC, você está com sobrepeso.")
elif (peso / (altura ** 2)) >= 20 and (peso / (altura ** 2)) < 40:
    print(f"De acordo com o seu IMC, você está com obesidade.")
else:
    print(f"De acordo com o seu IMC, você está co obesidade mórbida.")
