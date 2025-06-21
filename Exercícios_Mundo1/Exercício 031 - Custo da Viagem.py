#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km_viagem= float(input("Qual a \033[1mdistância\033[m que será percorrida nessa viagem? "))

if km_viagem <= 200.0:
    print(f"Como a distância da viagem é de \033[1m{km_viagem:.1f}Km\033[m, o valor da passagem será de: \033[3;34mR${float(km_viagem * 0.50):.2f}\033[m")
else:
    print(f"Como a distância da viagem é de \033[1m{km_viagem:.1f}Km\033[m, o valor da passagem será de: \033[3;35mR${float(km_viagem * 0.45):.2f}\033[m")

#Ou (Dado como possibilidade pelo Guanabara, usando 'if' simplificado)
# preço = km_viagem * 0.50 if km_viagem <= 200 else km_viagem * 0.45
# print(f"Sua viagem será de {km_viagem}Km. Portanto, custará R${preço:.2f}")
