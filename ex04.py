# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))
a = num * 2
b = num * 3
c = num ** (1 / 2)
print(f'O dobro de {num} é {a}\nO triplo de {num} é {b}\nA raiz quadrada é {c:.2f}')
