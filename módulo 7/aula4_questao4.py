import random

def ler_palavras():
    with open('gabarito_forca.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras


def escolher_palavra(palavras):
    return random.choice(palavras)

def imprimir_progresso(palavra, letras_corretas):
    progresso = ''
    for letra in palavra:
        if letra in letras_corretas:
            progresso += letra + ' '
        else:
            progresso += '_ '
    return progresso

def imprime_enforcado(erros):
    estagios = [
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      /
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |      /
          -
        """,
        """
           _______
          |       |
          |       O
          |       |
          |      /
          -
        """,
        """
           _______
          |       |
          |       O
          |       |
          |       
          -
        """,
        """
           _______
          |       |
          |       O
          |       
          |       
          -
        """,
        """
           _______
          |       |
          |       
          |       
          |       
          -
        """
    ]
    print(estagios[erros])

def main():
    palavras = ler_palavras()
    
    palavra = escolher_palavra(palavras)
    
    letras_corretas = []
    
    tentativas = 0
    
    while tentativas < 6:
        progresso = imprimir_progresso(palavra, letras_corretas)
        print("Palavra:", progresso)
        
        if '_' not in progresso:
            print("Parabéns! Você venceu!")
            break
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas:
            print("Você já escolheu essa letra. Tente outra.")
            continue
        
        if letra in palavra:
            letras_corretas.append(letra)
        else:
            tentativas += 1
            imprime_enforcado(tentativas)
            print("Letra errada. Você tem mais", 6 - tentativas, "tentativas.")
    
    if tentativas == 6:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    main()