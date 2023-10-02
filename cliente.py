import socket  # fornece funcionalidades para criar e gerenciar conexões de rede em Python.
import threading


def main():
    # socket.AF_INET: Especifica a família de endereços IPv4.
    # socket.SOCK_STREAM: Especifica o tipo de soquete (tipo de conexão que será estabelecido), neste caso, SOCK_STREAM representa uma conexão TCP.

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Criado um objeto de soquete (cliente) que usa o <<protocolo TCP>> e a família de endereços <<IPv4>>.
    # Esse objeto de soquete pode ser usado para estabelecer uma conexão com um servidor TCP remoto.

    try:
        # A função connect é usada para iniciar a conexão TCP com o servidor.
        # Tentativa de estabelecer uma conexão com um servidor que está executando na máquina local ("localhost") na porta 7777.
        cliente.connect(('localhost', 7777))
    except:
        return print("\nNão foi possível se conectar ao servidor\n")

    username = input("Entre com seu nome de usuário: ")
    print(f"Usuário {username} conectado!")

    thread_1 = threading.Thread(target=receiveMessages, args=[cliente])
    thread_2 = threading.Thread(target=sendMessages, args=[cliente, username])

    thread_1.start()
    thread_2.start()


def receiveMessages(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            # Tenta receber uma mensagem do servidor usando o método recv do objeto de soquete cliente.
            # O número 2048 representa o tamanho máximo dos dados a serem recebidos em bytes.
            # Após receber a mensagem, a função a decodifica de UTF-8 usando .decode('utf-8') para convertê-la de bytes em uma string legível.
            print(f"{msg}\n")
        except:
            print("Não foi possível permanecer conectado ao servidor!\n")
            print("Pressione <enter> para continuar...")
            cliente.close()
            break


def sendMessages(cliente, username):
    while True:
        try:
            msg = input('\n')
            # O código tenta enviar a mensagem para o servidor usando o objeto de soquete cliente.
            # A mensagem que é enviada ao servidor é uma string que inclui o nome de usuário (username) e a mensagem digitada pelo usuário (msg).
            # Antes de enviar a mensagem, ela é codificada em UTF-8 usando .encode('utf-8'). 
            cliente.send(f"<{username}> {msg}".encode('utf-8'))
        except:
            return


main()