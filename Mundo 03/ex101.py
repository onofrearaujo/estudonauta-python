def voto(ano):
    from datetime import date
    ano_atual = date.today().year

    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif (idade >= 16 and idade < 18) or (idade >= 70):
        return f'Com {idade} anos: VOTO NÃO OBRIGATORIO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


ano_nascimento = int(input('Em que ano você nasceu: '))
print(voto(ano_nascimento))
