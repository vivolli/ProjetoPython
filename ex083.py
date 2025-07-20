expressao = input('Digite sua expressao matematica:\n')
validacao_direito = expressao.count('(')
validacao_esquerdo = expressao.count(')')
if validacao_direito == validacao_esquerdo:
    print('Sua expressao eh perfeita!')
else:
    print('Sua expressao possui erros')
# Tem erros de forma como escreve )(