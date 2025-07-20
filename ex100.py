from random import randint
from time import sleep

def sorteia(lista):
    while len(lista) < 5:
        num = randint(0,10)
        if num not in numeros:
            numeros.append(num)
    print('Sorteando os valores')
    for i in numeros:
        sleep(1)
        print(f'{i}', end=' ')
    sleep(1)
    print('FIM')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos pares é igual a: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)