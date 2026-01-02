a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Lista dos 10 primeiros termos da PA:')
an = a1 + (10 - 1) * razao
for pa in range(a1, an + 1, razao):
    print(pa, end=' -> ')

print('ACABOU')
