#Crie um programa onde o usário digite uma expressão que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao= str(input("Informe sua expressão matemática: ").strip())

g_abertos= []
for partes in expressao:
    if partes == "(":
        g_abertos.append(partes)
    elif partes == ")":
        if len(g_abertos) > 0:
            g_abertos.pop()
        else:
            g_abertos.append(")")
            break
            
if len(g_abertos) > 0:
    print(f"A expressão '{expressao}' está incorreta.")
else:
    print(f"Sua expressão '{expressao}' está correta.")
