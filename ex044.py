import time
print('''Seja bem-vindo(a) ao caixa, qual a forma de pagamento:
[ 1 ] Dinheiro ou Cheque a vista, com 10% de desconto
[ 2 ] Cartao a vista, com 5% de desconto
[ 3 ] Cartao ate 2x sem juros
[ 4 ] Cartao 3+ vezes com 20% de juros''')
escolha = int(input('Escolha a forma de pagamento: '))
time.sleep(3)
valor = float(input('Digite o valor da compra: R$'))
if escolha == 4:
    quantidade = int(input('Digite a quantidade de parcelas: '))
    print(f'O valor pago sera de R${valor + (valor * 10)/100:.2f}')
    print(f'Parcelado em {quantidade}x, o valor de cada parcela saira R${valor+(valor*10/100)/quantidade}')
elif escolha == 1:
    print(f'O valor pago no dinheiro/cheque sera de R${valor - (valor * 10 / 100):.1f}.')
elif escolha == 2:
    print(f'O valor pago no cartao a vista sera de, R${valor - (valor * 5 / 100):.2f}.')
elif escolha == 3:
    print(f'O valor pago no cartao em 2x sera de, R${valor:.2f}.')
    print(f'O valor de cada parcela sera de {valor/2}')
elif escolha == 4:
    print('O valor pago no cartao em ')
else:
    print('Opcao invalida. Tente novamente!')