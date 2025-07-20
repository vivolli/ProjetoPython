valor_lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valor_lista:
        print('Valor ja consta na lista. Não adicionado!')
    else:
        valor_lista.append(valor)
        print('Numero adicionado com sucesso!')
    continuar = input('Deseja continuar [S/N]: ').upper().strip()
    if continuar in 'S':
        continue
    elif continuar in 'N':
        break
    else:
        print('Opcao invalida, apenas [S/N]')
valor_lista.sort()
print(f'Lista: {valor_lista}')