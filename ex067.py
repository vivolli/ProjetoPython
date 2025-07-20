while True:
    print('=' * 20)
    num = int(input('Digite um numero: '))
    print('=' * 20)
    if num >= 0:
        for i in range (1,11):
            print(f'{num} x {i} = {num*i}')
    if num < 0:
        break
print('VOCE CHEGOU AO FIM. Muito Obrigado!')
