from datetime import date
idade = int(input('Digite o ano de nascimento do atleta: '))

idade_atual = date.today().year - idade

if idade_atual <= 9:
    categoria = 'MIRIM'
elif idade_atual <= 14:
    categoria = 'INFANTIL'
elif idade_atual <= 19:
    categoria = 'JUNIOR'
elif idade_atual <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'De acordo com a idade do atleta: {idade_atual} anos, a categoria dele se encaixa em - {categoria}')
