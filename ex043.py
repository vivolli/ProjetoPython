print('CALCULADORA IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
if altura.is_integer():
    altura = altura/100
imc = peso / (altura*altura)
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('Você está no PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com Obesidade Grau I!')
elif imc >= 40:
    print('Você está com Obesidade Grau II!')
print(f'Seu IMC é de {imc:.1f}.')
