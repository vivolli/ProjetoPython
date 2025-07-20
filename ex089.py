from time import sleep
boletim = []
while True:
    print('-'*20)
    nome = input('Seu nome: ').capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    print('-'*20)
    if n1 and n2 > 10 or n1 and n2 < 0:
        print('Numero invalido. Recomece! ')
        print()
        break
    else:
        boletim.append([nome, [n1, n2], media])
    continuar = input('Deseja continuar [S/N]: ').upper()
    if continuar == 'S':
        pass
    elif continuar == 'N':
        print('='*30)
        break
    else:
        print('Error typing.')
        break
print(f'{"Num. ":>4}{"NOME":<10}{"MEDIA":>8}')
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=' * 30)
    aluno_mostrar = int(input('Deseja mostrar a nota de qual aluno: (999 interrompe): '))
    if aluno_mostrar == 999:
        break
    else:
        pass
    sleep(1)
    print('-' * 30)
    print(f'Aluno {boletim[aluno_mostrar][0]} possui as notas: {boletim[aluno_mostrar][1][0]} e {boletim[aluno_mostrar][1][1]}')
print('FIM DO BOLETIM DSO')


