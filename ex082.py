numero = []
par = []
impar = []
while True:
    numero.append(int(input('Digite um numero: ')))
    continuar = input('Deseja continuar [S/N]: ').upper().strip()
    if continuar == 'S':
        pass
    elif continuar == 'N':
        break
    else:
        print('Resposta invalida. Tente novamente')
        pass
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
par.sort(), impar.sort(), numero.sort()
print(f'Lista completa: {numero}')
print(f'Apenas pares: {par}')
print(f'Apenas impares: {impar}')