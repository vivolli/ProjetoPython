from ex108 import moeda
num = float(input('Digite um valor: R$'))
num_ = moeda.conversao(num)
print(f'A metade de {num_} é {moeda.metade(num)}')
print(f'O dobro de {num_} é {moeda.dobro(num)}')
print(f'O valor {num_} aumentado fica {moeda.aumentar(num, 10)}')
print(f'O valor {num_} diminuido fica {moeda.diminuir(num, 1)}')
