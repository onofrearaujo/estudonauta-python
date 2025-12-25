dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de km rodados: '))

valor_pagar = (dias * 60) + (km * 0.15)
print(f'O valor total a pagar é: R$ {valor_pagar:.2f} ')
