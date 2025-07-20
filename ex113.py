def leia_int(y):
    while True:
        try:
            num = int(input(y))
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuario preferiu nao digitar!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mDigite um número inteiro valido\033[m')
        else:
            return num


def leia_float(x):
    while True:
        try:
            num = float(input(x))
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuario preferiu nao digitar!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mDigite um número real valido\033[m')
        else:
            return num

a = leia_int('Digite um numero inteiro: ')
b = leia_float('Digite um numero real: ')
print(f'Voce digitou os numeros: {a} e {b}')