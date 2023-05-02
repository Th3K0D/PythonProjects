'''
 A ideia desse script simples é apenas gerar um registro de compra/venda e comissão do vendedor no console com o objetivo de praticar a logica.

'''
import os

cliente = input("Digite o nome do cliente: ")
os.system("cls")
qtd_producto = int(input("Quantos produtos ele comprou: "))
os.system("cls")
nam_producto = input("Qual o produto ele comprou: ")
os.system("cls")
val_producto = float(input("Qual o valor de cada produto: "))
os.system("cls")
nam_vendor = input("Quem foi o Vendedor: ")
os.system("cls")
valor_venda = val_producto * qtd_producto
perc_comissao = 10
Comissao = valor_venda * perc_comissao / 100

texto = f'Olá, {cliente} sua compra "{qtd_producto}x {nam_producto}" com o valor R$ {val_producto:.2f} cada e total de R$ {valor_venda:.2f}  foi efetuada com sucesso!".'
texto_vendor = f'Olá, {nam_vendor} você acaba de receber uma comissão de R${Comissao:.2f} pela compra realizada pelo(a) cliente {cliente}.'

print(texto)
print(texto_vendor)
