# Matriz
par = coluna3 = 0
linha = coluna = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha} , {coluna}]: '))
print('=' * 20)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
    print()
# Soma dos pares
matriz_extenso = [extenso for completo in matriz for extenso in completo]
for num in matriz_extenso:
    if num % 2 == 0:
        par += num
print(f'Soma dos valores pares: {par}')
# Soma dos valores da terceira coluna
print(f'Soma dos valores da teceira coluna : {matriz_extenso[2] + matriz_extenso[5] + matriz_extenso[8]}')
# Maior valor 2 coluna
segunda_linha_maior = max(matriz_extenso[3:6])
print(f'Maior valor da segunda linha: {segunda_linha_maior}')

# Na parte de somar a terceira coluna ele usa
#for l in range(0, 3):
#   x += matriz [linha] [2]