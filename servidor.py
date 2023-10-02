import socket
import threading

lista_de_clientes = []

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(('localhost', 7777))
        servidor.listen(2)
    except:
        return print("Não foi possível iniciar o servidor")

    while True:
        cliente, endereco = servidor.accept()
        lista_de_clientes.append(cliente)
        thread = threading.Thread(target=messagesTreatment, args=[cliente])
        thread.start()

def messagesTreatment(cliente):
    while True:
        try:
            msg = cliente.recv(2048)
            broadcast(msg, cliente)
        except:
            deleteCliente(cliente)
            break


def broadcast(msg, cliente):
    for clientItem in lista_de_clientes:
        if clientItem != cliente:
            try:
                clientItem.send(msg)
            except:
                deleteCliente(clientItem)


def deleteCliente(cliente):
    lista_de_clientes.remove(cliente)


main()