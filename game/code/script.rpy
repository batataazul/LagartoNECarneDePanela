# The script of the game goes in this file.

#Personagens
define lagarto = Character("[name]")
define cervo = Character("Abelarde", color="#1197a9")
define dragao = Character("Palma",color="#aa423e")
define gamba = Character("Aurora", color="#7702f1")
define castor = Character("Pierre", color="#ffec05") 

#variáveis úteis
define ePalma = 0
define eAbelarde = 0
define genero = False


# The game starts here.

label start:
    #começo dia 0
    
    scene bg floresta
    "Era uma das últimas tardes mornas do começo do outono. 
    Uma brisa leve bagunçava suas roupas e os raios de sol banhavam o mundo inteiro em laranja."

    "Quer dizer, é assim que você descreveria o clima antes de entrar na floresta."

    "Infelizmente, o labirinto de troncos acabou com todo e qualquer sussurro da brisa confortável que era anteriormente tão marcante." 

    "O céu de folhas esmaeceu completamente a quentura do dia, substituindo o laranja do sol pelos azuis e verdes escuros da vegetação local."

    "A floresta tinha acabado de transformar o começo do outono no final do inverno"

    "… Além de ter acabado com toda a sua disposição poética"

    "Ughhhhhhhh"

    "De acordo com o seu contato, era só “Seguir pela floresta”. 
    O problema é que você já tinha se disposto a seguir pela floresta já fazia pelo menos uma hora."

    "Agora onde tinha disposição pra fazer um trabalho bem feito, só resta uma poça de suor."

    "Entre horas de caminhada, frequente interação com a podridão mais profunda do solo, e o salário baixo, esse trabalho é absolutamente..."

menu:
    "Exaustivo":
        "É, por aí mesmo"
    "Recompensador":
        "Hey, até positividade tem limite"

label floresta_1:
    "De qualquer modo, é nisso que dá ser necromante profissional"

    "Quando não se tá conversando com uma mulher desesperada pra ver o filho de novo, uma autoridade local que quer te prender, 
    ou com um cara que desesperadamente quer namorar um esqueleto, é isso que sobra."

    "Caminhar"

    "BAM!"

    "Falando nisso, parece que você acabou de caminhar em alguma coisa, bom trabalho."

    "Você massageia o seu nariz onde tá doendo antes de confrontar a coisa que aparentemente 
    você tava fundo demais nos seus pensamentos pra perceber"

    show palma at center 

    "Moça da floresta?" "Oh, eu sinto muito! Eu não tinha te visto"

    "Moça da floresta?" "Você por acaso é quem eu contratei?"

    "Você se dá direito de esperar meio segundo antes de responder, 
    tanto pra evitar gritar com a moça pelas informações precárias, 
    quanto pra amaciar o seu nariz um pouquinho mais."

    "Ok, ok. Você diz pra ela que sim, você provavelmente é quem ela contratou."

    "Cliente da floresta!" "Oh, que maravilha!"

    "Cliente da floresta!" "Sabe, com o tempo todo que tava demorando, eu tava começando a achar que você tinha se perdido"

    "Você escolhe não entender isso como uma reclamação pelo atraso."

    "Cliente da floresta!" "Eu tava dando umas voltas pra ver se te encontrava"

    "Moça da floresta?" "E aqui tá você!"

    "Moça da floresta?" "E aqui tá você!"

    "Cliente da floresta!" "Mas é um prazer te conhecer, senhor!"

    "Cliente da floresta!" "Digo, uh…"

    "Cliente da floresta!" "Um…"

    "Cliente da floresta!" "… Senhora?"

    "Uh"

    "Confusão da floresta" "É, uh…"

    "Confusão da floresta" "É um prazer lhe conhecer, réptil!"

    "Pera, isso foi racista?"

    "Desrespeitosa da floresta" "Pera, isso foi racista, né?"

    "Desrespeitosa da floresta:" "Ugh! Desculpa!"

    "Desrespeitosa da floresta" "Ok, eu vou ser sincera eu absolutamente não faço ideia, ok?"

    "Desrespeitosa da floresta" "Que tal assim, você facilita as coisas pra nós dois e só me diz do que você prefere que eu te chame"

menu Genero:
    "Ele":
        $genero = 0
        $name = "Lagarto"
    "Ela":
        $genero = 1
        $name = "Lagarta"
    "Elu":
        $genero = 2
        $name = "Lagarte"

label floresta_2:
    "Constrangimento da floresta" "Claro, uh, claro"

    if genero == 0:
        "Constrangimento da floresta" "É, uh, ele realmente combina com você"
    elif genero == 1:
        "Constrangimento da floresta" "É, uh, ela realmente combina com você"
    else:
        "Constrangimento da floresta" "É, uh, elu realmente combina com você"

    
