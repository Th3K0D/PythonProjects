import os

print('Calcule a área de um retangulo')

base = float(input("Digite a base do retangulo: "))
os.system("cls")
altura = float(input("Digite a Altura do retangulo: "))
os.system("cls")

calculo = base * altura

print("A área do seu retangulo é de {calculo}.".format(calculo=calculo))