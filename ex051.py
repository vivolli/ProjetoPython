from time import sleep
print('-='*8)
print('MATEMATICA / PA')
print('-='*8)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
sleep(1.5)
razao = int(input('Digite a Razao da PA: '))
for count in range(1,11):
    sleep(1)
    formula = primeiro_termo + (count - 1) * razao
    print(formula, end=' → ')
print('Acabou')
