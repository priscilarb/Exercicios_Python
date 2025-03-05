#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p= float(input('Qual o valor do produto? R$ '))
d= p-(p * 0.05)
print('O valor do produto com desconto de 5% é R$ {:.2f}'.format(d))