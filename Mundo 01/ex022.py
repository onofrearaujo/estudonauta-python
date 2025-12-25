nome_completo = str(input('Digite o seu nome completo: ')).strip()

print(f'Nome Maiúsculas: {nome_completo.upper()}')
print(f'Nome Minúsculas: {nome_completo.lower()}')

print(f'Quantidade de letras(sem contar espaços): {len(''.join(nome_completo.split()))}')
print(f'Quantas letras tem o primeiro nome: {len(nome_completo.split()[0])}')
