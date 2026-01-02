n = int(input('Digite um número inteiro: '))
primo = True

if n <= 1:
    primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False

if primo:
    print('O número é primo ')
