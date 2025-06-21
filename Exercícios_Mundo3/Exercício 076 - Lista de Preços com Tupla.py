#Crie um programa que tenha uma tupla única com nomes de produtos e seus respecitvos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista_p= ("Coxinha", 3, "Pastel", 4, "Hambúrguer", 8, "Suco", 1.50, "Joelho", 5, "Refrigerante", 3, "Pizza", 10, "Sanduíche", 5, "Enroladinho", 3, "Bolo", 16)

print(f"=" * 26)
print(f"|" + f"Cardápio".center(24) + f"|")
print(f"=" * 26)

for cardapio in range(0, len(lista_p), 2):
    if lista_p[cardapio+1] > 9:
        print(f"|{lista_p[cardapio]:.<16}" + f"R$ "+ f"{lista_p[cardapio+1]:.2f}|")
    else:
        print(f"|{lista_p[cardapio]:.<16}" + f"R$  " + f"{lista_p[cardapio+1]:.2f}|")
