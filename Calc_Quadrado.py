'''
    Calcula a area de um quadrado
'''
import os

base = float(input("Digite a base do quadrado: "))
os.system("cls")
altura = float(input("Digite a Altura do quadrado: "))
os.system("cls")

calculo = base * altura

print("A área do seu quadrado é de {calculo}.".format(calculo=calculo))