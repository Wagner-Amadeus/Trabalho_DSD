import socket
from modules import *

lista_de_clientes = []


def main():

    host = 'localhost'  # Endereço IP do servidor
    port = 7777         # Porta do servidor

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind((host, port))
        servidor.listen(2)
        print("Servidor conectado com sucesso\n")
        print(f"Servidor aguardando conexão em {host}:{port}...\n")
    except:
        return print("Não foi possível iniciar o servidor")

    while True:
        cliente, endereco = servidor.accept()
        nome_cliente = receber_mensagem_string_servidor_cliente(cliente)
        print(f"---> {nome_cliente} Acabou de se conectar ao servidor\n")
        opcao_de_jogo = receber_mensagem_char_servidor_cliente(cliente)
        print(f"Opção numérica do cliente: {opcao_de_jogo}\n")

        lista_de_clientes.append(((nome_cliente),(opcao_de_jogo)))  
        print(f'Imprimindo a lista de {lista_de_clientes}')

        # ---------------------------------------------------------------- #
        # Inicio do jogo
        palavra_secreta = sorteador_de_palavras()
        letras_descobertas = []
        pontos = 0
        chave = False

        while fim_do_jogo(pontos, palavra_secreta):
            print(palavra_secreta)
            enviar_mensagem_servidor_cliente(cliente, revela_palavra(palavra_secreta, letras_descobertas))
            enviar_mensagem_servidor_cliente(cliente, "\nEntre com uma letra: ")
            letra = receber_mensagem_char_servidor_cliente(cliente)
            print(f'A recebida pelo user foi {letra}')

            # A letra já foi testada anteriormente
            if (check_de_palavra(letra, letras_descobertas)):
                enviar_mensagem_servidor_cliente(cliente, f"---> A letra {letra} já foi testada!\n\n")
                
            # A letra está contida na palavra
            else:
                if (check_de_letra(letra, palavra_secreta)):
                    pontos += contar_letras_na_palavra(letra, palavra_secreta)
                    enviar_mensagem_servidor_cliente(cliente, '---> ACERTOU!!\n\n') 
                else:
                    # A letra não está contida na palavra
                    enviar_mensagem_servidor_cliente(cliente, '---> ERROU FEIO, ERROU RUDE !\n\n')
                letras_descobertas.append(letra)
        
        enviar_mensagem_servidor_cliente("Fim do jogo!")
        servidor.close()



            


















        



main()