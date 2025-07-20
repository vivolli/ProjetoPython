from ex109 import moeda
num = float(input('Digite um valor: R$'))
num_ = moeda.conversao(num)
print(f'A metade de {num_} é {moeda.metade(num, True)}')
print(f'O dobro de {num_} é {moeda.dobro(num, True)}')
print(f'O valor {num_} aumentando 10% fica {moeda.aumentar(num, 10, True)}')
print(f'O valor {num_} diminuindo 1% fica {moeda.diminuir(num, 1, True)}')
