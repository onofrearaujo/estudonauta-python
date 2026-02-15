def linha(tam=40, elem='-'):
    print(elem * tam)


def titulo(msg):
    linha()
    print(msg.center(40))
    linha()

def menu_principal():
    titulo('MENU PRINCIPAL')

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')

    linha()
    opcao = leiaInt('Sua opção: ')

    return opcao

    
def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[31mERRO: Por favor, digite um valor inteiro válido\033[m')
        except KeyboardInterrupt:
            return None
