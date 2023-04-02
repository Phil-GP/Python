def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo de Forca!***")
    print("*********************************")

    plv_sec = input("Digite a palavra secreta: ").upper()
    for r in range(0, 15):
        print("*********************************")
    plv_rvl = ["_" for i in range(0, len(plv_sec))]
    usadas = []
    enf = 7
    win = len(plv_rvl)
    while enf > 0 and win > 0:
        print("Você já usou: {}".format(usadas))
        print(''.join(plv_rvl))
        chute = input("Escolha uma letra: ").strip().upper()
        if chute in usadas:
            print("Você já chutou a letra", chute)
            continue
        usadas.append(chute)
        if chute in plv_sec:
            index = 0
            for letra in plv_sec:
                if letra == chute:
                    print("Encontrou letra", chute)
                    plv_rvl[index] = chute
                    win -= 1
                index += 1
        else:
            enf -= 1
            desenha_forca(7 - enf)
    if enf > 0:
        imprime_mensagem_vencedor(plv_sec)
    else:
        #print("Puxa, você foi enforcado! A palavra era {}".format(plv_sec))
        imprime_mensagem_perdedor(plv_sec)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(x):
    print("Parabéns, você ganhou! A palavra é", x)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()
