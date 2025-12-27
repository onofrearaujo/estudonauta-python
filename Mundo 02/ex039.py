from datetime import date
sexo = str(input('Digite o sexo do jovem M / F: ')).strip().upper()


if sexo == 'M':
    ano_nascimento = int(input('Digite o ano de nascimento do jovem: '))

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    idade_minima = 18

    print(f'Quem nasceu em {ano_nascimento} tem atualmente {idade} anos em {ano_atual}.')
    ano_alistamento = ano_nascimento + idade_minima

    if idade < idade_minima:
        print(f'Você pode se alistar a partir dos {idade_minima} anos - falta {idade_minima - idade} anos para você poder se alistar.')
        print(f'Seu alistamento será em {ano_alistamento}.')
    elif idade > idade_minima:
        print(f'Você está em atraso de {idade - idade_minima} anos com o serviço de alistamento militar.')
        print(f'Seu alistamento foi em {ano_alistamento}')
    else:
        print('Você deve se alistar IMEDIATAMENTE!')
elif sexo == 'F':
    print('Você não precisa fazer o alistamento obrigatório.')
else:
    print('Sexo inválido.')
