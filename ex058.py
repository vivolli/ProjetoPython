from random import randint
from time import sleep
contabilizador_tentativa = 1
print('='*25)
print('ESCOLHA UM NÚMERO DE 1-10')
print('='*25)
sleep(1.5)
tentativa = int(input('Digite sua tentativa: '))
print('='*25)
jogo = randint (0,10)
while tentativa != jogo:
    contabilizador_tentativa += 1
    print('Voce errou!')
    print('-'*19)
    tentativa = int(input('Tente novamente: '))
print(f'''
Voce acertou! Parabéns
Sua escolha, {tentativa}
Opção da Maquina, {jogo}
Voce tentou {contabilizador_tentativa} vezes, antes de acertar.''')