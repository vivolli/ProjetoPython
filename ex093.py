gols_feitos = []
gols_total = 0
nome = input('Nome do jogador: ').capitalize().strip()
partidas = int(input(f'Quantos jogos {nome} jogou: '))
futebol = {
    'nome':nome,
    'partidas':partidas,
    'gols':gols_feitos
}
for i in range(partidas):
    gol = int(input(f'Quantos gol(s) {nome} fez em seu {i+1} jogo: '))
    gols_feitos.append(gol)
    gols_total += gol
print('='*50)
print(futebol)
print('='*50)
for key, value in futebol.items():
    print(f'O campo {key} tem o valor {value}')
print('='*50)
print(f'O jogador {nome} jogou {partidas} jogos.')
for i, jogos in enumerate(gols_feitos):
    print(f'   - Na partida {i+1} {nome} fez: {jogos} gols')
print(f'{nome} fez um total de {gols_total} gol(s).')