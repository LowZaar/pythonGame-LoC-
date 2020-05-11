import random, time


def splashscreen():
    print(r"""\

          ____                  __      ___           _       
         |  _ \                 \ \    / (_)         | |      
         | |_) | ___ _ __ ___    \ \  / / _ _ __   __| | ___  
         |  _ < / _ \ '_ ` _ \    \ \/ / | | '_ \ / _` |/ _ \ 
         | |_) |  __/ | | | | |    \  /  | | | | | (_| | (_) |
         |____/ \___|_| |_| |_|     \/   |_|_| |_|\__,_|\___/ 
                                                      
                                                      
                    """)


def startjogo():
    print("Pressione qualquer tecla para jogar, pressione X para fechar o jogo")
    escolha = input()
    if escolha == "x":
        return False
    else:
        return True


def timer():
    clock = time.time()
    return clock


def endtimer(timer):
    timer = time.time() - timer
    timer = time.strftime("%M:%S", time.gmtime(timer))
    print("Tempo Jogado até sua morte iminente: ", timer)


def escolhajogo(escolha):
    if escolha == 1:
        return 1
    elif escolha == 2:
        return 2
    elif escolha == 3:
        return 3
    elif escolha == 4:
        return 4


def ataquePlayer():
    atkdmg = [0, 35, 70, 100]
    atk = random.choice(atkdmg)
    return atk


def ataqueNPC():
    atkdmg = [0, 15, 20]
    atk = random.choice(atkdmg)
    return atk


def batalha(enemyHP, playerHP):
    turno = 1
    while enemyHP > 0 and playerHP > 0:
        if turno == 1:
            atk = ataquePlayer()
            enemyHP -= atk
            if enemyHP < 0:
                enemyHP = 0

            print("Voce deu {} de dano, o inimigo tem {} de vida".format(atk, enemyHP))
            turno += 1
        if turno == 2 and enemyHP > 0:
            turno -= 1
            atkNPC = ataqueNPC()
            playerHP -= atkNPC
            if playerHP < 0:
                playerHP = 0

            print("O Inimigo lhe causou {} de dano, voce ainda tem {} de vida".format(atkNPC,
                                                                                      playerHP))
    if enemyHP == 0:
        print("Voce Ganhou a batalha, lhe resta {} de vida".format(playerHP))
    elif playerHP == 0:
        print("Você morreu, o inimigo ainda vive com {} de vida".format(enemyHP))
        time.sleep(3.0)
        return False


def batalharandom():
    batalhatrue = random.randint(0, 100)
    return batalhatrue


splashscreen()
start = startjogo()
clockStart = timer()
playerHP = 100

while start:

    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    escolhaResult = escolhajogo(escolha)

    if escolhaResult == 1:
        print("Você Morreu")
        start = False
        endClock = timer() - clockStart
        endClock = time.strftime("%M:%S", time.gmtime(endClock))
        print("Tempo Jogado até sua morte iminente: ", endClock)
        time.sleep(3.0)
        startjogo()
    elif escolhaResult == 2:
        batalhachance = batalharandom()

        if batalhachance <= 65:
            print("Um Inimigo aparece na sua frente, Deseja atacar ou fugir?")
            print("X para escapar")
            escolha = input()
            if escolha != "x":
                enemyHP = 100
                print("Você o ataca")
                batalha = batalha(enemyHP, playerHP)

            if batalha == False:
                start = False

        elif batalhachance >= 66:
            print("Você não encontra nada neste caminho")

    elif escolhaResult == 3:
        print("O inimigo Escapou")

    elif escolhaResult == 4:
        print("O universo inteiro se despedaça ao seu redor")

    else:
        print("Escolha uma opção válida")

else:
    print("")
    print("")
    startjogo()
