# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = str(input('Nome do primeiro meliante: '))
n2 = str(input('Nome do segundo meliante: '))
n3 = str(input('Nome do terceiro meliante: '))
n4 = str(input('Nome do quarto meliante: '))
lista = [n1, n2, n3, n4]
the_chosen_one = random.choice(lista)
print(f'O aluno escolhido foi {the_chosen_one}')
