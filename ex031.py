passagem = float(input('Digite a distancia da viagem: '))
if passagem <=200:
    print(f'O valor pago pela passagem sera de R$ {passagem * 0.5:.2f}')
else:
    print(f'O valor pago pela passagem sera de R$ {passagem * 0.45:.2f}')