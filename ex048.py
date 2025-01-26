s = 0
c = 0
print('Soma de todos os números múltiplos de 3 a 500.')
for numeros in range(3, 500, 6):
    s += numeros
    if numeros % 3 == 0:
        c += 1
print(f'A soma de todos os números múltiplos de 3 é igual a {s} com {c} de números totais!')