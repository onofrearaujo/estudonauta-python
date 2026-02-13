def leiaDinheiro(txt):
    while True:
        valor = input(txt).replace(',', '.').strip()
        if not valor.isalpha() and valor != '':
            break
        print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
    return float(valor)

