from time import sleep
print('-='*8)
print('MATEMATICA / PA')
print('-='*8)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
sleep(1.5)
razao = int(input('Digite a Razao da PA: '))
termo = primeiro_termo
cont = 1
total  = 0
mais = 10
while mais != 0:
    total += mais
    while cont <=total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('Acabou...')
    sleep(1.5)
    mais = int(input('Quantos termos a mais voce quer mostrar (Digite 0 para sair!): '))
print(f'Finalizado com {total} termos no total!')

