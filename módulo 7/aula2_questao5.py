import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    for palavra in palavras:
        if len(palavra) > 3:  
            letras_interiores = list(palavra[1:-1])
            random.shuffle(letras_interiores)
            nova_palavra = palavra[0] + ''.join(letras_interiores) + palavra[-1]
            nova_frase.append(nova_palavra)
        else:
            nova_frase.append(palavra)
    return ' '.join(nova_frase)

