numero = int(input('Digite um numero de 0 a 9999: '))

milhar = numero // 1000
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
