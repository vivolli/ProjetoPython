from random import randint
contabilidade = 0
while True:
    numero = int(input('Digite um número: '))
    maquina = randint(0, 23)
    soma = numero + maquina
    impar_par = ''
    while impar_par not in 'PI':
        impar_par = input('Ímpar ou Par [I / P]: ').strip().upper()
    print(f'Você escolheu {numero}, a máquina escolheu {maquina}, e a soma foi {soma}')
    if (soma % 2 == 0 and impar_par == 'P') or (soma % 2 == 1 and impar_par == 'I'):
        print('PARABÉNS, VOCÊ VENCEU!')
        contabilidade += 1
        print('Vamos jogar novamente...')
        print('=-=' * 15)
    else:
        print('VOCÊ PERDEU! :(')
        break
vez_palavra = "vez" if contabilidade == 1 else "vezes"
print(f'GAME OVER. Você ganhou {contabilidade} {vez_palavra}.')
