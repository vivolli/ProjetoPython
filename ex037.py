numero_base = int(input('Digite um valor inteiro: '))
print('''Digite um valor para conversao:
[ 1 ] PARA BINARIO
[ 2 ] PARA OCTAL
[ 3 ] PARA HEXADECIMAL''')
escolha = int(input('Digite a sua escolha: '))
if escolha == 1:
    print(f'O valor {numero_base}, em BINARIO vira {bin(numero_base)[2:]}')
elif escolha == 2:
    print(f'O valor {numero_base}, em OCTAL vira {oct(numero_base)[2:]}')
elif escolha == 3:
    print(f'O valor {numero_base}, em HEXADECIMAL vira {hex(numero_base)[2:]} ')
else:
    print(f'Nao existe opcao {escolha}. Tente novamente.')