import random
import time
import historia


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
    escolha = input("Pressione qualquer tecla para jogar, pressione X para fechar o jogo")
    if escolha == "x" or escolha == "X":
        return False
        quit()
    else:
        return True


def timer():
    clock = time.time()
    return clock


def endtimer(timer):
    timer = time.time() - timer
    timer = time.strftime("%M:%S", time.gmtime(timer))
    print("Tempo Jogado até sua morte iminente: ", timer)

def endGame(timer):
    timer = time.time() - timer
    timer = time.strftime("%M:%S", time.gmtime(timer))
    print("Tempo decorrido até a sua vitória: ", timer)
    print("")

def batalha(enemyHP, playerHP, atkPlayer, atkNPC):
    turno = random.randint(0, 1)

    if turno == 1:
        print("Você começa atacando")
    else:
        print("O inimigo lhe ataca primeiro ")

    while enemyHP > 0 and playerHP > 0:
        if turno == 1:
            turno -= 1
            # atk = ataquePlayer(atkPlayer)
            dano = random.choice(atkPlayer)
            enemyHP -= dano
            if enemyHP < 0:
                enemyHP = 0
            print("Voce deu {} de dano, o inimigo tem {} de vida".format(dano, enemyHP))
            input("Enter para continuar")

        if turno == 0 and enemyHP > 0:
            turno += 1
            dano = random.choice(atkNPC)
            playerHP -= dano
            if playerHP < 0:
                playerHP = 0
            print(f"O Inimigo lhe causou {dano} de dano, voce ainda tem {playerHP} de vida")

            input("Enter para continuar")

    if enemyHP == 0:
        print(f"Voce Ganhou a batalha, lhe resta {playerHP} de vida")
        return playerHP
        # final da batalha, setar variavel usando esta função

    elif playerHP == 0:
        print(f"Você morreu, o inimigo ainda vive com {enemyHP} de vida")
        time.sleep(3.0)
        return playerHP
        # volta pro começo do jogo


def vantagemRoll():
    vantagem = [0, 1]
    roll = random.choice(vantagem)
    return roll


def batalharandom():
    batalhatrue = random.randint(0, 100)
    return batalhatrue


splashscreen()
start = startjogo()
timer = timer()
playerHP = 100
atkP = [0, 35, 70]
atkNPC = [0, 15, 30]

nome = input("Digite o Nome do Aventureiro >> ")

while start == True:
    historia.intro(nome)
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    # escolhaResult = escolhajogo(escolha)
    etapa1 = historia.etapa1(escolha, nome)

    if etapa1 == 2:
        endtimer(timer)
        start = False
        break

    historia.intro2(nome)
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa2 = historia.etapa2(escolha, nome)
    if etapa2 == 1:
        playerHP -= 30
    elif etapa2 == 2:
        enemyHP = 100
        batalha2 = batalha(enemyHP, playerHP, atkP, atkNPC)
        if batalha2 == 0:
            endtimer(timer)
            start = False
            break
        else:
            playerHP = batalha2
            print(playerHP)
    elif etapa2 == 3:
        enemyHP = 100
        batalha2 = batalha(enemyHP, playerHP, atkP, atkNPC)
        if batalha2 == 0:
            endtimer(timer)
            start = False
            break
        else:
            playerHP = batalha2
            print(playerHP)

    elif etapa2 == False:
        start = False
        break

    historia.intro3()
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa3 = historia.etapa3(escolha)
    if etapa3 == 1:
        playerHP = 100
    elif etapa3 == 2:
        playerHP = 100
    elif etapa3 == 4:
        roll = random.randint(0, 1)
        if roll == 1:
            print("Um Camponês o atinge com uma pedra nas costas")
            print("- 10 de vida")
            playerHP -= 10
        else:
            print("Você consegue fugir sem problemas")

    historia.intro4()
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa4 = historia.etapa4(escolha)
    if etapa4 == 1:
        historia.intro5()
        time.sleep(2.0)
    else:
        historia.intro4_1()
        print("Escolha aqui")
        print("Qual é a sua escolha?")
        escolha = int(input())
        etapa41 = historia.etapa4_1(escolha)
        if etapa41 == 1:
            playerHP = 150
        elif etapa41 == 2:
            enemyHP = 100
            batalha41 = batalha(enemyHP, playerHP, atkP, atkNPC)
            if batalha41 == 0:
                start = False
                endtimer(timer)
                break
            else:
                playerHP = batalha41
        elif etapa41 == 3:
            print()
        elif etapa41 == 4:
            atkP = [0, 60, 85, 100]

        historia.intro5()
        time.sleep(2.0)

    enemyHP = 10
    bossAttack = [0, 30, 60]
    print(enemyHP, playerHP, atkP, bossAttack)

    boss = batalha(enemyHP, playerHP, atkP, bossAttack)

    etapa5 = historia.etapa5(escolha, nome)
    endGame(timer)
    start = False
