# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=' * 30)
print('      ALUGUEL DE CARROS')
print('=' * 30)
dias = int(input('Quantos dias vai ficar com o carro? '))
d = dias * 60
print(f'O carro irá custa R${d} reais pelos dias que ficará com ele.')
print('=' * 30)
km = int(input('Quantos KMs irá percorrer? '))
k = km * .15
print(f'{km} kilometros percorridos lhe custarão R$ {k:.2f} reais adicionais')
print('=' * 30)
tot = d + k
print(f'O total a pagar será de R$ {tot:.2f} reais')
