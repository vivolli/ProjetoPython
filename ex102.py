def fatorial(num=1, show=False):
    """
    -> Calculo de um fatorial
    por: Eduardo N. Oliveira
    :param num: Entrada do usuario para calculo
    :param show: Se o usuario deseja demonstrar todo calculo (parametro opcional)
    :return: retorna o valor calculado
    """
    if show == True:
        f = 1
        for i in range(num, 0, -1):
            f *= i
            print(i, end=' ')
            print('x' if i > 1 else '=' ,  end=' ')
    else:
        f = 1
        for i in range(num, 0, -1):
            f *= i
    return f


fact = int(input('Digite um numero: '))
print(fatorial(fact, True))
