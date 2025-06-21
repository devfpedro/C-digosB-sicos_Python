#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de ângulo será formado:
#Equilátero: Todos os lados iguais;
#Isóceles: Dois lados iguais;
#Escaleno: Todos os lados diferentes.

# reta1= float(input("Informe o comprimento da \033[1;30mprimeira reta\033[m: ").strip())
# reta2= float(input("Informe o comprimento da \033[1;30msegunda reta\033[m: ").strip())
# reta3= float(input("Informe o comprimento da \033[1;30mterceira reta\033[m: ").strip())

# if (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2 and (reta1 + reta2) > reta3:
#     print(f"As retas \033[1m{reta1}\033[m, \033[1m{reta2}\033[m, \033[1m{reta3}\033[m \033[1;32mpodem formar um triângulo\033[m.")
# else:
#     print(f"As retas \033[1m{reta1}\033[m, \033[1m{reta2}\033[m, \033[1m{reta3}\033[m \033[1;34mnão podem formar um triângulo\033[m.")

reta1= float(input("Informe o compprimento da primeira reta: ").strip())
reta2= float(input("Informe o comprimento da segunda reta: ").strip())
reta3= float(input("Informe o comprimento da terceira reta: ").strip())

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print(f"As retas {reta1} {reta2} e {reta3} podem formar um triângulo.")
    if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo equilátero, pois todos os lados são iguais.")
    elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta3 == reta1 and reta3 != reta2):
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo isóceles, pois dois lados, dos três, são iguais.")
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo escaleno, pois todos os três lados são diferentes.")
else:
    print(f"As retas {reta1}, {reta2} e {reta3} não podem formar um triângulo.")

#Parelelo - resposta do vídeo de resolução do desáfio:

# if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
#     print(f"As retas {reta1}, {reta2} e {reta3} podem formar um triângulo ", end= "")
#     if reta1 == reta2 == reta3:
#         print(f"equilátero.")
#     elif reta1 != reta2 != reta3 != reta1:
#         print(f"escaleno.")
#     else:
#         print(f"isóceles.")
# else:
#     print(f"As retas {reta1}, {reta2} e {reta3} não podem formar um triângulo.")
