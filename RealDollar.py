'''
    Calcula a conversão de Real para o Dollar
'''
import os

Dollar = float(input("Digite o valor atual do Dollar: "))
os.system("cls")
Real = float(input("Digite o valor que quer converter em reais: "))
os.system("cls")

calculo =  Real / Dollar

print(f'A conversão de R${Real:.2f} para o cambio atual de ${Dollar:.2f} é de ${calculo:.2f}.')