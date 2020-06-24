import random


def intro(name):
    print("há séculos, em uma pequena vila chamada Northbury, o Lord Blackbird, a mando do rei")
    print("chamou o aventureiro " + name + " para uma missão perigosa.")
    print("O Lord deu duas opções ao aventureiro")
    print("1 – aceitar a missão que lhe foi dada")
    print("2 – sofrer as consequencias de não seguir as ordens do rei")


def etapa1(escolha, name):
    if escolha == 2:
        print(
            'Por desobecer as ordens reais, o jovem heroi foi sentenciado '
            'a masmorra, tendo que viver seus ultimos dias em uma cela fria e escura')
        return False
    elif escolha == 1:
        print("A missão do aventureiro era capturar e matar um terrivel monstro que assolava "
              "os trabalhadores de uma mina de ouro em uma provincia ao leste da vila,"
              "Logo ao voltar para casa " + name +
              " deve decidir se contará a sua amada de sua missão,"
              "sabendo de seus problemas de coração o aventureiro estava em receio "
              "de contar a sua amada com medo de sua reação.")


def intro2(name):
    print('na mochila dada a você pelo lord, existem provisões para uma viagem inteira, '
          'alem de moedas de prata e uma espada para você se defender')
    print('"Eu ouço relatos de bandidos no caminho saindo da vila” diz lord blackbird')
    print('ao sair da vila ' + name + ' se depara com a grande floresta de highwater.')
    print('Alem de densa, nela vivia uma bruxa chamada Frewin. O aventureiro possui 4 caminhos')
    print('1- Contornar a floresta')
    print('2- Ir pelo caminho a sua esquerda')
    print('3- Ir pelo caminho a sua direta')
    print('4- Retornar a vila')


def etapa2(escolha):
    if escolha == 1:
        print("- 30 de vida devido ao cansaço de contornar a floresta inteira")
        return 1
    elif escolha == 2:
        return 2
    elif escolha == 3:
        print("Batalha Bruxa")
        return 3
    elif escolha == 4:
        print(
            'Por desobecer as ordens reais, o jovem heroi foi sentenciado '
            'a masmorra, tendo que viver seus ultimos dias em uma cela fria e escura')


def intro3():
    print('Após enfrentar os obstaculos da floresta, o aventureiro se depara com a '
          'vila de Blackfeather ao adentrar a vila, os camponeses o olham de uma maneira estranha.')
    print('1 - tentar encontrar um lugar para comer')
    print('2 - tentar encontrar um lugar para descansar')
    print('3 - seguir a viagem')
    print('4 - gritar aos camponeses “o que voces estão olhando?”')


def etapa3(escolha):
    if escolha == 1:
        return 100
    elif escolha == 2:
        return 100
    elif escolha == 3:
        return None
    elif escolha == 4:
        print('Uma horda de camponeses cerca o aventureiro por confundi-lo com um famoso lider '
              'de um grupo de saqueadores')
        print('O aventureiro sem poder escolher o que fazer corre da vila')
        roll = random.randint(0, 1)
        if roll == 1:
            print("Um Camponês o atinge com uma pedra nas costas")
            print("- 10 de vida")
            return -10
        else:
            print("Você consegue fugir sem problemas")


def intro4():
    print('Após andar mais alguns quilômetros o jovem guerreiro '
          'encontra um acampamento escondido em meio a floresta')
    print('1- Ignorar e seguir seu caminho')
    print('2- Ir investigar o campamento')


def etapa4(escolha):
    if escolha == 1:
        return True
    else:
        print('Você descobre que o acampamento pertence aos saqueadores da vila anterior')
        return


def intro4_1():
    print('1- Voltar a vila e reportar a população')
    print('2- Ignorar e seguir seu caminho, pois os habitantes da vila tentaram mata-lo')
    print('3 - Fingir ser o lider dos saqueadores ir ao o acampamento')
    print('4 - Ir conversar com os saqueadores, pedindo ajuda para derrotar o monstro da vila')


def etapa4_1(escolha):
    if escolha == 1:
        print('O guerreiro leva os habitantes ate o acampamento dos saqueadores e '
              'pelo ato nobre recebe uma benção de um bruxo que o deixa mais forte.')
        return 1
    elif escolha == 2:
        print("Um saqueador o avista na estrada")
        return 2
    elif escolha == 3:
        print("Você Conquista a confiança dos saqueadores e os saqueadores acreditam que você"
              "é o lider perdido deles,"
              "então conta sobre a mina para ter ajuda a derrotar o monstro")
        return 3
    elif escolha == 4:
        print("Os saqueadores se juntam com o guerreiro para ir a mina derrotar o monstro.")
        return 4
        #return [0, 60, 85, 100]


def intro5():
    monstros = ["Dragão", "Troll Gigante", "Lobisomem", "Centauro"]

    print('Chegando a mina o guerreiro ve muitos corpos de mineiros,'
          ' ao adentrar a caverna da mina o jovem se depara com um ' + random.choice(monstros))
    return False
