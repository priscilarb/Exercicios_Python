#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido. 
import random
aluno_1= input('Nome do 1° aluno: ')
aluno_2= input('Nome do 2° aluno: ')
aluno_3= input('Nome do 3° aluno: ')
aluno_4= input('Nome do 4° aluno: ')
lista= [aluno_1,aluno_2,aluno_3,aluno_4]
escolhido= random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')