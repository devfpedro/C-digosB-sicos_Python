#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n= int(input("Digite um número inteiro: "))
valor_n= ""
valores= 1

if n > 1:
    if n == 2:
        print(f"{n} é um número primo.")
    elif n != 2 and n % 2 != 0:
        for primo in range(2, n):
            valores= valores + 1
            
            if n % valores == 0 and n / n == 1 and n / 1 == n:
                valor_n= f"{n} não é um número primo."
                break
            else:
                valor_n= f"{n} é um número primo."
        print(f"{valor_n}")
    else:
        print(f"{n} não é um número primo.")

else:
    print(f"Para ser um número primo, o número deve ser maior do que '1'.")
