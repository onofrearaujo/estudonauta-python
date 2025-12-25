distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    passagem = 0.50 * distancia
else:
    passagem = 0.45 * distancia

print(f'A sua viagem vai custar {passagem:.2f}')
