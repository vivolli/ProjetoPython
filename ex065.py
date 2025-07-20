count = contabilizador_numeros = media = menor = maior = 0
resposta = 'S'
numero = []
while resposta == 'S':
    num = int(input('Digite um numero: '))
    resposta = str(input('Quer continuar [S/N]')).upper().strip()
    contabilizador_numeros += 1
    numero.append(num)
    count += num
    media = count/contabilizador_numeros
    maior = max(numero)
    menor = min(numero)
print(f'A quantidade de numeros informados foi de {contabilizador_numeros}. A soma foi de {count} e a media foi {media:.2f}!')
print(f"O maior numero foi {maior} e o menor foi {menor}!")
print('Fim')