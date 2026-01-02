from datetime import date
maiores = 0
menores = 0

atual = date.today().year

for i in range(7):
    ano = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))
    idade = atual - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
    
print(f'{maiores} pessoas são MAIORES de idade e {menores} são MENORES de idade')
