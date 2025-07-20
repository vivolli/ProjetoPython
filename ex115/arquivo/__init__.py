from ex115.backend import cores

def criar_txt():
    from os.path import exists
    if exists('arquivo.txt'):
        pass
    else:
        try:
            with open('arquivo.txt','x') as criar:
                pass
            print('"arquivo.txt" criado com sucesso')
        except FileExistsError:
            pass


def cadastrar_pessoas(nome='', idade=0):
    try:
        nome = input('Digite seu nome: ').strip().title()
        while True:
            idade = int(input(f'Qual sua idade, {nome}: '))
            if 1 <= idade <=128:
                break
        with open('arquivo.txt', 'a') as ler:
            ler.write(f'\n{nome};{idade}')
        print(f'{nome} cadastrada com sucesso!')
    except ValueError:
        pass
    except KeyboardInterrupt:
        print('\n\033[0;31mO usuário encerrou o programa!\033[m')


def ler_pessoas():
    try:
        with open('arquivo.txt', 'r') as f:
            conteudo = f.read()
        linhas = conteudo.split('\n')
        for i, linha in enumerate(linhas):
            if linha.strip() == '':
                continue
            nome, idade = linha.strip().split(';')
            print(f'{i + 1} - {nome:<30} {idade:>3}')
    except (ValueError,TypeError):
        print(cores('vermelho', 'Não há pessoas cadastradas!'.center(35)))
    except KeyboardInterrupt:
        print('\n\033[0;31mO usuário encerrou o programa!\033[m')

