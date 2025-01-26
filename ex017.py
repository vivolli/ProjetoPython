ca = float(input('Digite o valor do cateto adjascente: '))
co = float(input('Digite o valor do cateto oposto: '))
hip = (ca ** 2 + co ** 2) ** (1/2)
print(f'a hipotenusa desses catetos é igual a {hip:.2f}')