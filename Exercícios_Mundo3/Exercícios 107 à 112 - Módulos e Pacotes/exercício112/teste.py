from utilidadeCeV import dado, moeda

moeda_usuario= dado.leia_dinheiro(f"=" * 30 + f"\nInforme o valor: R$")
moeda.resumo(moeda_usuario, 45, 72)
