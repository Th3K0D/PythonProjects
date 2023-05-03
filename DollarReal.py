'''
    Calcula a conversão de Dollar Real
'''
import os

Cot_Dollar = float(input("Digite o valor atual do Dollar: "))
os.system("cls")
Dollar = float(input("Digite o valor em Dollar que quer converter para Real: "))
os.system("cls")

calculo = Dollar * Cot_Dollar
 
print(f'A conversão de ${Dollar:.2f} para Real é de R${calculo:.2f}, Usando a cotação de R${Cot_Dollar:.2f} o Dollar')