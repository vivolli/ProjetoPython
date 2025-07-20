def notas(*valor, sit=False):
    """
    -> Funcao para avaliar desempenho de alunos
    :param valor: valores que serao passados para o calculo da media e averiguacao da situacao
    :param sit: situacao referente ao valor da media, sendo pessimo, ruim, regular, boa e exelente
    :return: retorno do dicionario nota
    """
    situacao = ''
    maior = max(valor)
    menor = min(valor)
    total = len(valor)
    media = (sum(valor) / total)
    nota = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'media': media
    }
    if sit:
        if media <= 3:
            nota['situacao'] = 'PÉSSIMO'
        elif 3 < media <= 5:
            nota['situacao'] = 'RUIM'
        elif 5 < media <= 7:
            nota['situacao'] = 'REGULAR'
        elif 7 < media <= 8:
            nota['situacao'] = 'BOA'
        else:
            nota['situacao'] = 'EXCELENTE'
    return nota

n = notas(5.5,2.5,1.5)
print(n)
