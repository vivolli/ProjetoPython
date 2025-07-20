valores = []
contagem_maior = contagem_menor = 0
for valor in range(5):
    valores.append(int(input(f'Digite o {valor+1} numero: ')))
print(valores)
contagem_maior = valores.count(max(valores))
contagem_menor = valores.count(min(valores))
print(f'O MAIOR valor é {max(valores)}')
print(f'O MENOR valor é {min(valores)}')
if contagem_maior > 1:
    print(f'O MAIOR valor {max(valores)} se encontra nas posições ', end='')
    for pos, v in enumerate(valores):
        if v == max(valores):
            print(f'{pos}...', end='')
    print()
elif contagem_maior <= 1:
    print(f'O MAIOR valor {max(valores)} se encontra na posição ', end='')
    for pos, v in enumerate(valores):
        if v == max(valores):
            print(f'{pos}')
if contagem_menor > 1:
    print(f'O MENOR valor {min(valores)} se encontra nas posições ', end='')
    for pos, v in enumerate(valores):
        if v == min(valores):
            print(f'{pos}...', end='')
    print()
elif contagem_menor <= 1:
    print(f'O MENOR valor {min(valores)} se encontra na posição ', end='')
    for pos, v in enumerate(valores):
        if v == min(valores):
            print(f'{pos}')
