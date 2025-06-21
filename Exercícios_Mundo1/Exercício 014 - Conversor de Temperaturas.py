#Escreva um prograna que converta uma temperatura digitada em C° e converta para °F.

celsius= float(input("\033[3mInsira a temperatura em celsius:\033[m "))
print(f"\033[1mC°{celsius}\033[m é igual a \033[1mF°{(celsius * 1.8) + 32:.1f}\033[m")
