label dia_1_palma:
    play music "music/Musica-3.ogg"
    "Você fala a palavra capitalismo em voz alta e isso fica por isso"

    "Você decide que seja lá o que cada um dos dois queira que você faça hoje, pelo menos a Palma vai te pagar"

    "O cheiro que enche as suas narinas quando você desce as escadas é quase tão intoxicante quanto o de um corpo decaindo"

    "Sua boca começa a salivar quase tanto quanto a de um cão raivoso"

    "O desejo que invade o seu corpo é quase tão poderoso quanto o seu desejo secreto de reencarnar como uma minhoca"

    "Ah...!"

    "...Torta"

    show palma normal at center

    dragao "Olha, eu vou tomar isso como um elogio"

    "Oh, claro, foi isso que você quis dizer"

    dragao "Ótimo"

    dragao "Eu fiz café"

    dragao "Eu costumo cozinhar mais pra mim mesma, então eu espero que esteja bom?"

    "Ela te encara cheia de expectativa, esperando que você experimente um pedaço da torta"

    "Você aponta pro forno? Que é de onde tá vindo o cheiro?"

    dragao "Oh, claro"

    dragao "Não dá pra experimentar a torta se ela não estiver aqui"

    dragao "Na mesa"
    if genero == 2:
        "Ela ainda demora uns 5 segundos pra se levantar e ir pegar a torta depois desse último comentário. 
        Em pouco tempo, você tá sentade na mesa e tem uma fatia generosa de torta com um recheio vermelho brilhante na sua frente"
    elif genero == 1:
        "Ela ainda demora uns 5 segundos pra se levantar e ir pegar a torta depois desse último comentário. 
        Em pouco tempo, você tá sentada na mesa e tem uma fatia generosa de torta com um recheio vermelho brilhante na sua frente"
    else: 
        "Ela ainda demora uns 5 segundos pra se levantar e ir pegar a torta depois desse último comentário. 
        Em pouco tempo, você tá sentado na mesa e tem uma fatia generosa de torta com um recheio vermelho brilhante na sua frente"

    "Palma senta na cadeira dela e recarrega o olhar expectativo que ela tinha pouco tempo atrás"

    "Claro, você experimenta um pedaço da torta e se prepara pra dar sua opinião"
menu:
    "Tá ótima!":
        dragao "Ainda bem!"
    "Tá ok":
        dragao "Huh, é melhor que nada"
    "Você decide que essa escolha requer um nível de abstração que você não se dispõe a alcançar":
        dragao "Eu agradeço a sinceridade"

label cozinha_0:

    dragao "Que bom que você tá comendo"

    dragao "Então"

    dragao "Eu preciso de ajuda com um tio meu hoje"

    dragao "Ele morreu"

    dragao "...O que eu acho que é um pré requisito pra você poder me ajudar então isso é bom"

    dragao "Não que seja bom ele estar morto, essa parte especificamente não é boa"

    dragao "Mas é bom que ele possa ser revivido por você"

    "Você se surpreende com o quanto ela consegue complicar o fraseamento de uma ideia tão simples"

    "Você come outra garfada da torta"

    dragao "...Ótimo!"

    dragao "Tem uma coisinha que eu queria ler pra você antes"

    "Você come outra garfada da torta, parece que a Palma puxou um pedacinho de papel de algum lugar"

    dragao "Ok, uh, atenção"

    show poema lenhador at truecenter
    pause
    hide poema lenhador 
    with dissolve

    "Você pergunta se ela espera que você avalie o poema dela"

    "Olha, você pode gostar de falar mas isso não significa que você tem qualificação pra -"

    dragao "Não! Ah, não fui eu que escrevi"

    "Não?"

    dragao "É, uh, não, foi outra pessoa"

    dragao "Eu digo"

    dragao "É tematicamente relevante"

    "Quando você leva outra garfada de torta até a boca você só sente o sabor metálico do talher"

    "Você olha pro prato, parece que a torta acabou"
    if genero == 2: 
        dragao "Pronte pra ir? Pode deixar que eu cuido do prato depois"
    elif genero == 1:
        dragao "Pronta pra ir? Pode deixar que eu cuido do prato depois"
    else:
        dragao "Pronto pra ir? Pode deixar que eu cuido do prato depois"

    "Oh, claro"

    "Você se levanta e Palma corre logo em direção à porta"
    
    scene bg entrada with fade

    show palma normal at center with dissolve

    "Você segue ela até à entrada da casa"

    "Ela te guia da clareira do quintal até uma árvore específica só longe o bastante da casa pra começar a te deixar desconfortável"

    dragao "Certo, uh"

    dragao "Você pegou aquele poema, né?"

    dragao "Tipo, você Pegou, pegou aquele poema, né?"

menu:
    "Claro?":
        dragao "Oh, ainda bem"
    "Eu achei que você tinha guardado":
        dragao "Não é disso que eu tô falando!"
        dragao "Eu tô perguntando se você entendeu"

label arvore_0:

    "Era alguma coisa sobre árvores? Você acha"

    dragao "É, ugh"

    dragao "Eu digo"

    dragao "Eu só tô dizendo que"

    dragao "É Importante"

    dragao "Sabe?"

    "Você não se atreve a dizer que sabe exatamente do que ela tá falando, 
    mas pela expressão que ela tá fazendo parece que você provavelmente devia"

    "Só falta ela dar uma piscadela pra mostrar que tem alguma coisa ali que você devia ter sacado"

    "Ela absolutamente precisa trabalhar na didática dela"

    dragao "Tá, ok, esquece, olha"

    dragao "Eu digo, olha"

    dragao "Literalmente"

    dragao "Uh, pra frente"

    "Oh, claro"

    "Você olha pra frente e, huh"

    "Tem um cadáver jogado ali"

    "Apoiado no pinheiro, um machado do lado, o cara tá vestido e tudo"

    dragao "Tá aí ele!"

    "Você esperava um túmulo?"

    dragao "Não!"

    dragao "Ele era bem ligado à natureza, sabe"

    dragao "Então a gente queria deixar ele em um lugar próximo à natureza"

    "Então eles deixaram ele jogado no meio da floresta do lado de uma árvore"

    "Aproveitaram e botaram um machado do lado pra ter certeza de que qualquer aventureiro que 
    passasse pudesse perceber que ele era sim um lenhador e pudesse elogiar as habilidades 
    de contação de histórias por meio de design de ambiente da família"

    "Talvez tenham pensado até em enquadrar uma cartinha do lado explicando como ele morreu, 
    pra ter certeza absoluta de que ninguém conseguiria olhar praquele negócio e interpretar algum detalhe da história de maneira errô -"

    "Oh, pera, tem mesmo uma cartinha enquadrada do lado"

    "Você chega mais perto pra ler"

    show poema lenhador at truecenter
    pause
    hide poema lenhador with fade

    "Oh"

    dragao "He he"

    dragao "É aquele mesmo poema"

    "Então foi assim que ele morreu? Como era, \"vou cair em você?\""

    dragao "O eu-lírico é uma árvore"

    dragao "Mas, uh, talvez você deva perguntar pra ele"

    "Oh, claro"

    "Você se ajoelha ao lado do cadáver"

    "Você sente que ele morreu já faz um bom tempo, você sente quase como se o corpo dele tivesse começado a criar raízes no chão"

    "Você se assusta com a quantidade de massa peitoral que ele ainda tem? 

    Uh, você para de tatear o peito dele antes que a Palma comece a achar estranho"

    "O cadáver começa a pulsar contra os seus dedos" with vpunch

    "Ele não consegue exatamente abrir os olhos, visto que ele não tem exatamente pálpebras, mas ele faz alguma coisa parecida"

    show palma normal at left with move

    "Bom dia grandão"

    show castor cp with pixellate

    castor "Huh?"

    dragao "Oh, nossa"

    castor "Ehh?"

    castor "Quem?"

    "Você acha que a melhor resposta pra essa pergunta é que é você mesmo, 
    mas você não acha que é isso que o castorzão tá querendo ouvir então você só se cala"
    dragao "Eu?"

    castor "..."

    castor "... Palma?"

    dragao "Oh, ufa!"

    dragao "Oi! Tio!"

    castor "Oi"

    "Ele te encara por um segundo e você não tem nenhuma ideia do que é suposto você fazer"

    dragao "Oh, uh, necromante!"

    dragao "Digo, afirmação"

    dragao "Tio, necromante"

    castor "Lenhador"

    dragao "Não, digo"

    dragao "Guhh"

    dragao "Tio! Você tá morto!"

    "O castor solta a fachada estóica por um segundo pra encarar a própria mão. 
    Ele balança um ossinho que protubera pra fora do buraco de onde o dedo dele devia continuar"
    castor "... Machucadinho"

    dragao "Não!"

    castor "Eu sou forte"

    dragao "Não!"

    dragao "Eu digo, sim, mas, não!"
    "Você fica encarando a Palma tentar argumentar com o tio dela sobre? 
    Seja lá o que ela tá tentando argumentar sobre por mais uns 5 minutos e 
    você tem certeza de que isso não vai progredir pra lugar nenhum nessa situação"

    "Você tenta chamar a atenção do senhor… uh, como era?"

    castor "Pierre"

    "Claro, do senhor Pierre"

    "Você aponta pro chão onde tá a plaquinha com o poema"

    castor "...?"

    "Ele vira pra Palma de leve"
    if genero == 2:
        castor "Lagarte tá tentando mandar em mim?"
    elif genero == 1:
        castor "Lagarta tá tentando mandar em mim?"
    else:
        castor "Lagarto tá tentando mandar em mim?"

    dragao "Uh, tio, eu acho que você devia escutar"

    "Pierre parece extremamente insatisfeito com ter que escutar, m
    as ele acaba se abaixando pra dar uma olha no que é que tá no chão eventualmente"

    "Ele lê o poema inteiro"

    castor "..."

    castor "... Mamãe?"

    "Não, você tem quase certeza de que é um poema"

    castor "Eu esqueci"

    castor "Que dia é hoje mesmo?"

    castor "Eu ainda preciso terminar de carvar"

    dragao "Cavar o que?"

    castor "O crânio"

    "???"

    "Ok, ele começou a correr na direção da casa"

    "A Palma olha na sua direção como se esperasse que você fizesse alguma coisa"

    "Ok, você vai salvar esse momento familiar seja isso a última coisa que você faça"

    "Você mata as pernas dele"

    #[Sprite do Pierre fica mais baixo]
    "O castorzão cai no chão"

    "Ele passa um segundinho encarando a terra enquanto presumivelmente reavalia toda decisão que já tomou em morte"

    castor "Morto"

    "É sim grandão, dá pra se acalmar agora?"

    "Você encara a Palma"

    "Ela encara você de volta e não faz nada"

    "Você encara a Palma com mais tenacidade"

    dragao "Oh! Claro"

    dragao "Olha, tio"

    dragao "A gente precisa conversar"

    dragao "Eu sei que você não é exatamente muito dessas coisas de família e tudo"

    dragao "Mas eu te trouxe aqui por um motivo"

    castor "..."

    castor "... Certo"

    "Oh, progresso"

    dragao "Você tava falando de carvar um crânio"

    dragao "Você pode elaborar?"

    castor "... Certo"

    #[Tela branca]
    scene bg branco with fade
    castor "Era um presente pra mamãe"

    dragao "Era um presente?"

    dragao "Vovó tava morta, não tava?"

    castor "Era uma homenagem"

    castor "Quando ela morreu a gente leu alguns poemas dela em família"

    castor "Ela era uma artista"

    castor "Ela ia querer ser homenageada com arte"

    castor "Então a Aurora me ajudou"

    castor "A esposa do meu irmão?" 
    scene bg entrada
    show palma normal at left
    show castor cp 
    #[Tela volta ao normal]
    dragao "Eu conheço a minha tia"

    castor "Claro"

    #[Tela branca]
    scene bg branco
    castor "Ela era a única outra artista de verdade na casa"

    castor "Então a gente pensou numa homenagem"

    #[Silhueta dos crânios]
    castor "Eu parti o crânio da mamãe em dois"

    castor "Cada um ficou com uma metade"

    #[Sprite dos crânios]

    show cranio1_aurora at right 
    show cranio2_pierre at left
    castor "E nós dois decoramos"

    castor "Era uma surpresa pra família, a gente queria que fosse exposto na sala"

    castor "Mas eu não tive tempo de dar os toques finais"

    #[Tela normal]
    scene bg entrada
    show palma normal at left
    show castor cp 

    dragao "Oh? Não tava pronta?"

    dragao "A gente expôs mesmo assim"

    castor "Com licença"

    castor "O crânio foi exposto?"

    castor "Não estava pronto"

    dragao "Ficou na sala por um tempo"

    dragao "Você ia procurar por ele onde?"

    castor "Na minha oficina"

    dragao "Claro"

    dragao "Ok, mas"

    dragao "Digamos que supostamente"

    dragao "Por algum motivo não especificado"

    dragao "Ele não estivesse na sua oficina"

    dragao "Você tem alguma ideia de onde mais ele poderia estar?"

    castor "Na minha oficina"

    dragao "Ok mas se ele não estivesse lá?"

    castor "Na minha oficina"

    dragao "Ok mas e se por acaso você procurasse e ele não estivesse lá"

    castor "Na minha oficina"

    dragao "Ok mas tomemos como pressuposto que por algum motivo não relevante pro contexto atual ele não estivesse lá, onde você procuraria?"
    castor "Na minha oficina"

    dragao "Certo, mas e se você fosse até a oficina, passasse um tempo considerável revirando o lugar inteiro em busca do crânio, 
    e chegasse por si próprio na conclusão de que -"

    "Você não faz a mínima ideia do que tá acontecendo"

    "Aparentemente a Palma tava procurando por esse crânio? Mas parece que o castor não tem como ajudar ela"

    "Você chama o nome da Palma"

    "O que exatamente vocês tão fazendo aqui?"

    dragao "Oh, uh"

    dragao "Desculpa, eu acho que o que eu tava tentando fazer não deu certo"

    "Jura?"

    dragao "É, eu juro"

    dragao "Será que tem como…"

    "Ela faz um sinal que parece muito com uma criança enjoada jogando um brinquedo no chão"

    "Você continua não sendo fluente em libras mas você tem quase certeza de que isso significa que ela quer que 
    você dê um slam dunk no tio dela de volta pra terra"

    "Então você chega mais perto do tio pra ver o que ele tem em mente"
    hide palma

    "Ele realmente fica bem engraçadinho tão baixinho assim"

    castor "Hunf"

    "Você pergunta qual o que ele pretende fazer agora"

    castor "Morto?"

    castor "Dar uma volta?"

    "Não parece uma ideia ruim"

    "Você pergunta pra ele como foi que ele morreu"

    castor "É uma história engraçada"

    castor "Eu saí de casa pra cortar madeira"

    castor "Eu sou um lenhador"

    "Você percebeu"

    castor "Foi quando começou uma tempestade"

    castor "O Conselho de Castores Madeireiros (CCM) não recomenda que ninguém vá cortar madeira durante uma tempestade"

    castor "Mas esse é um país livre"

    castor "E eu sou forte"

    castor "Então eu fui mesmo assim"

    scene vinhetapierre with dissolve
    #[Vinheta da morte aparece]

    castor "A parte ruim de cortar madeira quando tem uma tempestade por aí é essa"

    castor "Você não é o único lenhador por aí"

    castor "A Mãe Natureza também estava procurando troncos naquela noite"

    castor "E aparentemente Ela tava interessada numa árvore bem próxima de onde eu tava"

    castor "A última coisa que eu lembro de ver foi o tronco caindo em cima de mim"

    castor "E eu morri"
    scene bg entrada with fade
    show castor cp at center
    #[Vinheta da morte desaparece]
    "Você se pergunta porque exatamente ele acreditava que a morte tinha sido engraçada"

    "Você pergunta se ele quer as pernas dele de volta"

    castor "Sim"

    "Você pega elas de onde elas tinham caído no chão. Alinhar elas com o resto dos ossos é um pouquinho constrangedor com ele acordado, 
    mas em pouco tempo elas tão conectadas de novo"
    #[Sprite do Pierre volta ao normal]
    "Você pergunta se ele pretende dar aquela volta agora"

    castor "..."

    castor "... Sim"

    castor "Eu acho que eu vou, sim"

    "Ele acena pra Palma antes de se virar e entrar nas profundezas da floresta"
    
    hide castor with dissolve

    "Você vira pra Palma e pergunta? O que foi isso?"
    
    show palma normal at center

    dragao "Oh, uh"

    dragao "Bem"

    dragao "Eu acho que eu não sou muito boa nesse negócio de falar com os mortos"

    "Essa afirmação não te surpreende"

    "Você diz pra Palma que você realmente gostaria de ir dormir agora"

    dragao "Oh, claro"

    dragao "Eu imagino que reviver alguém seja um processo bem cansativo"

    "Oh, isso ela pode ter certeza que é"
    scene bg hall
    #[BG hall principal]
    "Você vai pro seu quarto e ela oferece te deixar mais um pedaço de torta pra você não ir dormir com fome"

    "Você cai no sono antes da torta chegar"
    scene bg black

    jump intro_dia2

label intro_dia2:
    return