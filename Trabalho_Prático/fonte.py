import os
import sys


#funções

def registro():
    while True:
        print ("\n")
        print("REGISTRO \n")
        usuario = input("Insira um usuário: ")
        pwd = input("Insira a senha: ")
        conf_pwd = input("Confirme a senha: ")
        tipo = int(input("Insira o seu tipo de usuário (1 - usuário, 2 - administrador): "))
        if tipo != 1 and tipo != 2:
            print("Tipo inválido \n")
            tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não): "))
            if tentar == 2:
                print("Encerrando o programa.")
                sys.exit()
            if tentar == 1:
                continue
            
          
        if conf_pwd == pwd:
            with open("info.txt", "a") as f:  
                f.write(usuario + ":" + pwd +  ":" + str(tipo) + "\n")
            print("Registrado com sucesso!")
            return tipo
        else:
            print("\n")
            print("Senhas diferentes!")
            tentar = input("Tentar de novo? (1 - Sim, 2 - Não): ")
            if tentar == '2':
                print("Encerrando o programa.")
                sys.exit()

def login():
    while True:
        print ("\n")
        print("LOGIN \n")
        usuario = input("Insira o usuário: ")
        pwd = input("Insira a senha: ")
        with open("info.txt", "r") as f:
            for linha in f:
                stored_usuario, stored_pwd, tipo = linha.strip().split(":")
                if usuario == stored_usuario and pwd == stored_pwd:
                    print("Login bem-sucedido!")
                    return int(tipo)
                
            print("\n")
            print("Usuário ou senha incorretos!")
            tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não): "))
            if tentar == 2:
                break
            elif tentar == 1:
                continue
    return 0

def editar_pedido(arquivo, pedido, destino, cidadeatual, previsão, status):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    for i, linha in enumerate(linhas):
        if str(pedido) in linha:
            linhas[i] = pedido + ":" + destino + ":" + cidadeatual + ":" + previsão + ":" + status + '\n'
            break  
    with open(arquivo, 'w') as f:
        f.writelines(linhas)


def editar_usuario(arquivo, usuario, senha, tipo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    for i, linha in enumerate(linhas):
        if str(usuario) in linha:
            linhas[i] = usuario + ":" + senha + ":" + tipo + '\n'
            break  
    with open(arquivo, 'w') as f:
        f.writelines(linhas)


#programa

print("\n")
print("GEN ERIOCHO CORREIOS \n")

print("Login - 1")
print("Registrar - 2 \n")

opção = input("Escolha a opção de entrada: ")

tipo_usuario = 0

if opção == "1":
    tipo_usuario = login()
elif opção == "2":
    tipo_usuario = registro()
else:
    print("Opção inválida!")
    sys.exit()
print("\n")





if tipo_usuario == 1:
    print("Você está navegando como usuário")
elif tipo_usuario == 2:
    print("Você está navegando como administrador")

print("\n")


#usuario 
if tipo_usuario == 1:
    while True:

        
        print("\n")
        print("MENU")
        print("\n")
        print("1 - Acompanhar pedido")
        print("2 - Agencias para retirada de produtos \n")

        opção = int(input("Escolha entre as opções: "))

        #acompanhar
        if opção == 1:
            while True:
                print("\n")
                print("ACOMPANHAMENTO DE PEDIDO \n")
                pedido = input("insira o numero do pedido: ")
                existe = 0
                with open("pedidos.txt", "r") as a:
                    for linha in a:
                        stored_pedido, destino, cidade_atual , previsão, status = linha.strip().split(":")
                        if pedido == stored_pedido:
                            existe = 1 
                            print("\n")
                            print(f"Pedido numero: {pedido} \n")
                            print(f"Destino: {destino}")
                            print(f"O pacote se encontra em: {cidade_atual}")
                            print(f"Previsão: {previsão}")
                            print(f"Status: {status} ")
                            print("\n", "\n")
                            break

                if existe == 1:
                    resposta = int(input("retornar ao menu? (1 - sim, 2 - Finalizar programa): "))
                    if resposta == 1:
                            
                        break

                    if resposta == 2:
                        print("Encerrando o programa.")
                        sys.exit()
                        
                            


                if existe == 0:
                    print("\n")
                    print("O pedido não foi encontrado no sistema :()")

                    tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não, 3 - Finalizar o programa): "))
                    if tentar == 3:
                        print("encerrando programa!")
                        sys.exit()
                    if tentar == 2:
                        break
                    elif tentar == 1:
                        continue
                                             
        #agencia                    
        if opção == 2:
            print("\n")
            print ("AGENCIAS \n")
            agencias = []
            with open("agencias.txt", "r") as a:
                for linha in a:
                    agencias.append(linha.strip().split(":"))

        
            print("Minas Gerais\n")
            for agencia in agencias:
                if agencia[1].upper() == "MG":
                    print("-----------------------------------------------------------------------------------------------")
                    print("-",agencia[0], "|", agencia[2], "|", f"Bairro: {agencia[3]}","|", f"Rua: {agencia[4]}")
                    print("-----------------------------------------------------------------------------------------------")
            print("\n\n")

            print("São Paulo\n")
            for agencia in agencias:
                if agencia[1].upper() == "SP":
                    print("-----------------------------------------------------------------------------------------------")
                    print("-",agencia[0], "|", agencia[2], "|", f"Bairro: {agencia[3]}","|", f"Rua: {agencia[4]}")
                    print("-----------------------------------------------------------------------------------------------")
            print("\n\n")

            print("Rio de Janeiro\n")
            for agencia in agencias:
                if agencia[1].upper() == "RJ":
                    print("-----------------------------------------------------------------------------------------------")
                    print("-",agencia[0], "|", agencia[2], "|", f"Bairro: {agencia[3]}","|", f"Rua: {agencia[4]}")
                    print("-----------------------------------------------------------------------------------------------")
            print("\n\n")
            resposta = int(input("retornar ao menu? (1 - sim, 2 - Finalizar programa): "))
            if resposta == 1:
                continue

            if resposta == 2:
                print("Encerrando o programa.")
                sys.exit()


#administrador
elif tipo_usuario == 2:
    while True:
        print("\n")
        print("MENU")
        print("\n")
        print("1 - Editar status de um pedido")
        print("2 - Adicionar um pedido ")
        print("3 - Deletar um pedido ")
        print("4 - Editar usuario ")
        print("5 - Deletar usuario \n")

        opção = int(input("Escolha entre as opções: "))


        #editar
        if opção == 1:
            while True:
                existe = 0
                print("\n")
                print("EDIÇÃO DE STATUS")
                pedido = input("insira o pedido a ser atualizado: ")

                with open("pedidos.txt", 'r') as pedidos:
                    for linha in pedidos:
                        stored_pedido, destino, cidade_atual , previsão, status = linha.strip().split(":")
                        if stored_pedido == pedido:
                            existe = 1
                            cidade_atual = input("\nInsira a cidade em que se encontra o pedido: ")
                            status = input("insira o status atual do pedido: ")
                            editar_pedido("pedidos.txt", pedido, destino, cidade_atual, previsão, status)
                            print("\nPedido atualizado!\n")
                            break
                


                if existe == 1:
                    resposta = int(input("retornar ao menu? (1 - sim, 2 - Finalizar programa): "))
                    if resposta == 1:
                            
                        break

                    if resposta == 2:
                        print("Encerrando o programa.")
                        sys.exit()

                if existe == 0:
                    print("\n")
                    print("O pedido não foi encontrado no sistema:")

                    tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não, 3 - Finalizar o programa): "))
                    if tentar == 3:
                        print("encerrando programa!")
                        sys.exit()
                    if tentar == 2:
                        break
                    elif tentar == 1:
                        continue

        #adicionar                    
        elif opção == 2:

            while True:
                print("\n")
                print("ADICIONAR PEDIDOS\n")

                pedido = input("Insira o numero do pedido: ")
                destino = input("Insira o destino: ")
                cidade_atual = input("Insira a cidade onde se encontra: ")
                previsão = input("Insira a previsão de entrega: ")
                status = input("Insira o status do pedido: ")

                with open("pedidos.txt", "a") as f:  
                    f.write(pedido + ":" + destino +  ":" + cidade_atual + ":" + previsão + ":" + status + "\n")
                print("Adicionado com sucesso!")

                resposta = int(input("Adicionar mais pedidos? (1 - sim, 2 - não, 3 - finalizar programa): "))
                if resposta == 1:
                    continue    

                elif resposta == 2:
                    break


                elif resposta == 3:
                    print("Encerrando o programa.")
                    sys.exit()            

        #deletar
        elif opção == 3:
            while True:
                print("\n")
                print("DELETAR PEDIDO \n")
                pedido = input("Insira o pedido a ser deletado: ")
                novas_linhas = []
                with open("pedidos.txt", 'r') as pedidos:
                    for linha in pedidos:
                        if pedido not in linha:
                            novas_linhas.append(linha)
                if len(novas_linhas) < 1:
                    print("\n")
                    print("O pedido não foi encontrado no sistema:")

                    tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não, 3 - Finalizar o programa): "))
                    if tentar == 3:
                        print("encerrando programa!")
                        sys.exit()
                    if tentar == 2:
                        break
                    elif tentar == 1:
                        continue
                else:
                    with open("pedidos.txt", 'w') as file:
                        for line in novas_linhas:
                            file.write(line)

                    print("Pedido(s) deletado(s) com sucesso.")
                
                
                resposta = int(input("Deseja continuar deletando pedidos? (1 - sim, 2 - não, 3 - finalizar programa): "))
                if resposta == 1:
                    continue
                if resposta == 2:
                    break
                if resposta == 3:
                    print("encerrando programa!")
                    sys.exit()
                
        #editar usuario
        elif opção == 4:
            while True:
                existe = 0
                print("\n")
                print("EDIÇÃO DE USUARIOS")
                temp_usuario = input("insira o usuario: ")

                with open("info.txt", 'r') as pedidos:
                    for linha in pedidos:
                        stored_usuario, stored_senha, stored_tipo_usuario = linha.strip().split(":")
                        if stored_usuario == temp_usuario:
                            existe = 1
                            nova_senha = input("\nInsira a senha nova: ")
                            novo_tipo = input("insira o tipo do usuario: ")
                            editar_usuario("info.txt", temp_usuario, nova_senha, novo_tipo)
                            print("\nUsuario atualizado!\n")
                            break
                


                if existe == 1:
                    resposta = int(input("retornar ao menu? (1 - Sim, 2 - Não 3 - Finalizar programa): "))
                    if resposta == 1:
                        break

                    elif resposta == 2:
                        continue

                    elif resposta == 3:
                        print("Encerrando o programa.")
                        sys.exit()

                if existe == 0:
                    print("\n")
                    print("O pedido não foi encontrado no sistema:")

                    tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não, 3 - Finalizar o programa): "))
                    if tentar == 3:
                        print("encerrando programa!")
                        sys.exit()
                    if tentar == 2:
                        break
                    elif tentar == 1:
                        continue

        #deletar usuario
        elif opção == 5:
            while True:
                print("\n")
                del_usuario = input("Insira o usuario a ser deletado: ")
                novas_linhas = []
                with open("info.txt", 'r') as usuarios:
                    for linha in usuarios:
                        if del_usuario not in linha:
                            novas_linhas.append(linha)
                if len(novas_linhas) < 1:
                    print("\n")
                    print("O usuario não foi encontrado no sistema:")

                    tentar = int(input("Tentar de novo? (1 - Sim, 2 - Não, 3 - Finalizar o programa): "))
                    if tentar == 3:
                        print("encerrando programa!")
                        sys.exit()
                    if tentar == 2:
                        break
                    elif tentar == 1:
                        continue
                else:
                    with open("info.txt", 'w') as file:
                        for line in novas_linhas:
                            file.write(line)

                    print("Pedido(s) deletado(s) com sucesso.")
                
                
                resposta = int(input("Deseja continuar deletando usuarios? (1 - sim, 2 - não, 3 - finalizar programa): "))
                if resposta == 1:
                    continue
                if resposta == 2:
                    break
                if resposta == 3:
                    print("encerrando programa!")
                    sys.exit()
                    
    

           


                
                            





                        


                    



    