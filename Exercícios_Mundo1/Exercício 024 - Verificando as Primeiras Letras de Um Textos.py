#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade= str(input("Informe o nome da cidade: \033[3;40m")).upper().split()
print("SANTO" in cidade[0])
