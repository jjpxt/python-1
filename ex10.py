# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = int(input('Qual o preço do produto? R$ '))
desc = preco - (preco *5/100)
print(f'Com 5% de desconto o novo preço passa a ser R$ {desc:.2f} reais.')
