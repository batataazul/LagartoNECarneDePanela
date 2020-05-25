label dia_1_com_abelarde:
    scene bg hall
    play music "music/Musica-4.ogg"
    if genero == 0:
        "Você decide que você tá se sentindo caridoso"
    elif genero == 1:
        "Você decide que você tá se sentindo caridosa"
    else:
        "Você decide que você tá se sentindo caridose"

    "E, mais importante que isso, sua curiosidade sobre que tipos de serviço um cara que tá vivo faz menos de 24 horas poderia precisar é…"

    "Bem, a sua curiosidade sempre foi implacável"

    "O cheiro que invade as suas narinas quando você desce as escadas é absolutamente criminoso"

    "...Torta. Morango, você tem quase certeza"

    "...Mas você se força a resistir a tentação. Pelo que você já viu do Abelarde, você consegue dizer com certeza absoluta que ele não sabe cozinhar"

    "Isso significa que a Palma deve estar na cozinha, e se ela te ver por lá você vai ter que falar com ela e ela vai pedir pra você fazer alguma coisa e você não vai ter a força de vontade pra resistir a torta"

    "Então, por mais que seu corpo queira dizer sim, seu coração mantém ele de refém e força você e todos os seus outros órgãos internos a continuarem seguindo em frente até a porta de entrada"

    scene bg entrada

    "Ok, vocês tão fora da casa"

    "Você percebe quase que imediatamente que você não faz ideia de como é suposto você encontrar o Abelarde, bom trabalho"

    "Quando ele tava tacando pedra na sua janela ontem ele tava mais ou menos por esse lado, então…"

    "Ok, você enche o peito, se prepara, e…"

    menu chamar_abelarde:
        "Ô CERVO!!!!":
            pass

    "Você sente alguém cutucando as suas costas"

    show abelarde
    cervo "Primeiro"
    "Abelarde sussurra de maneira extremamente vigorosa na sua direção"
    cervo "O que foi que eu falei sobre gritar?!"
    "Você lembra ao Abelarde que ele jogou uma pedra na sua direção e, até onde você tem ciência, isso ainda não pode ser considerado -"
    cervo "Segundo!"
    cervo "Eu quero acreditar que você não sabia exatamente quais eram as consequências de me deixar aqui fora a noite inteira depois de ter me revivido"
    cervo "Porque eu tive que aprender do jeito mais entediante possível que, não importa o quanto um morto se esforce, ele não consegue dormir"
    cervo "O que parece um pouquinho contraditório pra mim!"
    "Huh, pra você parece uma consequência inteiramente natural, você não faz ideia do que -"
    cervo "Olha"
    cervo "Eu passei!"
    cervo "A noite inteira!"
    cervo "Andando!"
    show bg cemiterio dia
    cervo "E eu pensei em jogar mais pedras na sua janela em diversas ocasiões diferentes durante a noite"
    cervo "E mesmo assim eu não joguei"
    cervo "Então eu sinto que você me deve um agradecimento"
    "Ok, você não vai agradecer porque isso é uma expectativa super esquisita mas você espera que a noite dele não tenha sido assim tão -"
    cervo "Uau, ok"
    cervo "De qualquer modo"
    cervo "Eu te chamei aqui por um motivo"
    cervo "Uh"
    cervo "Andando"
    "Claro"
    "Você segue o Abelarde, vocês dão uma volta na casa"

    scene bg hall

    cervo "Eu queria ajuda pra falar com uma tia minha"
    cervo "Ela tá morta, também, o que deve te ajudar"
    cervo "De qualquer modo"
    "Quando Abelarde aponta a mão na sua direção você percebe que ele tá segurando um pedacinho de papel"
    cervo "Por favor"
    cervo "Me permita"

    hide abelarde
    show poema aurora parte_1
    pause
    show poema aurora parte_2
    pause
    show poema aurora parte_3
    pause
    hide poema aurora parte_3
    show abelarde

    "..."
    "Huh"
    "Você diz pro Abelarde que se ele tá procurando críticas, talvez seja uma boa ideia checar a contagem de sílabas poéticas no verso-"
    cervo "Não!"
    cervo "Eu não preciso das suas críticas!"
    "Você diz pro Abelarde que ignorar o que as pessoas pensam sobre o seu trabalho absolutamente vai deixar ele criativamente estagnado, mas ok, ele quem sabe"
    cervo "Não!"
    cervo "O poema não é meu!"
    "Oh, claro, ele tava simplesmente explodindo em prosa roubada, como é costumeiro que se faça em caminhadas desse tipo"
    cervo "Não, olha"
    cervo "É importante"
    cervo "E é bem aqui"
    "Oh? O Abelarde tá atravessando uma janela da casa"
    "Quando ele chega do lado de dentro, ele faz uma cara como quem diz que você devia entrar também"
    "Ok, aparentemente é isso que você tá fazendo hoje"

    if genero == 0:
        "Arrombando uma casa pra qual você foi literalmente convidado"
    elif genero == 1:
        "Arrombando uma casa pra qual você foi literalmente convidada"
    else:
        "Arrombando uma casa pra qual você foi literalmente convidade"

    "Você segue o Abelarde pro lado de dentro"
    "Você dá uma olhada ao redor, parece que vocês foram parar em alguma espécie de ateliê?"
    show bg hall
    cervo "Entendeu?"
    "O que?"

    if genero == 0:
        "Você diz pro Abelarde que já faz um tempinho que ele falou pela última vez e talvez você não esteja inteiramente certo sobre a que é que ele tá se referindo"
    elif genero == 1:
        "Você diz pro Abelarde que já faz um tempinho que ele falou pela última vez e talvez você não esteja inteiramente certa sobre a que é que ele tá se referindo"
    else:
        "Você diz pro Abelarde que já faz um tempinho que ele falou pela última vez e talvez você não esteja inteiramente certe sobre a que é que ele tá se referindo"

    cervo "Ao poema?"
    cervo "Era importante?"
    "Oh, claro, era sobre tinta ou alguma coisa assim?"
    "Você elogia o Abelarde por ter dado um elo de coesão inesperado à sua caminhada"
    "O Abelarde tira o esqueleto do armário"
    "Pera, desculpa, o que?"
    "Não, não, tá certo. O Abelarde acabou de abrir um armário no canto do ateliê e um esqueleto inteiro rolou pra fora"
    "Oh isso é esquisito"
    cervo "É a minha tia"
    "E ela tava num armário?"
    "Você lembra ao Abelarde que vocês literalmente passaram pelo cemitério no caminho até aqui"
    cervo "Eu sei"
    cervo "Mas minha tia era uma artista"
    cervo "Ela ia querer ser enterrada como arte"
    "Você primeiro diz que enfiar um esqueleto num armário é a definição mais liberal de arte que você já ouviu, mas ok"
    "Depois você diz que, uh, na realidade, ela não foi enterrada como arte, porque, uh, ela não foi enterrada, ela foi, uh, enfiada em um armário"
    cervo "Eu vou admitir que eu concordo com você, nesse caso"
    cervo "Mas eu não tava envolvido com os rituais específicos que levaram o resto da família a enfiar ela em um armário, então a culpa não é minha"
    cervo "De qualquer modo"
    cervo "Você pode?"
    "Se você pode o - Oh claro, reviver o cadáver"
    "Abelarde segue seus movimentos quando você se agacha pra ordenar a pilha de ossos jogada no chão"
    "Vocês têm um esqueleto inteiro organizadinho no chão em pouco tempo"
    "Abelarde toma a oportunidade pra se afastar o máximo que o ateliê apertadinho permite"
    cervo "Pra não atrapalhar quando você estiver necromando"
    "Você agradece"
    "Você descansa sua palma na testa do esqueleto no chão"
    "A tia do Abelarde, né?"
    "Ela pulsa contra os seus dedos"
    "Os ossos vagarosamente se ligam um ao outro"
    "Você já fez isso mais vezes do que você consegue contar, mas ver um cadáver voltar a vida?"
    "É absolutamente…"

    show abelarde crop at right
    show gamba crop at left

    gamba "Magnífico..."

    "Opa, bom dia senhora"
    gamba "Bom dia"
    gamba "Aurora, encantada"
    gamba "Peço perdão aos senhores pela minha falta de discrição, mas por favor me perdoem quando eu pergunto que tipo de festa é essa que está acontecendo no meu ateliê?"
    gamba "Vocês vieram pedir um autógrafo, hm? Vieram requisitar um tour pessoal de onde a mágica acontece, hm?"
    cervo "Uau, não"
    cervo "Tia? Lembra de mim? É o Abelarde?"
    gamba "Ora, o pequeno Abelarde é mais baixo do que o senhor de maneira considerável"
    gamba "Talvez mais importante do que isso, ele não é inteiramente feito de osso, hm?"
    gamba "Você deve estar simplesmente se confundindo com o meu sobrinho, o que, após breve consideração, eu posso concluir que é extremamente esquisito"
    cervo "Não!"
    "Abelarde olha pra você como se quisesse que você resolvesse o desentendido por ele"
    "Você sinaliza pra Aurora que talvez ela deva dar uma boa encarada no braço dela pra ver o que ela acha"
    "Ela olha pro próprio braço"
    "Ela foca o olhar em Abelarde, depois no próprio braço de novo"
    gamba "Da minha perspectiva, parece que eu estou positivamente pálida nesta noite, meus caros"
    gamba "A minha aura roxeada emana uma energia simplesmente sobrenatural"
    gamba "Não me digam, não é possível, eu?"
    gamba "Oh, eu morri?"
    cervo "Uh"
    cervo "É, morreu sim, tia"
    gamba "Oh!"
    gamba "Ora, conte-me, como fui enterrada?"
    cervo "Uh"
    "Abelarde dá uma apontada sem graça em direção ao armário do qual Aurora saiu"
    gamba "Oh!"
    gamba "A artisticidade inerente em enfiar um esqueleto em um armário!"
    gamba "Oh, que período para se estar morta!"
    cervo "Com licença?"
    gamba "Oh, eu preciso contar pra minha querida sogrinha o quanto antes! Onde? Onde é que ela foi parar?"
    "Os olhos da Aurora param em um canto vazio da sala, pela expressão dela, parece que esse canto não devia estar vazio"
    gamba "Oh"
    gamba "Isso não é ideal"
    "Você pergunta pra ela o que exatamente ela tá procurando"
    gamba "Oh, o crânio, é claro"
    "Você diz pra ela que isso não explica nada. Na realidade, só serve pra aumentar a sua confusão"
    cervo "Na realidade, esse foi um dos motivos pelos quais a gente veio aqui"
    "Uh, foi?"
    cervo "Se você tiver como contar a sua história sobre esse crânio desde o começo, talvez a gente consiga descobrir onde ele foi parar"
    "A gente consegue?"
    gamba "Oh, claro que eu poderia contar"
    gamba "Admitirei que contar histórias não é exatamente a minha área de maior expertise, mas, bem"
    gamba "Quando minha querida sogrinha faleceu, abençoada seja sua alma"
    gamba "Eu e Pierre, meu cunhado, tivemos uma ideia para homenageá-la"

    #[Silhueta dos crânios]

    #gamba "Pierre cortou o crânio deles em dois pedaços idênticos"
    gamba "Sendo o mais qualificado para usar objetos cortantes, o Pierre partiu o crânio dela ao meio"

    #[Sprites completos dos crânios]
    hide gamba
    hide abelarde
    show cranio1_aurora at center
    show cranio2_pierre at left

    gamba "E cada um de nós dois decorou a sua metade"
    gamba "O plano era que fossem expostos na sala, mas eu não tive tempo de terminar a minha parte antes de, é claro"
    "Claro"

    hide cranio1_aurora
    hide cranio2_pierre
    show abelarde crop at left

    cervo "Você vai ficar feliz em saber que o crânio foi exposto mesmo assim"

    show gamba crop at right

    gamba "Abelarde, você deve estar ciente de que eu realmente preferiria que meu trabalho incompleto não fosse exibido para toda a casa"
    cervo "Uh"
    "Ok, você toma essa como a sua deixa pra tentar fazer alguma coisa pra evitar que a interação continue sendo estranha"
    "Então, uh, como foi que ela morreu?"

    if genero == 0:
        gamba "Que pergunta insensível querido"
    elif genero == 1:
        gamba "Que pergunta insensível querida"
    else:
        gamba "Que pergunta insensível queride"

    "Oh, não era sua intenção -"
    gamba "As garras do inverno cortavam minha garganta naquela noite congelante"
    "Oh, ok"

    hide abelarde
    hide gamba crop
    scene bg black

    gamba "Meus pulmões, que antigamente só guardavam floresta, agora já eram quase que inteiramente vácuo"
    gamba "Eles constringiam com força o pouco que eu conseguia respirar do espectro do outono"
    gamba "Eu passei o inverno inteiro deitada em minha cama, rezando pela chegada da primavera"
    gamba "Passou-se um mês, depois três, depois doze"
    gamba "O inverno nunca acabou"

    scene bg vinhetaaurora

    gamba "Minha única companhia eram os meus quadros"
    gamba "Suas cores quentes sussurravam uma promessa de retorno"
    gamba "Mas o inverno progredia e eles iam perdendo sua saturação"
    gamba "A mesma neve que congelava meus pulmões transformava em gelo sua matiz"
    gamba "E eu pintei mais"
    gamba "Eu procurei a primavera nas minhas composições"
    gamba "E eu ofereci todo o ar que estava contido em mim nessa procura"
    gamba "Mas minhas tintas se apagaram"
    gamba "E quando até o meu mais vibrante vermelho se tornou azul"
    gamba "Eu também o fiz"
    gamba "A doença me consumiu inteiramente"
    gamba "Um espelho do dia fatídico em que eu consumi minha morte"
    gamba "Foi quando as garras do inverno me tocaram pela primeira vez"

    scene bg hall

    show gamba crop

    gamba "Quando eu comi meu primeiro balde de tinta"
    "Com licença?"

    show gamba crop at left
    show abelarde crop at right
    cervo "É, ela comia tinta"

    cervo "A gente tentou pedir pra ela parar, mas?"
    gamba "Abelarde, querido!"
    gamba "A artisticidade inerente em comer tinta!"
    gamba "Esse era um presente que eu simplesmente não podia negar"

    menu:
        "Por quê?":
            pass

    gamba "Pra ficar colorida por dentro"
    "Claro"

    if genero == 0:
        "Você olha pro Abelarde e ele parece tão decepcionado quanto você parece confuso"
    elif genero == 1:
        "Você olha pro Abelarde e ele parece tão decepcionado quanto você parece confusa"
    else:
        "Você olha pro Abelarde e ele parece tão decepcionado quanto você parece confuse"

    "Você olha pro armário de onde o esqueleto tinha saído, Aurora tinha começado a fuçar nos baldes que sobraram dentro dele"
    "Ela pegou uns baldes e se virou pra ir embora?"
    "Oi, senhora?"
    gamba "O quê? Vocês ainda precisam de alguma coisa?"
    gamba "Pouco importa, acabei de ser atingida por inspiração sem precedentes"
    gamba "Eu preciso pintar"
    gamba "Vocês viram as árvores do lado de fora?"

    define escolha_estacao = ""
    menu:
        "É primavera?":
            $escolha_estacao = "primavera"
            pass
        "É verão?":
            $escolha_estacao = "verão"
            pass
        "É outono?":
            $escolha_estacao = "outono"
            pass
        "É inverno?":
            $escolha_estacao = "inverno"
            pass

    "Aurora te oferece o melhor sorriso que a mandíbula ossuda dela consegue produzir"
    gamba "É floresta"

    hide gamba

    "E ela se foi"
    "Sim, pela janela, sem um pingo de hesitação"
    cervo "Huh"
    cervo "Isso não foi produtivo"
    "Nessa parte você consegue concordar"
    cervo "Respondendo a sua pergunta de antes"
    "No lugar de uma explicação sobre do que é que ele tá falando, Abelarde só aponta em direção à porta do armário, agora fechada"
    "Huh, você nota agora que tem um papel enquadrado ali"
    "Você lê"

    hide abelarde
    show poema aurora parte_1
    pause
    show poema aurora parte_2
    pause
    show poema aurora parte_3
    pause
    hide poema aurora parte_3
    show abelarde

    "É o mesmo poema que o Abelarde tinha te mostrado a caminho daqui"
    "Os detalhes sobre envenenar e tinta são um pouquinho mais familiares dessa vez"
    "Parece que ele é vagamente relacionado ao que aconteceu com a tia dele?"
    cervo "É uma explicação exata do que aconteceu com a minha tia"
    cervo "Foi escrito pela minha avó, dona daquele crânio que ela mencionou"
    cervo "Na época em que a minha tia morreu, meu familiares não pensavam nada demais sobre isso"
    cervo "Mas minha avó sabia de muito mais do que a gente achava que ela sabia"
    "Huh"
    cervo "Eu tô tentando descobrir algumas coisas a mais sobre ela"
    cervo "Mas por hoje é só"
    "Abelarde se vira pra sair pela janela"
    cervo "Você devia ir inventar alguma desculpa sobre o seu sumiço pra Palma, e eu espero que você não me mencione"
    cervo "Eu te espero amanhã de novo"

    hide abelarde

    "Ele não espera uma confirmação antes de pular pela janela e voltar em direção à floresta"
    "Huh, ok"
    "Você olha pra trás e lembra que você tá dentro de um cômodo da casa, então você pode simplesmente voltar pela porta"
    "Que conceito"
    "Quando você encontra a Palma de novo você inventa alguma desculpa esquisita sobre estar com alergia por causa do clima de [escolha_estacao] e que você precisa passar o resto do dia na cama"
    "Ela te questiona menos do que você acha que ela provavelmente devia"
    "Quando você sobe pro seu quarto você encontra uma fatia de torta já fria na cabeceira"
    "Você cai no sono sem nem tocar nela"
