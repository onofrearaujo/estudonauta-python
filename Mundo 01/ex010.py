real = float(input('Digite quanto você tem em reais: '))
dolar = real / 5.41
euro = real / 6.35

print(f'Você tem R${real:.2f} e pode comprar:')
print(f'Dolar U${dolar:.2f}')
print(f'Euro E{euro:.2f}')
