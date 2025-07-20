from time import sleep
def maior (*num):
    print('='*30)
    print('Analisando os valores passados...')
    sleep(0.3)
    for i in num:
        print(i, end=' ')
        sleep(1.5)
    sleep(1.5)
    if len(num) == 0:
        pass
    print(f'\nFim da analise! \n{len(num)} numeros foram analisados')
    sleep(1.5)
    if len(num) > 0:
        print(f'O maior numero foi {max(num)}')


maior(10, 2, 5, 3)
maior(29, 40, 72, 12, 43)
maior(0, 9, 7, 3, 1, 5, 6)
maior(10, 8 , 5, 3, 11, 6)

maior()