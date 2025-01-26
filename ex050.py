soma = 0
for numeros in range(1,7):
    num = int(input(f'Digite o {numeros} número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares é igual a {soma}')