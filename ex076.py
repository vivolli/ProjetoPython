preco = ('Lapis', 12,
         'Mochila', 139.99,
         'Caneta', 1.50,
         'Estojo', 4.90,
         'Marca-texto', 4,
         'Dicionario', 21.75,
         'Compasso', 10,
         'Trasferidor',12.99,
         'Borracha', 2,
         'Livro', 54.99)
for item in range(0, len(preco)):
    if item % 2 == 0:
        print(f'{preco[item]:.<30}', end='')
    if item % 2 == 1:
        print(f'R${preco[item]:.2f}')
