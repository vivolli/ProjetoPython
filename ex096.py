def area():
    print('Controle de Terrenos.')
    print('-'*30)
    largura = float(input('Qual o tamanho da largura(m): '))
    comprimento = float(input('Qual o tamanho do comprimento(m): '))
    tamanho = largura * comprimento
    print(f'A area de um terreno {largura}x{comprimento} é de {tamanho}m²')

area()