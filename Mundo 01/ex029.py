radar = int(input('Velocidade do carro em Km/h: '))

if radar > 80:
    velocidade_acima = radar - 80
    valor_multa = velocidade_acima * 7
    print(f'A sua velocidade é {velocidade_acima}Km/h acima do radar de {radar}Km/h')
    print(f'Você foi multado em R$ {valor_multa}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
    