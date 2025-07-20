lista = []
from random import randint
for i in range(5):
    numeros = randint(0,9)
    lista.append(numeros)
    print(numeros, end=' ')
print(f'\nO maior numero é {max(lista)}')
print(f'O menor numero é {min(lista)}')