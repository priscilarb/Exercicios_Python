#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
s= float(input('Qual o salário atual? R$ '))
ns= s + (s*0.15)
print('O novo salário com o aumento de 15% é R$ {:.2f}'.format(ns))