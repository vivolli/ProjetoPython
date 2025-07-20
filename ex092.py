from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = input('Digite seu nome: ').capitalize().strip()
dados['nasc'] = int(input(f'Digite seu ano de Nascimento, {dados['nome']}: '))
dados['ctps'] = int(input('Ano da contratacao, Carteira de Trabalho (0 caso nao tenha): '))
idade = ano - dados['nasc']
aposentadoria = 65 - idade
if dados['ctps'] == 0:
    print('='*25)
    print(f'Seu nome eh {dados['nome']}!')
    print(f'Voce possui {idade} anos!')
    print('Voce nao possui ctps (0)!')
else:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Seu salario atualmente: '))
    print(f'Seu nome eh {dados['nome']}!')
    print(f'Voce possui {idade} anos!')
    print(f'Sua ctps eh {dados['ctps']}')
    print(f'Seu salario eh igual a R${dados['salario']}')
    if aposentadoria <= 0:
        print('Voce ja pode se aposentar')
    else:
        print(f'Faltam {aposentadoria} anos pra se aposentar')
print(dados)