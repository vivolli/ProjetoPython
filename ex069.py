count_idade = qtd_homens = count_idade_mulheres = idade = 0
sexo = ''
while True:
    print('='*30)
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    while True:
        sexo = str(input(f'Digite o seu Sexo, {nome} [M/F]: ')).upper().strip()
        if sexo in ['M' ,'F']:
            break
    while True:
        idade = int(input(f'Digite sua idade, {nome}: '))
        if 1 <= idade <= 129:
            break
    if sexo == 'M':
        qtd_homens+= 1
    if idade >= 18:
        count_idade += 1
    if sexo == 'F' and idade < 20:
        count_idade_mulheres +=1
    print('='*30)
    while True:
        continuar = str(input('Voce deseja cadastrar mais pessoas?[S/N] ')).upper()
        if continuar == 'S' or continuar == 'N':
             break
        print('='*30)
        print("Entrada inválida! Digite 'S' para sim ou 'N' para não.")
        print('='*30)
    if continuar == 'N':
            print('Obrigado por participar!')
            break
print(f'Total de homens cadastrados: {qtd_homens}')
print(f'Pessoas com 18 anos ou mais: {count_idade}')
print(f'Mulheres com menos de 20 anos: {count_idade_mulheres}')
