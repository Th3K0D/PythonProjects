
'''
 Neste script coloquei iniciei perguntando qual o titulo do post e com a biblioteca random fiz com que o proprio script gere um numero de compartilhamentos aleatorio de 1 a 100.
'''

import os
import random

titulo = input("Digite o Titulo do post: ")
os.system("cls")
compartilhamentos = random.randint(1, 100)

texto = f'Seu post com o título "{titulo}" gerou {compartilhamentos} compartilhamentos.'

print(texto)
