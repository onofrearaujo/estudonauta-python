def escreva(msg):
    tamanho_msg = len(msg) + 4
    print('~' * tamanho_msg)
    print(f'  {msg}  ')
    print('~' * tamanho_msg)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

