# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano quer analisar? '))
print(f'Esse ano é BISSEXTO' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Esse ano não é BISSEXTO!')
