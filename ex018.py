import math
ang = int(input('Digite um valor de angulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O valor do seno do ângulo de {ang}° é igual a {sen:.2f}°!')
print(f'O valor do cosseno do ângulo de {ang}° é igual a {cos:.2f}°!')
print(f'O valor da tangente o ângulo de {ang}° é igual a {tan:.2f}°!')