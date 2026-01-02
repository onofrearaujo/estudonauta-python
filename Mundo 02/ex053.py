frase_original = str(input('Digite uma frase: '))
frase = frase_original.replace(' ', '').upper()

inverso = frase[::-1]
      
print(f'O inverso da frase {frase} é {inverso}')
if frase == inverso:
    print(f'A frase {frase_original.upper()} é um palindromo')
else:
    print(f'A frase {frase_original.upper()} - NÃO é um palindromo')
