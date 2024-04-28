#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = int(input('Qual o salário? R$ '))
novo_sal = sal + (sal * 15 / 100)
print('O novo salario passa a ser R$ {:.2f} reais'.format(novo_sal))
