casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
financiamento = float(input('Tempo de financiamento em anos: '))
calculo_meses = financiamento * 12
porcentagem_salario = salario * (30/100)
pretacoes = (casa / calculo_meses)
if porcentagem_salario >= pretacoes:
    print(f'Para pagar a casa no valor de R${casa:.0f} num periodo de {financiamento:.0f} anos, a pretacao sera de R${pretacoes:.2f}')
    print('CONCEDIDO, meus parabens pela sua nova aquisicao!')
else:
    print(f'Para pagar a casa no valor de R${casa:.0f} num periodo de {financiamento:.0f} anos, a pretacao sera de R${pretacoes:.2f}')
    print('NEGADO, voce ainda nao pode financiar a casa, pois cada parcela excede 30% do seu salario')