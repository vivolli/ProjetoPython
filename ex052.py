#MEU CODIGO
from time import sleep
print('Analisador de PRIMOS')
sleep(1.5)
tot = 0
num = int(input('Digite um numero: '))
for numero in range(1, num +1 ):
    if num % numero == 0:
        print(numero, end=' ')
        tot += 1
print(f'\nO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('PRIMO')
else:
    print('NAO PRIMO')

#CODIGO DO GUANABARA

# from time import sleep
# print('ANALISADOR DE PRIMOS')
# sleep(1)
# tot = 0
# num = int(input('Digite um numero para verificacao: '))
# for i in range(1, num +1):
#     if num % i == 0:
#         print('\033[033m', end=' ')
#         tot += 1
#     else:
#         print('\033[031m', end=' ')
#     print(i, end=' ')
# print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
# if tot == 2:
#     print('ELE EH PRIMO')
# else:
#     print('ELE NAO EH PRIMO')


