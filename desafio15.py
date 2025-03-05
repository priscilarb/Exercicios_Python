#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele ficou alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
d= int (input('Por quantos dias o carro ficou alugado? '))
k= float(input('Quantos km rodados? '))
v1= 60*d
v2= 0.15*k
print('O valor do aluguel do carro foi de R$ {}' .format(v1 + v2))
