while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    
    if n < 0:
        break
    
    for c in range(11):
        resultado = n * c
        print(f'{n} x {c} = {resultado}')
        
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
