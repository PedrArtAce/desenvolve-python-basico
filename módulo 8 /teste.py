
def aaaa(string):
    contagem = { }
    for char in string:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem
    
x = aaaa("fdafdlafjdssa")
print (x)