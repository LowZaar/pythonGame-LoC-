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


def escolhajogo(escolha):
    if escolha == 1:
        return "1"
    elif escolha == 2:
        return "2"
    elif escolha == 3:
        return "3"
    elif escolha == 4:
        return "4"


def ataquePlayer():
    atkdmg = [0, 35, 70, 100    ]
    atk = random.choice(atkdmg)
    return atk


def ataqueNPC():
    atkdmg = [0, 15, 30]
    atk = random.choice(atkdmg)
    return atk


def batalha(enemyHP, playerHP, turno):
    if turno == 1:
        print("Você começa atacando")
    else:
        print("O inimigo lhe ataca primeiro ")

    while enemyHP > 0 and playerHP > 0:
        if turno == 1:
            turno -= 1
            atk = ataquePlayer()
            enemyHP -= atk
            if enemyHP < 0:
                enemyHP = 0
            print("Voce deu {} de dano, o inimigo tem {} de vida".format(atk, enemyHP))
            input("Enter para continuar")

        if turno == 0 and enemyHP > 0:
            turno += 1
            atkNPC = ataqueNPC()
            playerHP -= atkNPC
            if playerHP < 0:
                playerHP = 0
            print("O Inimigo lhe causou {} de dano, voce ainda tem {} de vida".format(atkNPC,
                                                                                      playerHP))
            input("Enter para continuar")

    if enemyHP == 0:
        print("Voce Ganhou a batalha, lhe resta {} de vida".format(playerHP))
        return playerHP
        # final da batalha, setar variavel usando esta função

    elif playerHP == 0:
        print("Você morreu, o inimigo ainda vive com {} de vida".format(enemyHP))
        time.sleep(3.0)
        return False
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
clockStart = timer()
playerHP = 100


nome = input("Digite o Nome do Aventureiro >> ")

while start:
    historia.intro()
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    # escolhaResult = escolhajogo(escolha)
    etapa1 = historia.etapa1(escolha, nome)
    if etapa1 == False:
        start = False

    historia.intro2(nome)
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa2 = historia.etapa2(escolha)
    if etapa2 == 1:
        playerHP -= 30
    elif etapa2 == 2:
        enemyHP = 100
        batalha(enemyHP, playerHP, 1)
    elif etapa2 == 3:
        enemyHP = 100
        batalha(enemyHP, playerHP, 1)
    elif etapa2 == False:
        start = False

    historia.intro3()
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa3 = historia.etapa3(escolha)
    if etapa3 == 100:
        playerHP = 100


    historia.intro4()
    print("Escolha aqui")
    print("Qual é a sua escolha?")
    escolha = int(input())
    etapa4 = historia.etapa4(escolha)
    if etapa4 is True:
        historia.intro5()
    elif etapa4 is False:
        historia.intro4_1()
        print("Escolha aqui")
        print("Qual é a sua escolha?")
        escolha = int(input())
        etapa41 = historia.etapa4_1(escolha)
        if etapa41 == 1:
            playerHP = 200
        elif etapa41 == 2:
            enemyHP = 100
            batalha(enemyHP, playerHP, 0)
        elif etapa41 == 3: # todo sei la o andrey tem autismo??
            print()
        elif etapa41 == 4:
            playerATK = [ 0, 60, 85, 100]

    historia.intro5()
    enemyHP = 300
    batalha(enemyHP, playerHP, 0)

else:
    print("")
    print("")
    print("")
    startjogo()
