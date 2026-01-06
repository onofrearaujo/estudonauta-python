a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

c = 0
termo = a1
quantidade = 10
total = 0

while quantidade != 0:
    total += quantidade
    while c < total:
        print(termo, end = ' -> ')
        termo += razao
        c += 1
        
    print('PAUSA')
    quantidade = int(input('Quantos termos você quer mostrar a mais? : '))

print(f'Progressão finalizada com {total} termos mostrados.')
