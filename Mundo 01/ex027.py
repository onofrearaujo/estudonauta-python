nome = str(input('Digite o nome: ')).strip()


nome_split = nome.split()

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {nome_split[0]}')
print(f'Ultimo nome: {nome_split[-1]}')
