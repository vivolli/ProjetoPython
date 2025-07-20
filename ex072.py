numero = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolha = int(input('Digite um número (0 a 20): '))
    if 0 <= escolha <= 20:
        print(f'Seu número é {numero[escolha]}!')
        while True:
            print('='*15)
            continuar = input('Deseja continuar [S/N]: ').upper()
            print('=' * 15)
            if continuar not in ['S','N']:
                print('Resposta invalida. Try Again!')
            elif continuar == 'S':
                break
            elif continuar == 'N':
                break
        break
    else:
        print('Error. Try Again...')
print('Obrigado por participar!')
