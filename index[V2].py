from microbit import *
from mb_robot_maqueen import *
from random import *
import music
import neopixel

robot = Robot() #Appelle a la class Robot() dans la dépendance maqueen

#===================================/
#===|Eteint le Robot par défaut|===/
#=================================/
RobotStart = 0

#==============================/
#=====|Allume le pad LED|=====/
#============================/
display.on

#====================================/
#=====|Allume le Haut parleur|=====/
#==================================/
speaker.on

#=================================/
#=====|Variable Hors Boucle|=====/
#===============================/
Recherche = -1
DistanceLimit = 80
AccAvancer = 25

#======================/
#=====|Class BOT|=====/
#====================/
class BOT():
    class PAD_LED():
        def SHOW_1():
            #Affiche un 1 sur le Pad-LED
            display.clear
            display.show(Image(
                '00990:'
                '09090:'
                '90090:'
                '00090:'
                '99999:'
            ))
        def SHOW_0():
            #Affiche un 0 sur le Pad LED
            display.clear
            display.show(Image(
                '09990:'
                '90009:'
                '90009:'
                '90009:'
                '09990:'
            ))
    class Mouvement():
        def stop():
            #Robot Stop
            robot.run(0,0,0)
            robot.run(1,0,0)
        def Avant():
            #Je déclenche la marche avant
            robot.run(0,0,255)
            robot.run(1,0,255)
        def Droite():
            robot.run(0,0,255)
            robot.run(1,1,255)
        def Gauche():
            robot.run(0,1,255)
            robot.run(1,0,255)
        class SEARCH():
            def Gauche():
                robot.run(0,1,50)
                robot.run(1,0,50)
            def Droite():
                robot.run(0,0,50)
                robot.run(1,1,50)
    class Light():
        class RGB():
            def RED():
                neopixel.NeoPixel.clear
                #Je selectionne toute les RBG pour les définir en Rouge
                np = neopixel.NeoPixel(microbit.pin15, 4)
                np[0] = (255, 0, 0)
                np[1] = (255, 0, 0)
                np[2] = (255, 0, 0)
                np[3] = (255, 0, 0)
                #Je mais a jour les RGB pour affiché de nouveau réglage
                np.show()
            def PURPLE():
                #Je selectionne toute les RBG pour les définir en Violet
                np = neopixel.NeoPixel(microbit.pin15, 4)
                np[0] = (132, 0, 186)
                np[1] = (132, 0, 186)
                np[2] = (132, 0, 186)
                np[3] = (132, 0, 186)
                #Je mais a jour les RGB pour affiché de nouveau réglage
                np.show()
            def BLUE():
                neopixel.NeoPixel.clear
                #Je selectionne toute les RBG pour les définir en bleu
                np = neopixel.NeoPixel(microbit.pin15, 4)
                np[0] = (255, 0, 255)
                np[1] = (255, 0, 255)
                np[2] = (255, 0, 255)
                np[3] = (255, 0, 255)
                #Je mais a jour les RGB pour affiché de nouveau réglage
                np.show()
            def GREEN():
                #Je définis toute les RGB en vert
                np = neopixel.NeoPixel(microbit.pin15, 4)
                np[0] = (0, 255, 0)
                np[1] = (0, 255, 0)
                np[2] = (0, 255, 0)
                np[3] = (0, 255, 0)
                #mise a jour des RGB pour affiché de nouveau réglage
                np.show()
        class LED():
            def stop():
                #J'éteint les LED
                pin12.write_digital(0)
                pin8.write_digital(0)
            def Droite():
                #J'allume la LED droite
                pin12.write_digital(1)
                pin8.write_digital(0)
            def Gauche():
                #J'allume la LED Gauche
                pin12.write_digital(0)
                pin8.write_digital(1)
    class console():
        def READY():
            print('╔═══════════════╦╕')
            print('║Robot de combat║>Je suis prét !!')
            print('╚═══════════════╩╛')
        def STAND_BY():
            print('╔═══════════════╦╕')
            print('║Robot de combat║>Mise en veille !!')
            print('╚═══════════════╩╛')
        def LINE_BLACK_DETECT():
            print('╔═══════════════╦╕')
            print('║Robot de combat║>Ligne Noir détecter. Marche arriére !!')
            print('╚═══════════════╩╛')
        def ATTACK():
            print('╔═══════════════╦╕')
            print("║Robot de combat║>Object Repérer j'attaque !!")
            print('╚═══════════════╩╛')
        class SEARCH():
            def Droite():
                print('╔═══════════════╦╕')
                print('║Robot de combat║>Recherche Activée Rotation sur la Droite !')
                print('╚═══════════════╩╛')
            def Gauche():
                print('╔═══════════════╦╕')
                print('║Robot de combat║>Recherche Activée Rotation sur la Gauche !')
                print('╚═══════════════╩╛')

while True:

    #========================================================/
    #=====|Selectionner aléatoirement dans cette liste|=====/
    #======================================================/
    Liste_Recherche = [0, 1]

    #=====================/
    #=====|Variable|=====/
    #===================/
    #Bouton de la microbit
    BoutonA = button_a.is_pressed()
    BoutonB = button_b.is_pressed()

    #========================================================/
    #=====|Si le Bouton A est présser allumer le robot|=====/
    #======================================================/
    if ( BoutonA == True ):
        RobotStart = 1
        BOT.console.READY()
        #Joue la musique POWER_UP
        music.play(music.POWER_UP)
        BOT.PAD_LED.SHOW_1()

    #===============================================================/
    #=====|Sinon si le Bouton B est présser éteindre le Robot|=====/
    #=============================================================/
    if ( BoutonB == True ):
        RobotStart = 0
        BOT.console.STAND_BY()
        #Joue la musique POWER_DOWN
        music.play(music.POWER_DOWN)
        BOT.PAD_LED.SHOW_0()

    #====================================/
    #=====|Si le Robot est allumer|=====/
    #==================================/
    if ( RobotStart == 1 ):

        #=======================================/
        #=====|Détection de la ligne Noir|=====/
        #=====================================/
        while ( pin13.read_digital() == 0 or pin14.read_digital() == 0 and RobotStart == 1 ):
            #Je déclenche la marche arriére
            if ( pin13.read_digital() == 0 ):
                robot.run(0,1,255)
            else:
                robot.run(0,0,0)
            if ( pin14.read_digital() == 0 ):
                robot.run(1,1,255)
            else:
                robot.run(1,0,0)
            if ( button_b.is_pressed() == True ):
                RobotStart = 0
            Recherche = -1
            music.play(music.JUMP_UP)
            BOT.Light.RGB.PURPLE()
            BOT.console.LINE_BLACK_DETECT()

        #=================================================================/
        #=====|Détection si il y a un objet proche a moin de 125 cm|=====/
        #===============================================================/
        if ( robot.distance() < DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 ): #Si la distance est inférieure a 125
            BOT.Mouvement.Avant()
            #J'éteint le mode Recherche
            Recherche = -1
            BOT.Light.LED.stop()
            BOT.Light.RGB.RED()
            BOT.console.ATTACK()

        #=======================================================================/
        #=====|Détection si il n'y a pas d'object proche a moin de 125 cm|=====/
        #=====================================================================/
        Recherche = choice(Liste_Recherche)
        while ( robot.distance() > DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 and RobotStart == 1 ): #Tant que la distance est supérieur a 125
            BOT.Light.RGB.BLUE()
            if ( button_b.is_pressed() == True ):
                RobotStart = 0

                #======================/
                #=====|Recherche|=====/
                #====================/
            while ( robot.distance() > DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 and accelerometer.get_z() < AccAvancer ):
                BOT.Light.RGB.BLUE()
                if ( Recherche == 1 ): #Si le mode Recherche est a 1 commencer la recherche a droite
                    BOT.Mouvement.SEARCH.Droite()
                    BOT.Light.LED.Droite()
                    BOT.console.SEARCH.Droite()

                if ( Recherche == 0 ): #Si la Recherche est a 0 commencer la recherche a gauche
                    BOT.Mouvement.SEARCH.Gauche()
                    BOT.Light.LED.Gauche()
                    BOT.console.SEARCH.Gauche()

            #=========================================/
            #=====|Si il se fait pousser(Alpha)|=====/
            #=======================================/
            if ( accelerometer.get_z() > AccAvancer ):
                if ( Recherche == 1 ):
                    BOT.Mouvement.Droite()
                    BOT.Light.LED.Droite()
                if ( Recherche == 0 ):
                    BOT.Mouvement.Gauche()
                    BOT.Light.LED.Gauche()

    #=========================================/
    #=====|Sinon si le Robot est éteint|=====/
    #=======================================/
    if ( RobotStart == 0 ):
        Recherche = -1
        BOT.Light.LED.stop()
        BOT.Light.RGB.GREEN()
        #Robot Stop
        BOT.Mouvement.stop()