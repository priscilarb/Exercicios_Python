#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno_1= input('Nome do 1° aluno: ')
aluno_2= input('Nome do 2° aluno: ')
aluno_3= input('Nome do 3° aluno: ')
aluno_4= input('Nome do 4° aluno: ')
lista=[aluno_1,aluno_2,aluno_3,aluno_4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)