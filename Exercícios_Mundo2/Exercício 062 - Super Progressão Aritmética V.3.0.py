#Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p_termo= int(input("Digite o primeiro termo da PA: "))
razão= int(input("Informe a razão da PA: "))
guardar_termo= 0
total_termos= 10

while guardar_termo < 10:
    if guardar_termo <= 7:
        print(f"{p_termo}, ", end= "")
    elif guardar_termo == 8:
        print(f"{p_termo} e ", end= "")
    else:
        print(f"{p_termo}.")
    p_termo= p_termo + razão
    guardar_termo= guardar_termo + 1
termos= ""
while termos == "":
    mais_termos= int(input("Você gostaria que mais termos dessa PA fossem mostrados?\nSe sim, quantos seriam?\nSua resposta: "))
    guardar_termo= 0
    total_termos= total_termos + mais_termos
    
    if mais_termos > 0:
        while guardar_termo < mais_termos:
            if guardar_termo < (mais_termos - 2):
                print(f"{p_termo}, ", end= "")
            elif guardar_termo < (mais_termos - 1):
                print(f"{p_termo} e ", end= "")
            else:
                print(f"{p_termo}.")
            p_termo= p_termo + razão
            
            guardar_termo= guardar_termo + 1
    else:
        termos= "conferidos"
print(f"Ao todo, foram mostrados {total_termos} termos dessa PA.")
