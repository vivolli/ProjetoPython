def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mDigite um INTEIRO valido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero: {n}')
