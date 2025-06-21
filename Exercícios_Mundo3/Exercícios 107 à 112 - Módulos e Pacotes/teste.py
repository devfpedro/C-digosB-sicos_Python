from moeda import moeda, aumentar, metade, diminuir, dobro

moeda_usuario= float(input(f"=" * 30 + f"\nInforme o valor: R$"))
print(f"=" * 30)
print(f"O valor R${moeda(moeda_usuario, True)} aumentado em 52% é R${aumentar(moeda_usuario, 52, True)}")
print(f"O valor R${moeda(moeda_usuario, True)} descontado em 15% é R${diminuir(moeda_usuario, 15, True)}")
print(f"O dobro de R${moeda(moeda_usuario, True)} é R${dobro(moeda_usuario, True)}")
print(f"A metade de R${moeda(moeda_usuario, True)} é R${metade(moeda_usuario, True)}")
