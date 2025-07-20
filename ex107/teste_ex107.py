from ex107 import moeda
num = float(input('Digite um valor: R$'))
print(f'A metade de {num} eh {moeda.metade(num)}')
print(f'O dobro de {num} eh {moeda.dobro(num)}')
print(f'O numero {num} aumentado fica {moeda.aumentar(num, 10)}')
print(f'O numero {num} diminuido fica {moeda.diminuir(num, 1)}')