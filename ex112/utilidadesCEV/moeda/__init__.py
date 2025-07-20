def conversao(n):
    '''
    - > funcao de conversao do padrao para o real Brasileiro
    ex: 34.53 -> R$ 34,53
    :param n: parametro da funcao que recebera o valor inserido
    :return: retorno o valor ja convertido para a moeda Real
    '''
    import locale
    locale.setlocale(locale.LC_MONETARY, 'pt-BR.UTF-8')
    valor_convertido = locale.currency(n, grouping=True)
    return valor_convertido

def dobro(numero=0, format=False):
    res = numero * 2
    return res if not format else conversao(res)

def metade(numero=0, format=False):
    res = numero / 2
    return res if not format else conversao(res)

def aumentar(numero=0, valor=0, format=False):
    res = numero + (numero * valor/100)
    return res if format is False else conversao(res)

def diminuir(numero=0, valor=0, format=False):
    res = numero - (numero * valor/100)
    return res if format is False else conversao(res)

def resumo(numero=0, aumento=0,decremento=0, format=False):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preco Analisado: \t{conversao(numero)}')
    print(f'Dobro do preco: \t{conversao( dobro(numero) )}')
    print(f'Metade do preco: \t{conversao( metade(numero) )}')
    print(f'{aumento}% de aumento: \t{conversao( aumentar(numero, aumento) )}')
    print(f'{decremento}% de reducao: \t{conversao( diminuir(numero, decremento) )}')
    print('=' * 30)
