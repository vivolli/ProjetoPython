num_tupla = []
soma_par = 0
for i in range (1,5):
       num = int(input(f'Digite o {i} numero: '))
       num_tupla.append(num)
       if num % 2 == 0 and num != 0:
              soma_par += 1
print(f'Valores: {num_tupla}')
print(f'O numero 9 apareceu {num_tupla.count(9)} {'vez' if num_tupla.count(9) == 1 else 'vezes'}')
if 3 not in num_tupla:
       print('O valor 3 nao aparece, pois nao foi digitado!')
else:
       print(f'O numero 3 aparece pela primeira vez na posicao {num_tupla.index(3)+1}°')
print(f'A quantidade de numeros pares é igual a {soma_par}')
