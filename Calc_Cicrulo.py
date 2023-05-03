
'''
    Este programa calcula a área de um circulo.
'''

import os
import math

raio = float(input("Digite a o raio do circulo: "))
os.system("cls")

area = math.pi * raio**2

print(f'A área do seu circulo é de {area:.2f}')