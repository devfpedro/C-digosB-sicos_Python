#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O pograma será interrompido quando o número solicitado for negativo.

while True:
    n= int(input(f"Digite um número, para ver a sua tabuada:\nCaso não queira mais ver tabuadas, insira um número negativo (menor que zero).\nNúmero: "))

    if n < 0:
        print(f"Um número negativo foi inserido. O programa será encerrado!")
        break
    
    print(f"=" * 20)
    print(f"" + f"Tabuada de {n}".center(19) + f"")
    print(f"=" * 20)
    for tabuada in range (1, 11):
        print(f"{n} x {tabuada:2} = {n * tabuada:2}")
    print(f"=" * 20)
