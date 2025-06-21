#Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO;
#Média entre 5.0 e 6.9: RECUPERAÇÃO;
#Média 7.0 ou superior: APROVADO.

nota1= float(input("Digite a primeira nota: ").strip())
nota2= float(input("Digite a segunda nota: ").strip())

media= float((nota1 + nota2) / 2)

if media < 5.0:
    print(F"Sua média final foi {media}\nVocê está REPROVADO.")
elif media >= 5.0 and media < 7.0:
    print(f"Sua média final foi {media}\nVocê está de RECUPERAÇÃO.")
elif media >= 7.0:
    print(f"Sua média final foi {media}\nVocê está APROVADO!")
