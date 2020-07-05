import random


def intro(name):
    print(
        "Há séculos, em uma pequena vila chamada Northbury, o Lord Blackbird, a mando do rei chamou o aventureiro"
        f"\n{name} para uma missão perigosa. O Lord deu duas opções ao aventureiro")
    print("O Lord deu duas opções ao aventureiro")
    print("1 – Aceitar a missão que lhe foi dada")
    print("2 – Sofrer as consequencias de não seguir as ordens do rei")


def etapa1(escolha, name):
    if escolha == 2:
        print(
            "Por desobedecer as ordens reais, o jovem herói foi sentenciado a masmorra, tendo que viver seus últimos"
            "\ndias em uma cela fria e escura")
        return 2
    elif escolha == 1:
        print(
            "A missão do aventureiro era capturar e matar um terrível monstro que assolava os trabalhadores de uma"
            f"\nmina de ouro em uma província ao leste da vila.")


def intro2(name):
    print(
        'Na mochila dada a você pelo lord, existem provisões para uma viagem inteira, alem de moedas de prata e uma'
        '\nespada para você se defender. Eu ouço relatos de bandidos no caminho saindo da vila diz lord blackbird'
        f'\nao sair da vila {name} se depara com a grande floresta de highwater. Alem de densa, nela vivia uma bruxa'
        '\nchamada Frewin. O aventureiro possui 4 caminhos.')
    print('1- Contornar a floresta')
    print('2- Ir pelo caminho a sua esquerda')
    print('3- Ir pelo caminho a sua direta')
    print('4- Retornar a vila')


def etapa2(escolha, name):
    if escolha == 1:
        print("- 30 de vida devido ao cansaço de contornar a floresta inteira")
        return 1
    elif escolha == 2:
        print("Você se depara com um saqueador dentro da floresta. ")
        return 2
    elif escolha == 3:
        print(
            f"Após alguns metros adentrando a mata, {name} encontra Frewin e começa então uma batalha.")
        return 3
    elif escolha == 4:
        print(
            'Por desobecer as ordens reais, o jovem heroi foi sentenciado a masmorra, tendo que viver seus ultimos'
            '\ndias em uma cela fria e escura')


def intro3():
    print(
        'Após enfrentar os obstáculos da floresta, o aventureiro se depara com a vila de Blackfeather ao adentrar'
        '\na vila, os camponeses o olham de uma maneira estranha.')
    print('1 - Tentar encontrar um lugar para comer')
    print('2 - Tentar encontrar um lugar para descansar')
    print('3 - Seguir a viagem')
    print('4 - Gritar aos camponeses “o que voces estão olhando?”')


def etapa3(escolha):
    if escolha == 1:
        return 100
    elif escolha == 2:
        return 100
    elif escolha == 3:
        return None
    elif escolha == 4:
        print(
            'Uma horda de camponeses cerca o aventureiro por confundi-lo com um famoso líder de um grupo de '
            '\nsaqueadores')
        print('O aventureiro sem poder escolher o que fazer corre da vila')



def intro4():
    print(
        'Após andar mais alguns quilômetros o jovem guerreiro encontra um acampamento escondido em meio a floresta')
    print('1- Ignorar e seguir seu caminho')
    print('2- Ir investigar o campamento')


def etapa4(escolha):
    if escolha == 1:
        return True
    else:
        print(
            'Você descobre que o acampamento pertence aos saqueadores que roubaram a vila anterior')
        return False


def intro4_1():
    print('1- Voltar a vila e reportar a população')
    print('2- Ignorar e seguir seu caminho, pois os habitantes da vila tentaram matá-lo')
    print('3- Fingir ser o líder dos saqueadores e ir ao o acampamento')
    print(
        '4- Ir conversar com os saqueadores, pedindo ajuda para derrotar o monstro da vila em troca de algum ouro'
        '\napós a batalha')


def etapa4_1(escolha):
    if escolha == 1:
        print(
            'O guerreiro leva os habitantes ate o acampamento dos saqueadores e pelo ato nobre recebe uma benção de'
            '\num bruxo que o deixa mais forte.')
        return 1
    elif escolha == 2:
        print("Um saqueador o avista na estrada e o ataca. Então uma batalha se inicia.")
        return 2
    elif escolha == 3:
        print(
            "Você Conquista a confiança dos saqueadores e os eles acreditam que você é o lider perdido deles, então"
            "\nconta sobre a mina para ter ajuda a derrotar o monstro")
        return 3
        # return [0, 60, 85, 100]
    elif escolha == 4:
        print("Os saqueadores se juntam com o guerreiro para ir a mina derrotar o monstro.")
        return 4
        # return [0, 60, 85, 100]


def intro5():
    monstros = ["Dragão", "Troll Gigante", "Lobisomem", "Centauro"]

    print(
        'Chegando a mina o guerreiro ve muitos corpos de mineiros,ao adentrar a caverna da mina o jovem se'
        '\ndepara com um ' + random.choice(monstros))
    return False


def etapa5(escolha, name):
    if escolha == 1:
        print(
            f'Após uma arda batalha com o monstro, chega então a hora de voltar para casa. Sabendo de sua longa'
            '\nviagem, ao passar pela vila, o povo da aldeia em que havia ajudado decide então o recepcionar por'
            f'\nalguns dias para que {name} possa se recuperar. Após sua partida, o oferecem para levar comida em'
            '\nsua viagem. O guerreiro agradecido aceita a oferta dos camponeses. Chegando no reino, o rei então'
            '\nrealiza uma comemoração no reino para agradecer o guerreiro. Rei - Por sua nobre bravura, receba '
            '\nestá recompensa em ouro e a partir de hoje você será meu conselheiro.')
        return 1
    elif escolha == 2:
        print(
            'Após uma arda batalha com o monstro, chega então a hora de voltar para casa. Por ser uma viagem longa'
            '\ne o guerreiro estar machucado, acaba sendo uma vigem muito difícil. Quando estava algum quilometros'
            f'\ndo reino, {name} não aguenta mais e acaba desmaiando na estrada, porem alguns soldados do reino o '
            '\nencontram e o levam devolta ao reino, aonde por mandos do rei é cuidado pelos melhores medicos de sua'
            f'\nalteza. Após a recuperação de {name}, o rei então realiza uma comemoração no reino para agradecer'
            '\no guerreiro.'
            '\nRei: Por sua nobre bravura, receba está recompensa em ouro e a partir de hoje'
            'znvocê sera meu conselheiro.')
        return 2
    elif escolha == 3:
        print(
            f'Após uma arda batalha com o monstro, chega a então a hora de voltar para casa. {name} então fala aos'
            '\nsaqueadores que irá visitar sua familia para despistá-los, porém ao passar pela vila, repara que há'
            '\num cartaz de procurado em seu nome, não podendo mais voltar ao reino. Ele então se junta ao '
            '\nsaqueadores e se mantem foragido. Após a noticia chegar aos ouvidos do rei, ele ordena que prendam'
            '\nsua esposa e seu filhos.')
        return 3
    elif escolha == 4:
        print(
            f'Após uma arda batalha com o monstro, um dos saqueadores o golpei e {name} acaba desmaiando. Assim que'
            '\nacorda repara que todo o ouro foi levado e que está muito machucado. O guerreiro então sem muitas'
            f'\nopções vai em direção a vila em que havia passado antes. Chegando lá {name} novamente é confundido '
            'com o lider dos saqueadores e acaba preso. Após contar a a missão que veio realizar, o lider da vila'
            '\nentra em contato com o rei pedindo para que alguém venha averiguar a história. Depois de um soldado'
            f'\nconfirmar a história do guerreiro, ele foi solto e levado de volta ao reino. chegando lá, {name} '
            '\nmente contando que após derrotar o monstro, que saqueadores chegaram e roubaram o ouro.')
