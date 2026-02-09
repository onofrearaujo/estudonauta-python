cores = (
    '\033[m',
    '\033[42m',
    '\033[44m',
    '\033[41m',
    '\033[7;30m'
)

def msgPersonalizada(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')

def pyHelp():
    while True:
        msgPersonalizada('SISTEMA DE AJUDA PyHelp', 1)
        funcao = input('Função ou Biblioteca > ').strip().lower()
        
        if funcao == 'sair':
            msgPersonalizada('ATÉ LOGO!', 3)
            break
            
        msgPersonalizada(f'Acessando o manual do comando "{funcao}"', 2)
        print(cores[4], end='')
        help(funcao)
        print(cores[0], end='')

pyHelp()
