#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex:
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

frase= str(input("Digite uma frase: ").upper().strip())
q_palavras= len(frase.split())
junçao_palavras= ""
n= 0

if frase[0] == frase[-1]:
    leitura_palavras= frase.split()
    junçao_palavras= leitura_palavras[0]

    for soma in range(q_palavras-1):
        n= n + 1
        junçao_palavras= junçao_palavras + leitura_palavras[n]
    
    frase_invertida= junçao_palavras[::-1]
        
    if frase_invertida == junçao_palavras:
        print(f"'{frase}' é um palíndromo.")
    else:
        print(f"{frase} não é um palíndromo.")
else:
    print(f"'{frase}' não é um palíndromo.")

# frase= str(input("Digite uma frase: ").upper().strip())
# q_palavras= frase.split()
# espaços_0= "".join(q_palavras)
# frase_invertida= espaços_0[::-1]

# if espaços_0 == frase_invertida:
#     p_frase= f"{frase} é um palíndromo."
# else:
#     p_frase= f"{frase} não é um palíndromo."

# print(f"{p_frase}")
