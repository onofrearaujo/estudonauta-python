def area(l, a):
    area = l * a
    print(f'A área de um terreno {l}x{a} é de {area}m²')

print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
altura = float(input('ALTURA (m): '))
area(largura, altura)
