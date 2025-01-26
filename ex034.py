salario = float(input('Digite o seu salario atual: R$'))
if salario <= 1250:
    print(f'Com o aumento de 15% seu salario passa a ser R${salario + (salario * 15 / 100)}')
else:
    print(f'Com o aumento de 10% seu salario passa a ser R${salario + (salario * 10 / 100)}')