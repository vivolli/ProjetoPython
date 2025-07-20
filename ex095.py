print('=_'*15)
print('       Analise Jogador')
print('=_'*15)
jogadores = []
while True:
    gols_feitos = []
    gols_total = 0
    nome = input('Nome do jogador: ').capitalize().strip()
    partidas = int(input(f'Quantos jogos {nome} jogou: '))
    futebol = {
        'nome':nome,
        'partidas':partidas,
        'gols':gols_feitos,
        'gols_total':gols_total
    }
    for i in range(partidas):
        gol = int(input(f'Quantos gol(s) {nome} fez em seu {i+1} jogo: '))
        gols_feitos.append(gol)
        gols_total += gol
    jogadores.append(futebol)
    while True:
        continuar = input('Deseja continuar [S/N]: ').strip().upper()
        if continuar in 'SN':
            break
        print('Aceito apenas [S/N]')
    if continuar == 'N':
        break
    print('=_' * 15)
print('-' * 40)
print(f'{'Nº':>3} {"Nome":<15} {"Partidas":<10} {"Gols":<20}')
print('-' * 40)
for chave, valor in enumerate(jogadores):
    print(f'{chave+1:>3} {valor["nome"]:<15} {valor["partidas"]:<10} {str(valor['gols']):<15} Total: {sum(valor["gols"])}')
print('='*40)
while True:
    entrada = int(input('Digite o numero do jogador que voce deseja saber as estatisticas (999 encerra): '))
    if entrada == 999:
        print('<<<<<  FIM  >>>>>>')
        break
    quem_deseja_ver = entrada -1
    if quem_deseja_ver >= len(jogadores):
        print('Nao existe jogador com esse numero. Tente novamente.')
    elif 0 <= quem_deseja_ver < len(jogadores):
        jogador = jogadores[quem_deseja_ver]
        print(f'-- Levantamento do jogador {jogador["nome"].upper()}:')
        for i, gols in enumerate(jogador["gols"]):
            print(f'   - Na partida {i + 1}, fez {gols} gol(s)')