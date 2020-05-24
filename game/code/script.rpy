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

    
    scene bg borboleta
    e "Bom dia"

    return
