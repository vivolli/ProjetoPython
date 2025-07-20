lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar [S/N]: ').upper()
    if resp == 'S':
        pass
    elif resp == 'N':
        break
    else:
        print('Resposta invalida!')
        break
if 5 in lista:
    print('O valor 5 esta na lista!')
else:
    print('O valor 5 nao foi encontrado!')
lista.sort(reverse=True)
print(f'Sua lista decrescente: {lista}')
print(f'A quantidade de numeros digitados foram de: {len(lista)}')