# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual seu nome completo? ')).strip().lower()
print(f'Tem Silva' if 'silva' in nome else 'Não tem Silva')

# if 'silva' in nome:
#     print(f'{nome.lower()} Tem Silva no nome.')
# else:
#     print(f'{nome.lower()} Não tem Silva no nome.')
