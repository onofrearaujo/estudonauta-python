n = int(input('Digite o número que você quer ver a tabuada: '))

print(f'{f" TABUADA DO {n} ":=^20}')

for x in range(1, 11):
    print(f'{n} x {x:2} = {n * x:3}')
  
print('=' * 20)
