'''
    Este programa calcula qual o valor do produto após o valor do desconto.
'''

import os

print("Este programa calcula qual o valor do produto após o valor do desconto.")

produto = float(input("Digite o valor do produto: "))
os.system("cls")
desconto = int(input("Digite o valor do desconto: "))
os.system("cls")

calculo_desc = produto * desconto / 100
prod_desc = produto - calculo_desc

print(f"Seu produto custa R${produto:.2f}. Seu desconto é de {desconto}%. O valor do seu produto com desconto foi para R${prod_desc:.2f}.")