from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

comprimento_hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O valor do comprimento da hipotenusa é: {comprimento_hipotenusa:.2f}')
