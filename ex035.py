a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
#Condicao de existencia
if a + b > c and b + c > a and a + c > b:
    print('Os lados acima PODEM formar um triângulo!')
else:
    print('Os lados acima NÃO PODEM formar um triângulo!')