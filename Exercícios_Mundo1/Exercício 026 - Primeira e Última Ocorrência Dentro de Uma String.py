#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez.

frase= str(input("Digite uma \033[1;33mfrase:\033[m ")).strip()
print(f"A frase '\033[1m{frase}\033[m' possui\033[3m", frase.upper().count("A"), f"letras 'A'0\033[0m\03[m." f"\nA primeira letra 'A' que aparece na frase '\033[1;45m{frase}\033[m' está na posição\033[3m",frase.upper().find("A") + 1, f"\n\033[0mA última letra 'A' que aparece na frase\033[m '\033[1;45m{frase}\033[m' está na posição", frase.upper().rfind("A") + 1)
