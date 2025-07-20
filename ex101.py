def voto(ano):
    """
    :param ano: parametro que sera substituído pela entrada do usuário
    :return: retorna os valores idade (ano atual - entrada de ano usuário)
    """
    from datetime import date
    print("="*35)
    ano_de_hoje = date.today().year
    idade = ano_de_hoje - ano
    if idade < 16:
        situacao = 'Menor_16'
    elif idade < 18:
        situacao = 'Menor_18'
    elif idade >= 70:
        situacao = 'Maior_70'
    else:
        situacao = 'Maior18_Menor70'

    voto_valor = {
        'Menor_16': 'Nao pode votar!',
        'Menor_18': 'tem Voto Opcional',
        'Maior18_Menor70': 'tem Voto Obrigatorio!',
        'Maior_70': 'tem Voto Opcional!'
    }
    return idade, voto_valor[situacao]

nascimento = int(input('Qual seu ano de nascimento: '))
idade, ocorrencia = voto(nascimento)
print(f'Com {idade} anos, voce {ocorrencia}')


# Tem como fazer so usando o return e passando str para ele, eu preferi usar dicionários para deixar mais daora.
