print('ANALISTA DE VALORES')
primeiro = float(input('Dite o primeiro valor:'))
segundo = float(input('Digite o seugundo valor: '))
if primeiro > segundo:
    print(f'O Primeiro valor {primeiro} é maior que o Segundo valor {segundo}!')
elif segundo > primeiro:
    print(f'O Segundo valor {segundo} é maior que o primeiro {primeiro}!')
else:
    print('Ambos os valores sao iguais')