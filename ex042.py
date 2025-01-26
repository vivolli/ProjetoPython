a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
if a + b > c and b + c > a and a + c > b:
    print('Podem formar um triangunlo')
    print('Seu triangulo é:')
    if a == b == c:
        print('É Equilátero!')
    elif a != b != c != a:
        print('É Isósceles!')
    else:
        print('É Escaleno!')
else:
    print('Os lados acima NÃO PODEM formar um triângulo!')