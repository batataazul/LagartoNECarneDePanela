﻿# The script of the game goes in this file.

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

    cervo "…"

    show abelarde cranio

    cervo "ok, eu mudei de ideia"

    cervo "me segura"

    "Você atende ao pedido do seu novo amigo esqueletal"
    
    show abelarde cranio at truecenter
    with move

    "Você volta a sua posição usual: osso erguidos somente pelas pontas dos seus dedos, 
    tendo certeza de deixar as órbitas oculares do recém revivido sempre um pouquinho acima dos seus próprios olhos"

    "A reação do cervo não lhe é estranha, a experiência de voltar a vida pode ser algo extremamente chocante para a maioria das pessoas. 
    Você consegue ver ele se mexendo de leve na sua mão enquanto debate se ele devia pedir pra ser jogado na lama de novo ou não"

    "Você explica a condição na qual ele se encontra atualmente"

    "Você diz que ele não tem o que temer, que as entranhas da terra sempre serão parte dele na pós vida, 
    bem como ele se permitiu se tornar parte delas. Mesmo o frio da morte pode se aconchegar no calor Do Enterrado"

    "Bem como a pele é uma mera extensão do osso, o osso se torna uma mera extensão da terra ao ceder sua essência à insaciável fome do chão." 
    
    "Você diz para Abelarde que ele tanto pode, como deve, encontrar conforto no fato de que bem como ele faz parte de todo verme naquela 
    floresta, todo verme naquela floresta fazia parte dele."

    "Falando nisso, ah, opa"

    "Opa, opa, ok"

    "Você peteleca pro chão uma minhoquinha que tava tentando entrar dentro do olho do Abelarde, 
    ele não parece particularmente satisfeito, mas você não faz a mínima ideia do porque"

    "De qualquer modo, onde você tava? Claro, terra, vermes"

    "Você diz ao Abelarde que do pó ao pó é a -"

    cervo "Ok, me joga na lama de novo"

    "Oh, parece que ele tomou uma decisão"

    "Você explica pra ele que você não pode exatamente jogar ele no chão, visto que não foi exatamente pra isso que você foi chamado"

    cervo "Ah, é? Então pra que foi que você foi chamado"

    "Você explica que foi pra trazer Abelarde de volta pra irmã dele"

    cervo "Oh, oh, não, não"

    cervo "Nem a pau!"

    cervo "Ela te contratou pra me reviver?"

    cervo "Pois você pode avisar que eu tô muito bem morto e obrigado"

    cervo "Em primeiro lugar que eu não faço nem ideia do porque ela iria me querer vivo de novo"

    cervo "Em segundo que a conversa toda sobre as minhocas não me deixou exatamente num clima de querer conversar com ninguém agora"

    cervo "Então faz favor de me enfiar naquele buraco de novo"

    cervo "Ok?!"

    "Uh, enfiar pessoas em buracos é meio que o oposto da sua especialidade, caso ele não tenha percebido"

    cervo "Eu não sei se você notou mas eu não tô exatamente em condições de me jogar lá eu mesmo"

    "O problema é que mesmo se você jogasse ele ali dentro de novo ele não ia deixar de ficar vivo"

    cervo "Eu não me importo!"

    "O Abelarde não quer ver a irmã dele?"

    cervo "Oh!"

    cervo "Oh! Oh!"

    cervo "Oh!"

    cervo "Você absolutamente não faz a mínima ideia do que você tá falando!"

    cervo "Eu não tenho nem um mísero pinguinho de interesse em voltar a viver com aquela! Obcecada!"

    if genero == 2:
        "Ok, ok, é óbvio que eles tem alguma espécie de drama familiar que talvez você não esteja inteiramente qualificade pra lidar com, 
        mas isso não significa que vocês três não podem tentar chegar em algum acordo"
    elif genero == 1: 
        "Ok, ok, é óbvio que eles tem alguma espécie de drama familiar que talvez você não esteja inteiramente qualificada pra lidar com, 
        mas isso não significa que vocês três não podem tentar chegar em algum acordo"
    else:
        "Ok, ok, é óbvio que eles tem alguma espécie de drama familiar que talvez você não esteja inteiramente qualificado pra lidar com, 
        mas isso não significa que vocês três não podem tentar chegar em algum acordo"

    cervo "Olha aqui colega! Não existe esse negócio de “nós três”, ok?!"

    cervo "Eu! Sou um esqueleto!"

    if genero == 2:
        cervo "E eu acho que você não tá interessade em saber o porquê!"
    elif genero == 1:
        cervo "E eu acho que você não tá interessada em saber o porquê!"
    else:
        cervo "E eu acho que você não tá interessado em saber o porquê!"

    cervo "Se a Palma tá querendo me trazer de volta é só sinal de que ela nunca teve um plano de verdade sobre morar nessa casona sozinha!"

    cervo "E isso oficialmente não é mais problema meu!"
    
    "Ok, talvez o cervo raivoso não tenha percebido que esse meio que é o seu emprego"

    "Então seria bom se ele pudesse colaborar"

    "Se qualquer coisa, pelo menos pra que a sua viagem de mais de uma hora pra chegar aqui, 
    e, presumivelmente, mais de uma hora pra conseguir sair não fosse em vão"

    cervo "Ora, eu!"

    cervo "Eu!"

    cervo "…"

    cervo "… eu quero o resto do meu corpo antes de fazer qualquer decisão"

    "Ok, isso é uma coisa que você pode fazer"

    "Você deixa o Abelarde numa pilhinha confortável de lama de chão antes de pegar a pá e começar de novo a cavucar ao redor da lápide dele"

    "Mesmo tendo que lidar com o crânio constantemente gritando pra você acelerar o processo, 
    você consegue desenterrar o resto do esqueleto sem muitos problemas"

    "Você aproveita pra pegar um manto do varal próximo. Mesmo que não tenha mais nada pra esconder, 
    a maior parte dos recém revividos se sentem extremamente expostas quando os seus ossos ficam à mercê do vento"

    cervo "Vendo de longe, eu sempre achei que eu fosse um pouquinho mais alto do que isso"

    cervo "Devem ser os chifres"

    cervo "Dá pra me juntar agora?"

    "Oh, claro, juntar é a sua especialidade"

    "Você alinha as peças diferentes o melhor possível no chão antes de tocar novamente o crânio de Abelarde"

    "Vagarosamente, todas as peças do corpo dele começam a pulsar em uma única voz. 
    Você sente elas tremerem devagar enquanto Abelarde vai ganhando controle do seu novo velho corpo de novo."

    "A primeira ação consciente dele com as novas mãos é rapidamente tomar o manto das suas mãos para se cobrir"

    show abelarde with pixellate

    cervo "Uau"

    cervo "Isso não é assim tão ruim, na realidade"

    cervo "Obrigado"

    "É um prazer ajudar a deixar a morte dele o mais confortável possível"

    "Mas esse não era exatamente o foco principal desse exercício todo, você lembra. Agora ele precisa ir com você falar com a Palma"

    cervo "Huh"

    cervo "Claro, falar com a Palma"

    cervo "Oh!"

    cervo "O que é aquilo!"

    "Você vira pra onde o Abelarde tava apontando"

    "Pé Grande!!!"

    "Ok, não tem um Pé Grande, 
    mas você tem que admitir que você não conseguia parar de pensar na possibilidade de encontrar um durante a sua viagem até aqui"

    "Era um medo inteiramente irracional, é claro."
    
    "Todo mundo sabe que Pés Grandes costumam viver em áreas muito mais frias do que essa"
    
    "e que eles são inteiramente civilizados"

    if genero == 0:
        "Além disso você meio que precisa admitir que ter medo de um Pé Grande é sim um reflexo da sua visão privilegiada de mundo, 
        tendo nascido um lagarto, espécie considerada por literalmente quase todo mundo como \"bem ok\""
    elif genero == 1:
        "Além disso você meio que precisa admitir que ter medo de um Pé Grande é sim um reflexo da sua visão privilegiada de mundo, 
        tendo nascido uma lagarta, espécie considerada por literalmente quase todo mundo como \"bem ok\""
    else:
        "Além disso você meio que precisa admitir que ter medo de um Pé Grande é sim um reflexo da sua visão privilegiada de mundo, 
        tendo nascido um lagarte, espécie considerada por literalmente quase todo mundo como \"bem ok\""

    "Mas não era disso que essa situação se tratava, você se vira de novo pra Abelarde pra perguntar o que diabos que ele tinha -"

    hide abelarde with fade

    "Oh"

    "Claro, ele sumiu"

    "Não é como se fosse a primeira vez que um morto simplesmente te deixa de lado. 
    Isso, é claro, não muda o fato de que isso é uma situação extremamente decepcionante"
















    
