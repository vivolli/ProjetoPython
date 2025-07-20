from time import sleep
print('=' * 30)
sleep(1)
print('Contagem de 1 ate 10 de 1 em 1')
for i in range(1,11):
    sleep(0.7)
    print(i, end=' ')
print('FIM!')
print('=' * 30)
print('Contagem de 10 ate 0 de 2 em 2')
for i in range(10, -1, -2):
    sleep(0.7)
    print(i, end=' ')
print('FIM!')
print('=' * 30)
print('Agora é a sua vez!')
i = int(input('Numero que ira iniciar: '))
sleep(0.5)
f = int(input('Numero que finalizara: '))
sleep(0.5)
p = int(input('Passo que os numeros darao: '))
if i > f:
    p = -p
if p == 0:
    p = 1
def contador(inicio, fim, passo):
    print(f'Contando de {i} ate {f} de {p} em {p}')
    for g in range(inicio, fim, passo):
        sleep(0.7)
        print(g, end=' ')
    print('FIM!')
contador(i,f,p)
