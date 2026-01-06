a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Lista dos 10 primeiros termos da PA: ')

c = 0
termo = a1
while c < 10:
    print(termo, end = ' -> ')
    termo += razao
    c += 1
print('ACABOU')
