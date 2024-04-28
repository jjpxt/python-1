# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

a = int(input('Digite um número: '))
print('~' * 31)
for i in range(1, 11):
    print(f'A tabuada de {a} é -> {a} X {i} é {a * i}')
print('~' * 31)
