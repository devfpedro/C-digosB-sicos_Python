#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres têm menos de 20 anos.

idades= []
nomes_mulheres= []
nomes_mulheresjovens= []
nomes_homens= []
idades_mulheres= []
idades_mulheresjovens= []
idades_homens= []

for preenchimento in range(1, 5):
    print(f"-" * 10, f"Insira os dados da {preenchimento}ª pessoa", f"-" * 10)
    nome= str(input("Informe o nome: ").capitalize().strip())
    idade= int(input("Informe o idade: ").strip())
    sexo= str(input(f"[F] = Feminino\n[M] = Masculino\nInforme seu sexo: ").upper().strip())
    
    if sexo == "F":
        ori_sexual= "FEMININO"
    if sexo == "M":
        ori_sexual= "MASCULINO"

    idades.append(idade)

    if idade < 20 and ori_sexual == "FEMININO":
        idades_mulheresjovens.append(idade)
        nomes_mulheresjovens.append(nome)
    elif idade >= 20 and ori_sexual == "FEMININO":
        idades_mulheres.append(idade)
        nomes_mulheres.append(nome)
    elif ori_sexual == "MASCULINO":
        nomes_homens.append(nome)
        idades_homens.append(idade)

q_homens= len(idades_homens)
q_mulheres= len(idades_mulheres)
q_mulheres20anos= len(idades_mulheresjovens)

print(f"-" * 10, f"Dados", f"-" * 10)

print(f"A média de idade do grupo é: {int((idades[0] + idades[1] + idades[2] + idades[3]) / 4)} anos.")

if q_homens == 1:
    if idades_homens[0] == 1:
        print(f"Há apenas um homem no grupo:\n{nomes_homens[0]}, com {idades_homens[0]} ano.")
    elif idades_homens[0] > 1:
        print(f"Há apenas um homem no grupo:\n{nomes_homens[0]}, com {idades_homens[0]} anos.")
elif q_homens > 1:
    for homens in range(q_homens):
        mais_velho= nomes_homens[0]

        if idades_homens[0] > idades_homens[-1]:
            idades_homens.pop(-1)
            nomes_homens.pop(-1)
        elif idades_homens[-1] > idades_homens[0]:
            idades_homens.pop(0)
            nomes_homens.pop(0)

    print(f"O homem mais velho é: \n{nomes_homens[0]}, com {idades_homens[0]} anos.")

if q_mulheres20anos == 1:
    if idades_mulheresjovens[0] == 1:
        print(f"Há apenas uma mulher com menos de 20 anos no grupo:\n{nomes_mulheresjovens[0]}, com {idades_mulheresjovens[0]} ano.")
    elif idades_mulheresjovens[0] > 2:
        print(f"Há apenas uma mulher com menos de 20 anos no grupo:\n{nomes_mulheresjovens[0]}, com {idades_mulheresjovens[0]} anos.")
elif q_mulheres20anos >= 2:
    print(f"Há {q_mulheres20anos} mulheres com menos de 20 anos no grupo:")
    for mulheres in range(q_mulheres20anos):
        if idades_mulheresjovens[0] == 1:
            print(f"{nomes_mulheresjovens[0]}, com {idades_mulheresjovens[0]} ano.")
            nomes_mulheresjovens.pop(0)
            idades_mulheresjovens.pop(0)
        elif idades_mulheresjovens[0] != 1:
            if idades_mulheresjovens == 0:
                print(f"{nomes_mulheresjovens[0]}, com {idades_mulheresjovens[0]} anos.")
                nomes_mulheresjovens.pop(0)
                idades_mulheresjovens.pop(0)
            elif idades_mulheresjovens != 0:
                print(f"{nomes_mulheresjovens[0]}, com {idades_mulheresjovens[0]} anos.")
                nomes_mulheresjovens.pop(0)
                idades_mulheresjovens.pop(0)
elif q_mulheres20anos == 0:
    if q_mulheres == 1:
        print(f"{nomes_mulheres[0]}, a única mulher do grupo, possui {idades_mulheres[0]} anos.")
    elif q_mulheres > 1:
        print(f"Nenhuma mulher do grupo possui menos de 20 anos.\nAs {q_mulheres20anos} mulheres do grupo possuem: ")
        for anos20 in range(q_mulheres):
            if idades_mulheres[0] == 1:
                print(f"{nomes_mulheres[0]} possui {idades_mulheres[0]} ano.")
            elif idades_mulheres[0] > 1:
                print(f"{nomes_mulheres[0]} possui {idades_mulheres[0]} anos.")
            nomes_mulheres.pop(0)
            idades_mulheres.pop(0)

print(f"-" * 27)
