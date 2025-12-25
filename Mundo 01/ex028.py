
from random import randrange

numero_aleatorio = randrange(0, 6)

numero_usuario = int(input('Tente acertar o número gerado: '))

if numero_usuario == numero_aleatorio:
    print(f'Você acertou o número! O número gerado foi {numero_usuario}')
else:
    print(f'Infelizmente você errou o número! O número gerado foi {numero_aleatorio}')
    