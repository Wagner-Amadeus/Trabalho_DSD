import msvcrt
import socket
import threading
from modules import *


def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    nome_cliente = input("Entre com seu nome de usuário: ")

    try:
        cliente.connect(('localhost', 7777))
        cliente.send(nome_cliente.encode('utf-8'))

        print("[1] - Jogar\n[2] - Assistir \n--> ")
        #cliente.send(opcao_de_jogo.encode('utf-8'))
        enviar_mensagem_char_cliente_servidor(cliente)

    except:
        return print("\nNão foi possível se conectar ao servidor\n")

    
    print(f"Usuário {nome_cliente} conectado!\n")


    thread_1 = threading.Thread(target=receiveMessages, args=[cliente])
    thread_2 = threading.Thread(target=sendMessages, args=[cliente, nome_cliente])

    thread_1.start()
    thread_2.start()
    

def receiveMessages(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(f"{msg}\n")
        except:
            print("Não foi possível permanecer conectado ao servidor!\n")
            print("Pressione <enter> para continuar...")
            cliente.close()
            break


def sendMessages(cliente, nome_cliente):
    while True:
        try:
            #os.system('cls')
            letra = msvcrt.getch().decode('utf-8').upper()
            cliente.send(letra.encode('utf-8'))
        except:
            return


def receber_mensagem_string_cliente_servidor(cliente):
    return cliente.recv(1024).decode('utf-8')


def enviar_mensagem_char_cliente_servidor(cliente):
    char = msvcrt.getch().decode('utf-8')
    cliente.send(char.encode('utf-8'))

main()