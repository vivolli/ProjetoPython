from ex115.backend import *
from ex115.arquivo import *

criar_txt()
while True:
    menu()
    usuario = leia_int('Sua Opcao: ')
    if usuario == 3:
        cabecalho(usuario)
        break
    if usuario == 1:
        ler_pessoas()
    elif usuario == 2:
        cadastrar_pessoas()