# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero: '))
if numero % 2:
    print(f'O número {numero} é IMPAR')
else:
    print(f'O número {numero} é PAR')
