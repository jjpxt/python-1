# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

from time import sleep

nome = str(input('Qual seu nome: ')).strip()
print('-' * 30)
print('    ANALISANDO SEU NOME...')
print('-' * 30)
sleep(2)
print(f'Seu nome em maisculo fica: {nome.upper()}')
print('-' * 50)
sleep(2)
print(f'Seu nome em  minusculo fica: {nome.lower()}')
print('-' * 50)
sleep(2)
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras.')
print('-' * 50)
sleep(2)
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
print('-' * 50)
