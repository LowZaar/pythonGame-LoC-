import random


def intro(name):
    print("há séculos, em uma pequena vila chamada Northbury, o Lord Blackbird, a mando do rei")
    print(f"chamou o aventureiro {name} para uma missão perigosa.")
    print("O Lord deu duas opções ao aventureiro")
    print("1 – aceitar a missão que lhe foi dada")
    print("2 – sofrer as consequencias de não seguir as ordens do rei")


def etapa1(escolha, name):
    if escolha == 2:
        print(
            'Por desobecer as ordens reais, o jovem heroi foi sentenciado '
            'a masmorra, tendo que viver seus ultimos dias em uma cela fria e escura')
        return 2
    elif escolha == 1:
        print("A missão do aventureiro era capturar e matar um terrivel monstro que assolava "
              "os trabalhadores de uma mina de ouro em uma provincia ao leste da vila,"
              f"Logo ao voltar para casa {name}"
              " deve decidir se contará a sua amada de sua missão,"
              "sabendo de seus problemas de coração o aventureiro estava em receio "
              "de contar a sua amada com medo de sua reação.")


def intro2(name):
    print('Na mochila dada a você pelo lord, existem provisões para uma viagem inteira, '
          'alem de moedas de prata e uma espada para você se defender')
    print('Eu ouço relatos de bandidos no caminho saindo da vila” diz lord blackbird')
    print(f'ao sair da vila {name} se depara com a grande floresta de highwater.')
    print('Alem de densa, nela vivia uma bruxa chamada Frewin. O aventureiro possui 4 caminhos')
    print('1- Contornar a floresta')
    print('2- Ir pelo caminho a sua esquerda')
    print('3- Ir pelo caminho a sua direta')
    print('4- Retornar a vila')


def etapa2(escolha, name):
    if escolha == 1:
        print("- 30 de vida devido ao cansaço de contornar a floresta inteira")
        return 1
    elif escolha == 2:
        return 2
    elif escolha == 3:
        print(f"Após alguns metros adentrando a mata, {name} encontra a "
              f"bruxa e começa então uma batalha.")
        return 3
    elif escolha == 4:
        print(
            'Por desobecer as ordens reais, o jovem heroi foi sentenciado '
            'a masmorra, tendo que viver seus ultimos dias em uma cela fria e escura')
        return False

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
        return 1
    else:
        print('Você descobre que o acampamento pertence aos saqueadores da vila anterior')
        return 2


def intro4_1():
    print('1- Voltar a vila e reportar a população')
    print('2- Ignorar e seguir seu caminho, pois os habitantes da vila tentaram mata-lo')
    print('3 - Fingir ser o lider dos saqueadores ir ao o acampamento')
    print('4 - Ir conversar com os saqueadores, pedindo ajuda para derrotar o monstro da vila'
          'em troca de algum ouro após a batalha')


def etapa4_1(escolha):
    if escolha == 1:
        print('O guerreiro leva os habitantes ate o acampamento dos saqueadores e '
              'pelo ato nobre recebe uma benção de um bruxo que o deixa mais forte.')
        return 1
    elif escolha == 2:
        print("Um saqueador o avista na estrada e o ataca. Então uma batalha se inicia.")
        return 2
    elif escolha == 3:
        print("Você Conquista a confiança dos saqueadores e os eles acreditam que você"
              "é o lider perdido deles,"
              "então conta sobre a mina para ter ajuda a derrotar o monstro")
        return 3
        # return [0, 60, 85, 100]
    elif escolha == 4:
        print("Os saqueadores se juntam com o guerreiro para ir a mina derrotar o monstro.")
        return 4
        #return [0, 60, 85, 100]


def intro5():
    monstros = ["Dragão", "Troll Gigante", "Lobisomem", "Centauro"]

    print('Chegando a mina o guerreiro ve muitos corpos de mineiros,'
          ' ao adentrar a caverna da mina o jovem se depara com um ' + random.choice(monstros))


def etapa5(escolha, name):
    if escolha == 1:
        print(f'Após uma arda batalha com o monstro, chega então a hora de voltar para casa.'
              f'Sabendo de sua longa viagem, ao passar pela vila, '
              f'o povo da aldeia em que havia ajudado'
              f'decide então o recepcionar por alguns dias para que {name} possa se recuperar.'
              f'Após sua partida, o oferecem para levar comida em sua viagem. O guerreiro agradecido'
              f'aceita a oferta dos camponeses.'
              f'Chegando no reino, o rei então realiza uma comemoração '
              f'no reino para agradecer o guerreiro.'
              f'Rei - Por sua nobre bravura, receba está recompensa em ouro e a partir de hoje você'
              f'será meu conselheiro.')
        return 1
    elif escolha == 2:
        print(f'Após uma arda batalha com o monstro, chega então a hora de voltar para casa.'
              f'Por ser uma viagem longa e o guerreiro estar machucado, acaba sendo uma vigem'
              f'muito difícil. Quando estava algum quilometros do reino, {name} não aguenta mais'
              f'e acaba desmaiando na estrada, porem alguns soldados do reino o encontram e o'
              f'levam devolta ao reino, aonde por mandos do rei é cuidado pelos melhores medicos'
              f'de sua alteza. Após a recuperação de {name}, o rei então realiza uma comemoração'
              f'no reino para agradecer o guerreiro.'
              f'\n Rei: Por sua nobre bravura, receba está recompensa em ouro e a partir de hoje'
              f'você sera meu conselheiro.')
        return 2
    elif escolha == 3:
        print(f'Após uma arda batalha com o monstro, chega a então a hora de voltar para casa.'
              f'{name} então fala aos saqueadores que irá visitar sua familia para'
              f'despistá-los, porém ao passar pela vila, repara que há um cartaz de procurado em'
              f'seu nome, não podendo mais voltar ao reino. Ele então se junta ao saqueadores e'
              f'se mantem foragido. Após a noticia chegar aos ouvidos do rei, ele ordena que'
              f'prendam sua esposa e seu filhos.')
        return 3
    elif escolha == 4:
        print(f'Após uma arda batalha com o monstro, um dos saqueadores o golpei e {name}'
              f'acaba desmaiando. Assim que acorda repara que todo o ouro foi levado'
              f'e que está muito machucado. O guerreiro então sem muitas opções vai em'
              f'direção a vila em que havia passado antes. Chegando lá {name} novamente'
              f'é confundido com o lider dos saqueadores e acaba preso. Após contar a '
              f'a missão que veio realizar, o lider da vila entra em contato com o rei'
              f'pedindo para que alguém venha averiguar a história. Depois de um soldado'
              f'confirmar a história do guerreiro, ele foi solto e levado de volta ao reino.'
              f'chegando lá, {name} mente contando que após derrotar o monstro, que saqueadores'
              f'chegaram e roubaram o ouro.')

