count = soma = num = 0
while True:
    soma += num
    num = int(input('Digite um numero [999 para sair]: '))
    if num == 999:
        break
    count += 1
print(f"O somatório de todos os números foram de {soma}. A quantidade de números digitados por voce foram {count}")