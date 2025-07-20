maior = menor = 0
pessoas = []
while True:
    print('='*30)
    nome = input('Digite seu nome: ').capitalize()
    peso = int(input(f'Digite seu peso, {nome}: '))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print('='*30)
    coninuar = input('Deseja continuar [S/N]').upper()
    if coninuar == 'S':
        pass
    elif coninuar == 'N':
        break
    else:
        print('Error')
        break
print(f'Ao todo {len(pessoas)} foram cadastradas:\n')
print()
print(f'Lista dos mais pesados ({maior} Kg):', end=' ')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}', end=' ')
print(f'Lista dos mais leves ({menor} Kg):', end=' ')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}', end=' ')
