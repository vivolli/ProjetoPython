def mensagem(msg):
    print('-'  *35)
    print(str(msg).center(35))
    print('-'  *35)

def cores(cor, texto):
    cores = {
        'branco': f'\033[0;30m',
        'vermelho':f'\033[0;31m',
        'verde':f'\033[0;32m',
        'amarelo': f'\033[0;33m',
        'azul': f'\033[0;34m',
        'roxo': f'\033[0;35m',
        'ciano': f'\033[0;36m',
        'cinza': f'\033[0;37m'
    }
    final = '\033[m'
    return f'{cores.get(cor,'')}{texto}{final}'

def leia_int(y):
    while True:
        try:
            num = int(input(y))
            if 1 <= num <= 3:
                return num
            else:
                print(f'{cores('vermelho','Digite uma opção válida (entre 1 e 3)')}')
        except KeyboardInterrupt:
            print('\n'f'{cores('vermelho','O usuário encerrou o programa')}')
            return None
        except (ValueError, TypeError):
            print(f'{cores('vermelho','Digite um número inteiro válido')}')

def cabecalho(x):
    escolha_usuario = ['PESSOAS CADASTRADAS', 'CADASTRO DE PESSOA']
    if x == 1:
        mensagem(escolha_usuario[0])
    elif x == 2:
        mensagem(escolha_usuario[1])
    elif x == 3:
        mensagem(f'{cores('vermelho', 'FIM DO PROGRAMA')}'.center(45))



def menu():
    mensagem('MENU PRINCIPAL')
    print(f'''{cores('roxo','1')} - {cores('verde','Ver pessoas cadastradas')}
{cores('roxo', '2')} - {cores('verde', 'Cadastrar nova pessoa ')}
{cores('roxo', '3')} - {cores('verde', 'Sair do sistema')}''')
    print('-'  * 35)

