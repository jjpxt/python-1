# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'a letra "a" aparece {frase.count('A')} vezes')
print(f'a letra "a" aparece pela primeira vez na {frase.find('A') + 1}ª posição.')
print(f'a letra "a" aparece pela ultima vez na {frase.rfind('A')+1}ª posição.')
