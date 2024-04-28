# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Qual a largura da parede que deseja pintar? '))
comp = float(input('Qual o comprimento da parede que deseja pintar? '))
area = larg * comp
lts = area / 2
print(f'A área que você irá pintar é de {area:.2f} e você precisará de {lts:.0f} litros de tinta para pintar ela.')