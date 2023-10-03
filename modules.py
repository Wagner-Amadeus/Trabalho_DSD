import random

palavras_portuguesas = [
    "ALEGRIA",
    "BRINCAR",
    "CORAGEM",
    "SEGREDO",
    "ESCOLHA",
    "SORRISO",
    "AMIZADE",
    "CAMINHO",
    "GARAGEM"
]

# Sorteia uma palavra aleatoriamente
def sorteador_de_palavras(lista=palavras_portuguesas):
    palavra_sorteada = random.choice(lista)
    return palavra_sorteada


# Checa se uma letra já foi testada
def check_de_palavra(letra, letras_ja_descobertas):
    if (letra in letras_ja_descobertas):
        return True
    return False


# Checa se uma letra está contida na palavra
def check_de_letra(letra, palavra):
    return letra in palavra


# Retorna a quantidade de vezes que uma letra aparece em uma palavra
def contar_letras_na_palavra(letra, palavra):
    return palavra.count(letra)


# Retorna a marcação das letras com a palavra
def revela_palavra(palavra, letras_descobertas):
    resultado = ""
    for letra in palavra:
        if letra in letras_descobertas:
            resultado += letra
        else:
            resultado += '?'
    return resultado


# Testa o fim do jogo
def fim_do_jogo(pontos, palavra):
    return pontos != len(palavra)


# ----------------------------------- #
# Funções relativas as comunicações servidor-cliente #
# ----------------------------------- #

def enviar_mensagem_servidor_cliente(cliente, mensagem):
    return cliente.send(mensagem.encode('utf-8'))

def receber_mensagem_char_servidor_cliente(cliente):
    return cliente.recv(1).decode('utf-8')

def receber_mensagem_string_servidor_cliente(cliente):
    return cliente.recv(1024).decode('utf-8')

def enviar_mensagem_cliente_servidor(cliente, mensagem):
    return cliente.send(mensagem.encode('utf-8'))











# ----------------------------------- #
# Funções em avaliação #
# ----------------------------------- #

        # thread = threading.Thread(target=messagesTreatment, args=[cliente])
        # thread.start()



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