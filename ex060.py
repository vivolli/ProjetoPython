fatorial = int(input('Digite um número: '))
calculo = 1
num = fatorial
print(num, end='')
while num > 1:
    calculo *= num
    num -= 1
    print(' x', num, end='')
print(' =', calculo)
