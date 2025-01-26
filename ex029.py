velocimetro = float(input('Quantos KM de velocidade atingiu o seu carro?'))
multa = (velocimetro - 80) * 7
if  velocimetro <= 80:
    print('Pode prosseguir!')
else:
    print(f'Voce sera multado em R${multa:.1f}, por excesso de velocidade ')
print('Dirija com cuidado!')
