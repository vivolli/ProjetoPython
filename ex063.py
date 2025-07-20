print('='*20)
print('SEQUENCIA DE FIBONACCI')
print('='*20)
sequencia = 0
termos = int(input('Quantos termos voce deseja mostrar: '))
f_zero = 0
f_um = 1
armazenador = 0
while armazenador < termos:
    variavel = f_zero
    f_zero = f_um
    f_um += variavel
    armazenador +=1
    print(f'{f_zero} → ', end='')
print('FIM')