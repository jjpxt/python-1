# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

from time import sleep

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número: {num}')
sleep(2)
print(f'Unidade {u}')
sleep(2)
print(f'Dezena {d}')
sleep(2)
print(f'Centena {c}')
sleep(2)
print(f'Milhar {m}')
