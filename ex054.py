total_maioridade = 0
total_menoridade = 0
from datetime import date
ano = date.today().year
for i in range(1,8):
    nasc = int(input(f'{i}° usuario digite sua data de nascimento: '))
    calculo = ano - nasc
    if calculo >= 21:
        total_maioridade += 1
    elif calculo < 21:
        total_menoridade += 1
print(f'O total de maiores de idade é igual a {total_maioridade}')
print(f'O total de menores de idade é igual a {total_menoridade}')