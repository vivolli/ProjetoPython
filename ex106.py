def titulo(msg):
    from time import sleep
    sleep(1.5)
    print('~' * 40)
    print(msg)
    print('~' * 40)


def acesso():
    from time import sleep
    while True:
        titulo('           Python Help System')
        sleep(1.5)
        resp = input('Nome da Function ou Library > ').lower()
        if resp != 'fim':
            sleep(1.5)
            print()
            titulo(f"   Acessando o manual do(a) '{resp}'")
            print()
            help(resp)
        else:
            break
    print('FIM')

acesso()
