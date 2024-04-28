# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

viagem = int(input('Qual a distância da viagem em KMs: '))
if viagem <= 200:
    preço = viagem * 0.50
    print(f'A viagem custará: R$ {preço} reais.')
else:
    preço = viagem * 0.45
    print(f'A viagem custará: R$ {preço:.2f} reais.')
