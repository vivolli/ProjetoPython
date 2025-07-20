lista = []
soma = soma_mil = menor = 0
while True:
    print('='*30)
    produto = input('Digite o nome do produto: ').capitalize()
    valor = float(input('Digite o valor do produto: '))
    soma += valor
    lista.append((produto, valor))
    menor = min(lista, key=lambda item: item[1])
    print('='*30)
    if valor >= 1000:
        soma_mil += 1
    while True:
        pergunta = input('Deseja continuar [S/N]: ').upper().strip()
        if pergunta == 'N':
            break
        elif pergunta == 'S':
           break
    if pergunta == 'N':
        break
print('Fim do atendimento, obrigado por comprar conosco!')
print(f'O total da compra foi de R${soma:.2f}!')
print(f'No total temos {soma_mil} custando mais de R$1000.')
print(f'O valor do menor produto foi do(a) {menor[0]} custando R${menor[1]:.2f}')