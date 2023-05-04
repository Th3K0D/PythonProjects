''''
Password Generator
Regra de criptografia atual

A=@
B=&
C=*
D=13
E=1
F=7
R=#
S=%
M=$

'''

import os
import random

base = input("Digite a base da sua senha: ")

senha = ""

for letra in base:
    if letra in "Aa": senha = senha + "@"
    elif letra in "Bb": senha = senha + "&"
    elif letra in "Cc": senha = senha + "*"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "1"    
    elif letra in "Ff": senha = senha + "7"    
    elif letra in "Rr": senha = senha + "#"  
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra

print(senha)
