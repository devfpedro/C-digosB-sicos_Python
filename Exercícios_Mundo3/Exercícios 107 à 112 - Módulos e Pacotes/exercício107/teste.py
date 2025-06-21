import moeda

moeda_usuario= float(input(f"=" * 30 + f"\nInforme o valor: R$"))
print(f"=" * 30)
print(f"O valor R${moeda_usuario} aumentado em 52% é R${moeda.aumentar(moeda_usuario, 52)}")
print(f"O valor R${moeda_usuario} descontado em 15% é R${moeda.diminuir(moeda_usuario, 15)}")
print(f"O dobro de R${moeda_usuario} é R${moeda.dobro(moeda_usuario)}")
print(f"A metade de R${moeda_usuario} é R${moeda.metade(moeda_usuario)}")
