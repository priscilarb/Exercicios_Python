#Crie um programa que leia quanto dinheiro uma pessoa possa ter na carteira e mostre quantos dólares ela pode comprar. Considere $1.00 = R$ 3.27 
r= float(input('Quanto dinheiro você tem na carteira? R$ '))
d= r / 3.27
print('Com R$ {:.2f} você pode comprar US${:.2f}' .format(r,d))