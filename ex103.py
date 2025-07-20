def ficha(nome= '', gols=0):
    print('^'*30)
    nome = input('Digite o nome do jogador: ').capitalize().strip()
    gols = input('Quantos gol(s): ')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s)!')
    return nome, gols

ficha()