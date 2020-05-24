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

    show palma normal at center

    "Moça da floresta?" "Oh, eu sinto muito! Eu não tinha te visto"

    "Moça da floresta?" "Você por acaso é quem eu contratei?"

    "Você se dá direito de esperar meio segundo antes de responder, 
    tanto pra evitar gritar com a moça pelas informações precárias, 
    quanto pra amaciar o seu nariz um pouquinho mais."

    "Ok, ok. Você diz pra ela que sim, você provavelmente é quem ela contratou."

    "Cliente da floresta!" "Oh, que maravilha!"

    "Cliente da floresta!" "Sabe, com o tempo todo que tava demorando, eu tava começando a achar que você tinha se perdido."

    "Você escolhe não entender isso como uma reclamação pelo atraso."

    "Cliente da floresta!" "Eu tava dando umas voltas pra ver se te encontrava"

    "Moça da floresta?" "E aqui tá você!"

    "Moça da floresta?" "E aqui tá você!"

    "Cliente da floresta!" "Mas é um prazer te conhecer, senhor!"

    "Cliente da floresta!" "Digo, uh…"

    "Cliente da floresta!" "Um…"

    "Cliente da floresta!" "… Senhora?"

menu:
    "Uh":
        pass 

label floresta_2:

    "Confusão da floresta" "É, uh…"

    "Confusão da floresta" "É um prazer lhe conhecer, réptil!"

    "Pera, isso foi racista?"

    "Desrespeitosa da floresta" "Pera, isso foi racista, né?"

    "Desrespeitosa da floresta:" "Ugh! Desculpa!"

    "Desrespeitosa da floresta" "Ok, eu vou ser sincera eu absolutamente não faço ideia, ok?"

    "Desrespeitosa da floresta" "Que tal assim, você facilita as coisas pra nós dois e só me diz do que você prefere que eu te chame."

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

label floresta_3:
    "Constrangimento da floresta" "Claro, uh, claro."

    if genero == 0:
        "Constrangimento da floresta" "É, uh, \"ele\" realmente combina com você."
    elif genero == 1:
        "Constrangimento da floresta" "É, uh, \"ela\" realmente combina com você."
    else:
        "Constrangimento da floresta" "É, uh, \"elu\" realmente combina com você."

    "Você dá um agradecimento tosco pro elogio esquisito."

    "Vocês passam uns dois segundos, isso é, uns dois segundos a mais do que seria confortável, se encarando."

    "Você percebe pela curva na boca dela e pelo óbvio desconforto na postura 
    que se você deixar ela começar a falar de novo ela vai começar a tentar se desculpar de novo por deixar as coisas esquisitas."

    "Antes que isso possa acontecer, você lembra ela de que você tá aqui pra fazer algum…"

    "… Trabalho?"

    "Guia da floresta" "Oh! Claro!"

    "Guia da floresta" "Sim, o lugar certo fica a um tempinho daqui."

    "A moça te dá as costas começa a entrar mais fundo na floresta, a implicação óbvia é que você devia estar seguindo ela, 
    então é isso que você faz"

    "??? da floresta" "Minha nossa, que falta de educação! Eu esqueci de te dizer o meu nome!"

    "??? da floresta" "… É …"

    "Palma da floresta!" "Palma!"

    "Palma!"

    "Ok, só Palma" "É, só Palma."

    dragao "Foi minha avó que deu."

    dragao "Até hoje eu ainda não tenho certeza se foi falta de criatividade ou se foi criatividade em excesso."

    dragao "Ela deu o nome de muita gente."

    "Por um segundo parece que ela vai falar mais alguma coisa, mas ela para por aí mesmo."

    "Parece que vocês vão deixar os craquelados desconfortavelmente altos das folhas no chão se tornarem donos do ambiente sonoro."

    "Mas você já escutou os barulhos da floresta por tempo demais e pode confirmar, 
    com certeza absoluta, que eles perdem o charme depois de menos de 5 minutos"

    "Você pergunta se ela tem uma família grande"

    dragao "Oh, não, não. Não mais"

    dragao "Minha família já se foi faz um bocado, sou só eu por aqui"

    "Você tenta dizer que sente muito mas ela te interrompe antes que você consiga completar sequer uma sílaba"

    dragao "Ah, não, não"

    dragao "Não precisa se preocupar com isso"

    dragao "Eles se foram já faz um bocado, morar sozinha não é tão ruim assim"

    dragao "E mais, não é como se eu estivesse completamente sozinha"

    dragao "Eu ainda consigo, uh"

    dragao "Eu ainda consigo escutar as vozes deles uivando por entre as árvores, sabe?"

    dragao "E sabe, uh, eu tava pensando"

    dragao "Elas bem que podiam uivar um pouquinho mais alto, né?"

    dragao "É aí que você entra!"

    "Descrição super esquisita do que você tá aqui pra fazer, mas ok"

    "Então pelo visto ela espera que você revi- Oh, opa?"

    scene bg entrada with dissolve
    
    "Você começa a questionar a qualidade da sua vista. Você não somente não notou a presença da Palma até literalmente se tacar de nariz nela, 
    como você também só notou o literal maior casebre que você já viu na sua vida ao chegar do lado dele"

    "Ou a floresta não andou recebendo crédito o bastante pelo quão densa ela é, 
    ou você absolutamente devia falar com alguém sobre algum problema nos seus olhos"

    "Você pergunta pra Palma se esse casarão é onde ela mora"

    show palma normal at center with moveinright

    dragao "Pois é, era uma família grande"

    dragao "Então a gente precisava de uma casa bem grande"

    dragao "Mas! Eu não tô aqui pra me gabar do tamanho da minha casa!"

    dragao "Eu tô aqui pra te trazer até aqui!"

    dragao "E você, uh, não tá aqui pra me ouvir me gabar do tamanho da minha casa"

    dragao "Você tá aqui pra fazer me ajudar com um negócio!"

    dragao "E esse negócio fica do lado de fora da minha casa"

    dragao "Que, por acaso, é sim enorme"


menu:
    "Algum cemitério aqui por perto?":

        dragao "A floresta inteira é um cemitério!"

        dragao "Digo, não que eu saia enterrando gente em todo lugar, é só uma expressão"

        dragao "Um dama precisa de um sistema organizado!"
    
    "Algum cadáver enfiado numa árvore?":

        dragao "Agora que você menciona, talvez"

        dragao "Mas, uh, esse não é o foco pra você hoje!"

label casaOut_0:

    dragao "Eu tenho um cemitério de verdade, sim"

    dragao "Por favor"

    "Vocês começam a dar uma volta ao redor da casa. Não fosse a quantidade assustadora de lama ao redor, 
    você se sentiria confortável chamando o lugar de mansão"

    "Dizer que o cemitério era grande seria um eufemismo"

    scene bg cemiterio with dissolve

    "Era só um monte de túmulos espalhados por uma área livre de árvores."

    "Tinham umas cercas de madeira encostadas na parede da casa, como se alguém tivesse pensado em demarcar a área do lugar antes de desistir."

    "Considerada a área absurda de morte que tinha por lá"

    "Você é guiado até um túmulo específico, um dos mais longe que havia da casa."

    "Olhando mais de perto, não parecia ter nenhuma demarcação na sepultura"

    show palma normal at left

    dragao "Ah, tá aqui"

    dragao "O coitadinho não se mexeu esse tempo todo"

    "Você começa a se perguntar se ela sabe o que morte significa"

    dragao "É meu irmão"

    dragao "Abelarde"

    dragao "Foi uma morte trágica a dele, oh, oh, uma pena, realmente"

    "Você pergunta pra ela o que aconteceu"

    dragao " Ah, é, uh"

    dragao "É, uh, é difícil? Falar sobre isso?"

    dragao "Digo, uh"

    dragao "É difícil"

    dragao "Uh, falar sobre isso"

    dragao "É, isso aí"

    "Só tendo certeza, claro. Quanto mais informação se tem, mais fácil fica o trabalho"

    "Você pergunta se tudo bem vocês desenterrarem ele"

    dragao "Oh, claro!"

    dragao " Eu tenho umas pás justamente pra esse tipo de coisa aqui perto, um segundinho!"

    "Ela pega duas pás que estavam apoiadas em um dos outros túmulos"

    "Vocês começam a cavar juntos e em pouco tempo o branco de um osso aparece pra contrastar com o marrom escuro da terra"

    dragao "Opa, bom dia dorminhoco!"

    "Você enfia suas mãos na terra e segura o crânio que apareceu pelo buraco do olho. 
    Arrancar ele da terra é mais complicado do que normalmente é, por algum motivo."

    hide palma
    show abelarde cranio at truecenter

    "Ah, eram os chifres, enfiados fundo demais"

    "Uh, o crânio parece ser de um cervo, na realidade"

    show abelarde cranio at left
    show palma normal at right
    with move

    dragao "É meu, uh, meio irmão"

    hide abelarde

    "Isso faz mais sentido"

    "Você dá uma última olhada pra Palma antes de levantar o crânio ao céu"

    dragao "Ooooh!!! Eu nunca tinha visto isso acontecer antes"

menu:
    "E vai continuar sem ver!":
        dragao "Ah, sério!?"

        dragao "Aw!"

        dragao "Mas eu imagino que seja mais fácil pra você se eu não ficar toda curiosa do lado, né?"
    "Uh, o trabalho é mais fácil se eu puder me concentrar":
        dragao "Oh"

        dragao "Ah, claro, claro!"

label cemiterio_0:

    dragao "Então eu vou esperar dentro de casa, eu acho"

    dragao "Pode ir entrando quando der tudo certo, eu fico te esperando com alguma coisa pra comer"

    dragao "Pra nós três!"

    show palma normal at left 
    with move
    hide palma
    with None
    "Onde é que você tava mesmo?"

    show abelarde cranio at truecenter

    "Você ergue o crânio aos céus, os últimos pulsos de vida dele batucando contra os seus dedos"

    "A morte, há quem diga que a vida só faz sentido por causa da sua inevitabilidade"

    "O que isso torna você então? E as abominações que você ergue de volta da terra?"

    "Seriam elas inteiramente sem futuro? 
    Tendo completado sua jornada e depois trazidas de volta sem ter mais qualquer motivo temático para continuarem caminhando? 
    Como uma franquia de livros que não consegue parar de lançar sequências?"

    "Há quem diga até que um morto vivo nem mesmo devia ser considerado uma continuação do ser que era antes de morrer. 
    Ultrajado de tudo aquilo que o tornava vivo, um punhado de ossos não pode voltar a caminhar sem perder alguma coisa no processo"

    "Você não tem muita certeza se existe uma resposta satisfatória pra esses questionamentos, 
    mas você sabe que ossos não são inteiramente vazios"

    "Crânio" "Mm…"

    "O crânio começa a vibrar enquanto que a textura das minúsculas partículas de sangue e 
    dos traços de carbono começa a ficar cada vez mais evidente contra a sua pele"

    "Crânio" "Mmmmm!" with vpunch

    "Ser ou não ser? Dificilmente importa pra pessoas com habilidades como as suas"

    "No seu ramo, particularmente, só existe uma resposta satisfatória pra essa pergunta"

    "E essa resposta é..."

    "Crânio" "MEEEEE!"

    "Oh?"

    "Crânio" "SOLTAAAA!!!!!!!!" with vpunch

    "Você solta joga o crânio do cervo na terra, seja por respeito à vontade dele ou por causa do susto mesmo"

    hide abelarde

    "Os cenho do cervo se deforma na melhor imitação de raiva que uma pilha de ossos consegue fazer 
    quando ele cai das suas mãos direto no chão lamacento"

    "Você passa um momento encarando o chifrudo ranzinza no chão. Você sente que talvez ele possa ter se arrependido da reação precipitada"

    













    
