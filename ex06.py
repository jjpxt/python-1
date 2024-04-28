# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input('Digite a distancia em metros: '))
print(f'Essa distancia em kilometros é {metros / 1000} KM')
print(f'Essa distancia em centimetros é {metros * 100} cms')
print(f'Essa distancia em milimetros é {metros * 1000} mm')
