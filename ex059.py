from time import sleep
choice = 0
num = int(input('Digite o primeiro numero: '))
num_2 = int(input('Digite o segundo numero: '))
while choice != 5:
    sleep(2)
    print('-'*22)
    print('''
[1] Somar
[2] Multiplicar
[3] Maior numero
[4] Novos numeros
[5] Sair do Programa
    ''')
    print('-'*22)
    choice = int(input('Digite qual operação você deseja: '))
    sleep(1.2)
    if choice == 1:
        print(f'{num} + {num_2} = {num+num_2}')
    if choice == 2:
        print(f'{num} x {num_2} = {num*num_2}')
    if choice == 3:
        if num > num_2:
            print(f'Entre {num} e {num_2}, {num} é maior!')
        elif num_2 > num:
            print(f'Entre {num} e {num_2}, {num_2} é maior!')
    if choice == 4:
        num = int(input('Digite o primeiro número novamente: '))
        num_2 = int(input('Digite o segundo número novamamente: '))
    if choice == 5:
        print('FIM')
    if choice >= 6:
        print('Opção Invalida. Tente novamente!')
print('Obrigado pela participação!')
