frase = str(input('Digite uma frase: ')).strip()

print(
f"""A letra A aparece {frase.upper().count('A')} vezes na frase.
Ela aparece primeiro na posição {frase.upper().find('A')}
Ela aparece a última vez na posição {frase.upper().rfind('A')}""")
