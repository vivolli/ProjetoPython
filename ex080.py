numero = []
for i in range(5):
    num = int(input('Digite um numero: '))
    if i == 0 or num > numero[-1]: # Verifica se o numero eh o primeiou ou o ultimo, e adiciona
        numero.append(num)
    else:
        posicao_element = 0
        while posicao_element < len(numero): # enquanto a variavel for menor que o len de numero:
            if num <= numero[posicao_element]: # se o num(entrada) for menoir que o numero na posicao da lista:
                numero.insert(posicao_element, num) # coloca o numero a posicao onde ele se encontra e depois coloca o numero
                break
            posicao_element += 1
print(f"Sua lista ordenada: {numero}")