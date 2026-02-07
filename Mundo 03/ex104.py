def leiaInt(msg):
    while True:
        numero = input(msg).strip()
        if numero.isnumeric():
            return int(numero)
        print('\033[0;31mERRO: Digite um número inteiro válido\033[0;0m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
