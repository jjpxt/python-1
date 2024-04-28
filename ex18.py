# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu? ')).lower()

if cidade[:5] == 'santo':
    print('O usuario nasceu em uma cidade que começa com Santo')
else:
    print('O usuario NÃO nasceu em uma cidade que começa com Santo')
