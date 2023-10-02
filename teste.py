import jogo
import os
import msvcrt


palavra_secreta = jogo.sorteador_de_palavras()
letras_descobertas = []
pontos = 0

while jogo.check_de_fim_do_jogo(pontos, palavra_secreta):

    print(palavra_secreta)
    jogo.revela_palavra(palavra_secreta, letras_descobertas)
    print("\nInsira uma letra: ")
    letra = msvcrt.getch().decode('utf-8').upper()

    # A letra já foi testada anteriormente
    if (jogo.check_de_palavra(letra, letras_descobertas)):
        os.system('cls')
        print(f'A letra {letra} já foi testada!\n\n')
    else:
        # A letra está contida na palavra
        if (jogo.check_de_letra(letra, palavra_secreta)):
            pontos+=jogo.contar_letras_na_palavra(letra, palavra_secreta)
            os.system('cls')
            print('ACERTOU !\n\n')
        
        else:
            # A letra não está contida na palavra
            os.system('cls')
            print('ERROU FEIO, ERROU RUDE !\n\n')
        letras_descobertas.append(letra)

print("Fim de Jogo!")