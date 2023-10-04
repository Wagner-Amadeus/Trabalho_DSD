import msvcrt
import socket
import threading
from modules import *

host = 'localhost'      # Endereço IP do servidor
port_tcp = 7777         # Porta do servidor
port_udp = 8888         # Porta do servidor

cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nome_cliente = input("Entre com seu nome de usuário: ").upper()

servidor_udp.sendto(nome_cliente.encode(), (host, port_udp))

def receiveMessages(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(f"{msg}\n")
        except:
            print("Não foi possível permanecer conectado ao servidor!\n")
            print("Pressione <enter> para continuar...")
            cliente.close()

def sendMessages(cliente):
    while True:
        try:
            letra = msvcrt.getch().decode('utf-8').upper()
            cliente.send(letra.encode('utf-8'))
        except:
            cliente.close()
        
def jogo():
    print("Iniciando modo jogo...\n")
    cliente_tcp.connect(('localhost', 7777))
    thread_1 = threading.Thread(target=receiveMessages, args=[cliente_tcp])
    thread_2 = threading.Thread(target=sendMessages, args=[cliente_tcp])
    thread_1.start()
    thread_2.start()

jogo()
