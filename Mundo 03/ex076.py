produtos = ('Notebook', 3500, 'Teclado Mecânico', 140, 'Fone de ouvido', 86, 'Mouse sem fio', 75)

print('-' * 45)
print(f"{'LISTAGEM DE PREÇOS':^45}")
print('-' * 45)

for p in range(0, len(produtos), 2):
    print(f"{produtos[p]:.<35}R${produtos[p + 1]:>8.2f}")
    
print('-' * 45)
