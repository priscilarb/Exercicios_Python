#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a= float(input('Qual é a altura da parede? '))
l= float(input('Qual é a largura da parede? '))
h= l*a
t= h /2
print('A dimensão é {} x {} e sua área é de {}m²' .format(l,a,h))
print('Para pintar essa parede você precisará de {} l de tinta'.format(t))
