# Minha solucao, ela eh mais logica, funciona porem nao gostei tanto dela entao deixarei a que entendi no video
# matriz_full = [ [], [], [],[], [], [],[], [], [] ]
# contador = 0
# for i in range(1,10):
#     matriz = int(input('Digite um valor: '))
#     matriz_full[contador].append(matriz)
#     contador += 1
# print('='*15)
# print('Sua matriz 3x3:')
# print(f'{matriz_full[0]} {matriz_full[1]} {matriz_full[2]}\n{matriz_full[3]} {matriz_full[4]} {matriz_full[5]}\n{matriz_full[6]} {matriz_full[7]} {matriz_full[8]}')


#Codigo do video com algumas alteracoes, ambos funcionam porem esse eh mais tecnico e legivel por quem entende
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))
print('='*20)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
    print()
