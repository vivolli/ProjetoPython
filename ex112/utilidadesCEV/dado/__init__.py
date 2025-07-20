def leia_dinheiro(x):
    validador = False
    while not validador:
        num = str(input(x)).strip().replace(',', '.')
        if num.isalpha() or num == '':
            print(f'\033[0;31mErro: "{num}" é inválido! Digite um número valido\033[m')
        else:
            validador = True
            return float(num)



