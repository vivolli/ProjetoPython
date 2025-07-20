num = int(input('Digite um numero [999 para sair]:'))
count = 0
while num != 999:
    count += num
    num = int(input('Digite um numero [999 para sair]:'))
print(f"A soma de todos os numeros foi de  {count}")