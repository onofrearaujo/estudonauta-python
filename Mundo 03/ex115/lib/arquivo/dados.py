from lib.interface.menu import leiaInt 
nome_arquivo = 'dados.txt'

def cadastrar_pessoa():
    nome = validar_nome()
    if nome is None:
        return
    idade = validar_idade()
    if idade is None:
        return

    adicionar_dados(nome, idade)


def validar_nome():
    while True:
        try:
            nome = input('Digite o nome: ').strip()

            if nome:
                return nome
            else:
                print('\033[31mERRO: O nome não pode está vazio\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mERRO: Infelizmente não é possivel fazer o cadastro com o nome vazio!\033[m')
            return None


def validar_idade():
    while True:
        idade = leiaInt('Digite a idade: ')
        if idade is None:
            print('\n\033[31mERRO: Infelizmente não é possivel fazer o cadastro com a idade vazia!\033[m')
            return None

        if idade >= 0:
            return idade

        print('\033[31mERRO: A idade deve ser igual ou maior que 0\033[m')


def adicionar_dados(nome, idade):
    try:
        with open(nome_arquivo, 'a') as f:
            f.write(f'{nome};{idade}\n')
        
        print(f'\033[32mSUCESSO: Novo registro de {nome} adicionado.\033[m')
    except Exception:
        print(f'\033[31mERRO: {nome} não foi adicionado.\033[m')

def listar_pessoas():
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split(';')
                if len(partes) == 2:
                    nome, idade = partes 
                    print(f'{nome:<30} | {idade:>3} anos')

    except FileNotFoundError:
        print('\033[31mNenhuma pessoa cadastrada ainda.\033[m')

