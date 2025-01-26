from time import sleep
from random import choice
escolha_computador = ['Pedra', 'Papel', 'Tesoura']
print('Vamos Jogar?')
print('''Escolha sua opção
[ 1 ] PEDRA.
[ 2 ] PAPEL.
[ 3 ] TESOURA.''')
escolha = int(input('Opção escolhida: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
comp = choice(escolha_computador)
#PEDRA
if escolha == 1 and comp == 'Tesoura':
    print('Sua escolha foi Pedra.')
    print('O jogador venceu!')
    print(f'O jogador escolheu Pedra e o computador escolheu {comp}.')
elif escolha == 1 and comp == 'Papel':
    print('Sua escolha foi Pedra.')
    print('O computador venceu!')
    print(f'O jogador escolheu Pedra e o computador escolheu {comp}.')
#PAPEL
elif escolha == 2 and comp == 'Pedra':
    print('Sua escolha foi Papel.')
    print('O jogador venceu!')
    print(f'O jogador escolheu Papel e o computador escolheu {comp}.')
elif escolha == 2 and comp == 'Tesoura':
    print('Sua escolha foi Papel.')
    print('O computador venceu!')
    print(f'O jogador escolheu Papel e o computador escolheu {comp}.')
#TESOURA
elif escolha == 3 and comp == 'Papel':
    print('Sua escolha foi Tesoura.')
    print('O jogador venceu!')
    print(f'O jogador escolheu Tesoura e o computador escolheu {comp}.')
elif escolha == 3 and comp == 'Pedra':
    print('Sua escolha foi Tesoura.')
    print('O computador venceu!')
    print(f'O jogador escolheu Tesoura e o computador escolheu {comp}.')
#EMPATE
elif escolha == 1 and comp == 'Pedra' or escolha == 2 and comp == 'Papel' or escolha == 3 and comp == 'Tesoura':
    print('Empate')
else:
    print('Opcao invalida. Tente novamente!')
#refazer