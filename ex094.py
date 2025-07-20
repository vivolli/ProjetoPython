individuo = []
pessoas = {}
mulheres = []
total_idade  = 0
print('=' * 25)
print('   Cadastro de Pessoas')
print('=' * 25)
while True:
    #Cadastra a pessoa
    nome = input('Digite seu nome: ').capitalize().strip()
    sexo = input(f'Qual seu sexo {nome}, [M/F]: ').strip().upper()
    #Verifica se eh masculino ou feminino
    while sexo not in 'MF':
        sexo = input(f'Por gentileza, so aceitamos [M/F], qual seu sexo {nome}: ')
    idade = int(input(f'Qual sua idade, {nome}: '))
    pessoas[nome] = {'sexo': sexo, 'idade': idade}
    individuo.append(pessoas)
    total_idade += idade
    #Verifica se eh mulher
    if sexo == 'F':
        mulheres.append(nome)
    #Parte de continuar do codigo
    continuar = input('Deseja continuar, [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar, [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    print('=' * 25)
#Oq vai ser mostrado no final, qnd o usuario encerrar o programa
media_idade = total_idade / len(individuo)
print(f'A)  Ao todo {len(individuo)} pessoas foram cadastradas.')
print(f'B)  A media de idade é de {media_idade:.2f} anos')
#Esse codigo das mulheres eh chatinho, mas nada impossivel de se entender
if len(mulheres) == 0:
    print('C)  Nenhuma mulher foi cadastrada')
elif len(mulheres) == 1:
    print(f'C)  O nome da mulher cadastrada é: {mulheres[0]}')
else:
    frase = ''
    for i in range(len(mulheres)):
        if i == len(mulheres) - 1:
            frase += f'e {mulheres[i]}'
        else:
            frase += f'{mulheres[i]}, '
    print(f'C)  O nome das mulheres cadastradas sao: {frase}')
print('D)  Lista das pessoas acima da media: ')
#Esse percorre a lista e caca pessoas com idade maior q a media, bem tranquilo tb
for nome, pessoa in pessoas.items():
    if pessoa['idade'] >= media_idade:
        print(f'nome = {nome}; sexo = {pessoa['sexo']}; idade = {pessoa['idade']}')
print('<<<< FIM >>>>')