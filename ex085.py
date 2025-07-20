valores = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite o {i} numero: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Pares: {valores[0]}\nImpares: {valores[1]}')
# Especificar qual lista ira receber qual valor necessita colocar seu indice na frente:
# Ex:
# Valores[0] -> indica que na primeira lista sera adicionado os valores que eu indicar



