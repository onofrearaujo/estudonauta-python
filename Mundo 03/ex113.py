def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar esse número\033[m')
            return 0
        else:
            return num

valor_int = leiaInt('Digite um inteiro: ')
valor_float = leiaFloat('Digite um Real: ')

print(f'\033[32mO valor inteiro digitado foi {valor_int} e o real foi {valor_float}\033[m')
