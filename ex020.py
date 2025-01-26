from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
variavel = [n1, n2, n3, n4]
shuffle(variavel)
print('A ordem se apresentação será:')
print(variavel)
