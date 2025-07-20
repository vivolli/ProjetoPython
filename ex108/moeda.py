def conversao(n):
    import locale
    locale.setlocale(locale.LC_MONETARY, 'pt-BR.UTF-8')
    valor_convertido = locale.currency(n, grouping=True)
    return valor_convertido

def dobro(numero=0):
    res = numero * 2
    return conversao(res)

def metade(numero=0):
    res = numero / 2
    return conversao(res)

def aumentar(numero=0, valor=0):
    res = numero + (numero * valor/100)
    return conversao(res)

def diminuir(numero=0, valor=0):
    res = numero - (numero * valor/100)
    return conversao(res)

