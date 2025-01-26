from datetime import date
sexo = str(input('''INFORME SEU SEXO
[ 1 ] MASCULINO
[ 2 ] FEMININO
INFOME AQUI: '''))
if sexo == '2':
    print('Você nao precisa se alistar, tenha um Bom Dia!')
else:
    data = int(input('Digite seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - data
    if idade == 18:
        print(f'Se você nasceu em {data}, nesse ano fara {idade}, você têm que se alistar!')
        print('Esse é o seu ano de se alistar, Boa Sorte!')
    elif idade < 18:
        print(f'Se você nasceu em {data}, nesse ano fara {idade} anos.')
        print('Esse não é o seu ano de se alistar!')
        print(f'Seu alistamento esta previsto para {ano-(ano-(data + 18))}, quando nesse ano você completará 18 anos!')
    elif idade > 18:
        print(f'Se voce nasceu em {data}, nesse ano completara {idade} anos.')
        print('Seu ano de alistamento ja passou!')
        print(f'Voce deveria ter se alistado em {ano - ((ano-data)-18)}.')