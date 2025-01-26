from datetime import date
print('GUIA DE NATAÇÃO')
ano = date.today().year
nasc = int(input('Ano de Nascimento: '))
calculo = (ano - nasc)
if calculo <= 9:
    print(f'Com {calculo} anos, você se encaixa como Atleta Mirim.')
elif 14 >= calculo > 9:
    print(f'Com {calculo} anos, você se encaixa como Atleta Infantil.')
elif 19 >= calculo > 14:
    print(f'Com {calculo} anos, você se encaixa como Atleta Junior.')
elif calculo <= 25:
    print(f'Com {calculo} anos, você se encaixa como Atleta Sênior.')
elif calculo > 25:
    print(f'Com {calculo} anos, você se encaixa como Atleta Master.')
