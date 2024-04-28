# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('é Numerico? ',a.isnumeric())
print('só tem espaços? ',a.isspace())
print('está em minusculo? ',a.islower())
print('esta em maiusculo?',a.isupper())
print('O tipo primitivo desse valor é: ',type(a))
