import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")
    num_sec = random.randrange(1, 101, 1)
    pontos = 1000
    fim = 5
    tent = 0
    print("Defina a dificuldade:")
    while tent != 1 and tent != 2 and tent != 3:
        tent = int(input("(1)Fácil | (2)Médio | (3)Difícil:"))
    if tent == 1:
        fim = 20
    elif tent == 2:
        fim = 10
    tent = 1
    while tent <= fim:
        print("Rodada {} de {}".format(tent, fim))
        chute = int(input("Digite um número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print("O número precisa ser entre 1 e 100")
            continue
        if num_sec == chute:
            print("Você acertou!")
            break
        elif num_sec < chute:
            pontos = pontos - (chute - num_sec)
            print("Você errou chutando alto. O número é menor que", chute)
        elif num_sec > chute:
            pontos = pontos - (num_sec - chute)
            print("Você errou chutando baixo. O número é maior que", chute)
        tent += 1
    if fim < tent:
        print("Fim do Jogo! O número era {}. Você perdeu :(".format(num_sec))
        pontos = int(pontos / 2)
    else:
        print("Você venceu! O número é {}! \o/ Fim do Jogo!".format(num_sec))
    print("Sua pontuação foi de {} pontos.".format(pontos))

if(__name__ == "__main__"):
    jogar()
