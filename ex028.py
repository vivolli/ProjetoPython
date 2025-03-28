from random import randint
print('=-=' * 9)
print('Tente Adivinhar meu numero...')
print('=-=' * 9)
tentativa = int(input('Digite um valor: '))
variavel = randint(0,5)
if  tentativa == variavel:
    print('Voce ganhou! PARABENS')
else:
    print(f'Voce perdeu, meu numero era o {variavel}')

