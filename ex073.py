time_procurado = 'Chapecoense'
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro',
         'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR',
         'Criciúma', 'Atlético Goianiense', 'Cuiabá')
print('BRASILEIRÃO 2024')
print('Primeiros 5 colocados!')
for position in range (5):
    print(f'{position +1}° {times[position]}')
# Outra forma de mostrar sem precisar do +1
#for position, times in enumerate (times[:5], start=1):
#    print(f'{position} {times}')
print('='*30)
print('Ultimos 4 colocados, rebaixados Serie B!')
for ultimos in range(16, len(times)):
    print(f'{ultimos+1}° {times[ultimos]}')
print('='*30)
print('Times em Ordem Alfabetica:')
for time in sorted(times):
    print(time, end=', ')
print('')
print('='*30)
print('Em que posicao esta a Chapecoense?')
if time_procurado in times:
    posicao = times.index('Chapecoense') + 1
    print(f'A Chapecoense esta na posicao {posicao}°')
else:
    print('A Chapecoense nao se encontra no Brasileirao 2024')


