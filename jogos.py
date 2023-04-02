import forca
import adivinhacao

def inicio():
    print("*********************************")
    print("******Escolha um dos Jogos!******")
    print("*********************************")

    if int(input("(1)Adivinhação | (2)Forca:")) == 1:
        print("Adivinhação")
        adivinhacao.jogar()
    else:
        print("Forca")
        forca.jogar()

if(__name__ == "__main__"):
    inicio()
