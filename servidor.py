import socket
from modules import *

lista_de_clientes = []

host = 'localhost'      # Endereço IP do servidor
port_tcp = 7777         # Porta do servidor
port_udp = 8888         # Porta do servidor


servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    servidor_tcp.bind((host, port_tcp))
    servidor_tcp.listen(4)
    print("\nServidor TCP conectado com sucesso.")
    print(f"Servidor TCP aguardando conexão em <<{host}:{port_tcp}>>...\n")
except:
    print("Não foi possível iniciar o servidor TCP")

try:
    servidor_udp.bind((host, port_udp))
    print("Servidor UDP ativado com sucesso\n\n")
except:
    print("Não foi possível iniciar o servidor UDP")


cliente, endereco = servidor_tcp.accept()
nome_cliente, player_addr = servidor_udp.recvfrom(1024)
nome_cliente = nome_cliente.decode('utf-8')

lista_de_clientes.append(cliente)

print(f"---> {nome_cliente} Acabou de se conectar ao servidor TCP\n")

def jogo(player=nome_cliente):
    palavra_secreta = sorteador_de_palavras()
    letras_descobertas = []
    pontos = 0


    while(fim_do_jogo(pontos, palavra_secreta)):
        print(palavra_secreta)
        cliente.send(str(revela_palavra(palavra_secreta, letras_descobertas)).encode())
        cliente.send(str("\nEntre com uma letra: ").encode())
        letra = cliente.recv(1).decode('utf-8')
        print(f'A recebida por {player.upper()} foi "{letra}"\n')

        # A letra já foi testada anteriormente #
        if (check_de_palavra(letra, letras_descobertas)):
            mensagem = f"---> A letra {letra} já foi testada!\n\n"
            cliente.send(str(mensagem).encode())
        
        # A letra está contida na palavra
        else:
            # Acertou !
            if (check_de_letra(letra, palavra_secreta)):
                pontos += contar_letras_na_palavra(letra, palavra_secreta)
                mensagem = "---> ACERTOU!!\n\n"
                cliente.send(str(mensagem).encode())
            # Errou !
            else:
                mensagem = "---> ERROU FEIO, ERROU RUDE !\n\n"
                cliente.send(str(mensagem).encode())

            letras_descobertas.append(letra)
            
    mensagem = "Fim do jogo!\n"
    cliente.send(str(mensagem).encode())
    servidor_tcp.close()
    servidor_udp.close()

jogo(nome_cliente)
