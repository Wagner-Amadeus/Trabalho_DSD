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
            resultado+=letra
        else:
            resultado+='*'
    print(resultado)


# Testa o fim do jogo
def check_de_fim_do_jogo(pontos, palavra):
    return pontos != len(palavra)