import random,time

def startjogo():
    print("Bem-Vindo")
    print("Pressione qualquer tecla para jogar")
    input()
    return True

def escolhajogo(escolha):
    if escolha == 1:
        return 1
    elif escolha == 2:
        return 2
    elif escolha == 3:
        return 3
    elif escolha == 4:
        return 4






start = startjogo()
clockStart = time.time()

while start != False:

    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha1 = int(input())
    escolhaResult = escolhajogo(escolha1)

    if escolhaResult == 1:
        print("Você Morreu")
        start = False
        endClock = time.time() - clockStart
        endClock = time.strftime("%M:%S", time.gmtime(endClock))
        print("Tempo Jogado até sua morte iminente: ", endClock)
        time.sleep(3.0)
        startjogo()
    elif escolhaResult == 2:
        print("Voce Derrotou o Inimigo")
    elif escolhaResult == 3:
        print("O inimigo Escapou")
    elif escolhaResult == 4:
        print("O universo inteiro se despedaça ao seu redor")
    else:
        print("Escolha uma opção válida")







