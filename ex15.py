# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input('Nome da primeira pessoa: '))
n2 = str(input('Nome da segunda pessoa: '))
n3 = str(input('Nome da terceira pessoa: '))
n4 = str(input('Nome da quarta pessoa: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação será -> {lista}')
