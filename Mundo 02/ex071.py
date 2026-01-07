nome_banco = 'BANCO ON'
print('*' * 30)
print('{:-^30}'.format(f' {nome_banco} '))
print('*' * 30)

# 50, 20, 10, 5, 1

saque = int(input('Qual valor você quer sacar? R$ '))
resto = saque

ced = 50
total_ced = 0
while True:
    if resto >= ced:
        total_ced += 1
        resto -= ced
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_ced = 0
        if resto == 0:
            break
        
print(f'Volte sempre ao {nome_banco}! Tenha um bom dia')
