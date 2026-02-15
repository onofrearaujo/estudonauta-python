from lib.interface import menu
from lib.arquivo import dados

while True:
    opcao = menu.menu_principal()

    if opcao == 1:
        menu.titulo('PESSOAS CADASTRADAS')
        dados.listar_pessoas()
    elif opcao == 2:
        menu.titulo('CADASTRAR NOVA PESSOA')
        dados.cadastrar_pessoa()   
    elif opcao == 3 or opcao is None:
        print('\nFinalizando... Até logo!')
        break 
    else:
        print('\033[31mERRO: Opção Inválida\033[m')
    
