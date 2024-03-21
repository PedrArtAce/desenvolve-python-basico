import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []
    
    for nome in nomes:
        nome_cript = ''
        for letra in nome:
            codigo = ord(letra)
            if 33 <= codigo <= 126:
                novo_codigo = codigo + chave_aleatoria
                if novo_codigo > 126:
                    novo_codigo = 33 + (novo_codigo - 126)
                nome_cript += chr(novo_codigo)
            else:
                nome_cript += letra
        nomes_cript.append(nome_cript)
    
    return nomes_cript, chave_aleatoria


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print("Chave de criptografia:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)