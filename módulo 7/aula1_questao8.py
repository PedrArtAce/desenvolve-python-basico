def validar_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numerico) != 11:
        return False

    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(cpf_numerico[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf_numerico[9]) != digito_verificador_1:
        return False

    soma = 0
    multiplicador = 11
    for i in range(10):
        soma += int(cpf_numerico[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf_numerico[10]) != digito_verificador_2:
        return False

    return True

cpf = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")

if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")