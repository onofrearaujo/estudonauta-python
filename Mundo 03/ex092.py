from datetime import date

pessoa = {}
ano_atual = date.today().year

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = ano_atual - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho: '))
if pessoa['ctps'] > 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['ano_contratacao'] - (ano_atual - pessoa['idade']) + 35

print('~'*45)
print(pessoa)

for k, v in pessoa.items():
    print(f'{k.replace("_", " ").title()} tem o valor {v}')
