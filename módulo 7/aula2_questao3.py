while True:
    entrada = input("Digite uma frase (digite 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break

    frase = entrada.lower()
    frase = ''.join(caractere for caractere in frase if caractere.isalnum())

    if frase == frase[::-1]:
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')