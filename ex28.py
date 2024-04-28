# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual salario? '))

if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Seu novo salário é de {aumento}')
if salario < 1250:
    aumento1 = salario + (salario * 15 / 100)
    print(f'Seu novo salario passa a ser {aumento1}')
