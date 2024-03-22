def validador_senha(senha):
    num = "1234567890"
    força = 0
    cont = 0
    if len(senha) >= 8:
        força+=1
    
    for i in senha:
        if i.isupper():
            força += 1
            break

    for i in senha:
        if not i.isupper():
            cont += 1

    if cont >= 1:
        força += 1     
            
            
    for i in senha:
        if i in num:
            força += 1
            break
    
    for i in senha:
        if not i.isalnum():
            força += 1
            break

    return força

senha = str(input("insira a senha"))

print(validador_senha(senha))