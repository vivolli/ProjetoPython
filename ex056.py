idade_velho = 0
sexo = 0
idade = 0
mulher_menoridade = 0
mulher_maioridade = 0
media_total = 0
media = 0
nome_velho = ''
for s in range (0,4):
    print('='*7,f'Participante {s+1}ª','='*7)
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input(f'Digite sua idade, {nome}: '))
    sexo = str(input(f'Qual seu sexo {nome}, (M/F): ')).strip().lower()
    media += idade
    media_total = media/4
    if idade > idade_velho and sexo == 'm':
        idade_velho = idade
        nome_velho = nome
    if sexo == 'f' and idade < 20:
        mulher_menoridade += 1
    elif sexo == 'f' and idade >= 20:
        mulher_maioridade += 1
print(f'''
A media de idade das quatro pessoas é igual a {media_total:.1f}!
O nome do homem mais velho é {nome_velho} com {idade_velho} anos!
O total de mulheres com menos de 20 anos é igual a {mulher_menoridade} e maiores de 20 anos é {mulher_maioridade}''')