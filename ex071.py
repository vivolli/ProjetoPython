print('='*30)
print('{:^30}'.format('BANCO DO DUDU'))
print('='*30)
tot_um = tot_dois = tot_cinco = tot_dez = tot_vinte = tot_cinquenta = tot_cem = tot_duzentos = 0
while True:
    valor = int(input('Quanto você quer sacar: R$'))
    while valor >= 200:
        valor -= 200
        tot_duzentos += 1
    if tot_duzentos > 0 :
        print(f'Você receberá {tot_duzentos} notas de R$200')
    while valor >= 100:
        valor -= 100
        tot_cem += 1
    if tot_cem > 0:
        print(f'Você receberá {tot_cem} notas de R$100')
    while valor >= 50:
        valor -= 50
        tot_cinquenta += 1
    if tot_cinquenta > 0:
        print(f'Você receberá {tot_cinquenta} notas de R$50')
    while valor >= 20:
        valor -= 20
        tot_vinte += 1
    if tot_vinte > 0:
        print(f'Você receberá {tot_vinte} notas de R$20')
    while valor >= 10:
        valor -= 10
        tot_dez += 1
    if tot_dez > 0:
        print(f'Você receberá {tot_dez} notas de R$10')
    while valor >= 5:
        valor -= 5
        tot_cinco += 1
    if tot_cinco > 0:
        print(f'Você receberá {tot_cinco} notas de R$5')
    while valor >= 2:
        valor -= 2
        tot_dois += 1
    if tot_dois > 0:
        print(f'Você receberá {tot_dois} notas de R$2')
    while valor >= 1:
        valor -= 1
        tot_um += 1
    if tot_um > 0:
        print(f'Você receberá {tot_um} moeda de R$1')
    break
