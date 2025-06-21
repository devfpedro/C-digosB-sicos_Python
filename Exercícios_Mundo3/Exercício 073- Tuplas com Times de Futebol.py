#Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro, na ordem de colocação. Depois mostre:
#a)Apenas os 5 primeiros colocados;
#b)Os últimos 4 colocados da tabela;
#c)Uma lista com os times em ordem alfabética;
#d)Em que posição na tabela está o time do São Paulo (originalmente Chapecoense no desafio).

tabela= ("Atlético-MG", "Bahia", "Botafogo-RJ", "Ceará SC", "Corinthias", "Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Mirassol", "Palmeiras", "Bragantino", "Santos", "Sport Recife", "São Paulo", "Vasco da Gama", "EC Vitória")

print(f"-" * 48)
print(f"" + f"Campeonato Brasileiro 2025".center(48))
print(f"-" * 48)

print(f"" + f"Classificação".center(48) + f"\n")
for times in range(0, 20):
    print(f"{times+1:2}°| {tabela[times]}")
print(f"-" * 48)

print(f"O G5 (Cinco Primeiros Colocados) é Composto Por:" + f"\n")
for primeiros in range(1, 6):
    print(f"{primeiros}°| {tabela[primeiros-1]}")
print(f"-" * 48)

print(f"O Z4 (Quatro Últimos Colocados) é Composto Por:" + f"\n")
for ultimos in range(17, 21):
    print(f"{ultimos}°| {tabela[ultimos-1]}")
print(f"-" * 48)

print(f"A Lista em Ordem Alfabética dos Times é: " + f"\n")
tabela_abc= sorted(tabela)
for abc in range(0, 20):
    if abc < 19:
        print(f"{tabela_abc[abc]}, ", end= "")
    else:
        print(f"{tabela_abc[abc]}.")
print(f"-" * 48)

print(f"O São Paulo Encontra-se na Posição:" + f"\n\n{tabela.index('São Paulo') + 1}°| São Paulo")
print(f"-" * 48)
