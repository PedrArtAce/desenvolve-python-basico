ano = int(input("insira o ano em questão: "))
if ((ano % 4) == 0) and ano % 100 != 0 or ano % 400 == 0:
    print("bissexto")
else:
    print("não bissexto")