# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero = int(input('Pensei em um número de 1 a 3, qual foi? '))
adivinha = randint(1, 3)
print('PENSANDO...')
sleep(2)
if numero == adivinha:
    print(f'Você acertou, pensei no número {adivinha}')
else:
    print('você errou, MT BURROKKKKKKKK')

print(f'Eu pensei no {adivinha}')

# while True:
#     numero = int(input('Pensei em um número de 1 a 3, qual foi? '))
#     adivinha = randint(1, 3)
#     print('PENSANDO...')
#     sleep(2)
#     if numero == adivinha:
#         print(f'VOCÊ ACERTOU, PENSEI NO NÚMERO {adivinha}')
#     else:
#         print('você errou, MT BUROKKKKKKKK')
#         print(f'Eu pensei no {adivinha}')
#
#     r = str(input('Quer continuar? [S/N]'))
#
#     if r in 'Nn':
#         break
