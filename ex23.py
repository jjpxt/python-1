# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

carro = int(input('Qual foi a velocidade? '))
if carro > 80:
    multa = (carro - 80) * 7
    print(f'tomou multinha papai, multa de R${multa} reais')
print('tenha um bom dia, dirija com segurança.')
