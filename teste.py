import msvcrt
import os

from modules import *

palavra_secreta = sorteador_de_palavras()
letras_descobertas = []
pontos = 0

while fim_do_jogo(pontos, palavra_secreta):

    print(palavra_secreta)
    revela_palavra(palavra_secreta, letras_descobertas)
    print("\nInsira uma letra: ")
    letra = msvcrt.getch().decode('utf-8').upper()

    # A letra já foi testada anteriormente
    if (check_de_palavra(letra, letras_descobertas)):
        os.system('cls')
        print(f'A letra {letra} já foi testada!\n\n')
    else:
        # A letra está contida na palavra
        if (check_de_letra(letra, palavra_secreta)):
            pontos += contar_letras_na_palavra(letra, palavra_secreta)
            os.system('cls')
            print('ACERTOU !\n\n')
        
        else:
            # A letra não está contida na palavra
            os.system('cls')
            print('ERROU FEIO, ERROU RUDE !\n\n')
        letras_descobertas.append(letra)

print("Fim de Jogo!")