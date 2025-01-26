desc = float(input('Escreva o valor para ser aplicado o desconto! R$'))
desconto = desc - (desc * 5 / 100)
print('O valor com desconto aplicado é {:.2f} R$'.format(desconto))