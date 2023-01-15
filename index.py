from microbit import *
from mb_robot_maqueen import *
from random import *
import music
import neopixel
#from numpy import *

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
#=====|Allumer le Haut parleur|=====/
#==================================/
speaker.on

#=================================/
#=====|Variable Hors Boucle|=====/
#===============================/
NULL = 'undefined'
Recherche = -1
Avancer = NULL
#Reculer = NULL
DistanceLimit = 80
AccAvancer = 25

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
        #Envois dans la console:
        print('╔═══════════════╦╕')
        print('║Robot de combat║>Je suis prét !!')
        print('╚═══════════════╩╛')
        #Joue la musique POWER_UP
        music.play(music.POWER_UP)
        #Affiche un 1 sur le Pad LED
        display.clear
        display.show(Image(
            '00990:'
            '09090:'
            '90090:'
            '00090:'
            '99999:'
        ))

    #===============================================================/
    #=====|Sinon si le Bouton B est présser éteindre le Robot|=====/
    #=============================================================/
    if ( BoutonB == True ):
        RobotStart = 0
        #Envois dans la console:
        print('╔═══════════════╦╕')
        print('║Robot de combat║>Mise en veille !!')
        print('╚═══════════════╩╛')
        #Joue la musique POWER_DOWN
        music.play(music.POWER_DOWN)
        #Affiche un 0 sur le Pad LED
        display.clear
        display.show(Image(
            '09990:'
            '90009:'
            '90009:'
            '90009:'
            '09990:'
        ))

    #====================================/
    #=====|Si le Robot est allumer|=====/
    #==================================/
    if ( RobotStart == 1 ):

        #========================================/
        #=====|Détection de la ligne rouge|=====/
        #======================================/
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
            Avancer = NULL
            Recherche = -1
            music.play(music.JUMP_UP)
            neopixel.NeoPixel.clear
            #Je selectionne toute les RBG pour les définir en Violet
            np = neopixel.NeoPixel(microbit.pin15, 4)
            np[0] = (132, 0, 186)
            np[1] = (132, 0, 186)
            np[2] = (132, 0, 186)
            np[3] = (132, 0, 186)
            #Je mais a jour les RGB pour affiché de nouveau réglage
            np.show()
            print('╔═══════════════╦╕')
            print('║Robot de combat║>Ligne Noir détecter. Marche arriére !!')
            print('╚═══════════════╩╛')

        #=================================================================/
        #=====|Détection si il y a un objet proche a moin de 125 cm|=====/
        #===============================================================/
        if ( robot.distance() < DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 ): #Si la distance est inférieure a 125
            #Je déclenche la marche avant
            robot.run(0,0,255)
            robot.run(1,0,255)
            #Reculer = 0
            #Avancer = 1
            #J'éteint le mode Recherche
            Recherche = -1
            #J'éteint la LED avant-droite du robot
            pin12.write_digital(0)
            pin8.write_digital(0)
            neopixel.NeoPixel.clear
            #Je selectionne toute les RBG pour les définir en Rouge
            np = neopixel.NeoPixel(microbit.pin15, 4)
            np[0] = (255, 0, 0)
            np[1] = (255, 0, 0)
            np[2] = (255, 0, 0)
            np[3] = (255, 0, 0)
            #Je mais a jour les RGB pour affiché de nouveau réglage
            np.show()
            print('╔═══════════════╦╕')
            print("║Robot de combat║>Object Repérer j'attaque !!")
            print('╚═══════════════╩╛')

        #=======================================================================/
        #=====|Détection si il n'y a pas d'object proche a moin de 125 cm|=====/
        #=====================================================================/
        Recherche = choice(Liste_Recherche)
        while ( robot.distance() > DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 and RobotStart == 1 ): #Tant que la distance est supérieur a 125
            #J'arréte d'avancer
            Avancer = NULL
            #J'allume le mode Recherche
            #Recherche = choice(Liste_Recherche)
            #Recherche=0
            #Random.random()
            neopixel.NeoPixel.clear
            #Je selectionne toute les RBG pour les définir en bleu
            np = neopixel.NeoPixel(microbit.pin15, 4)
            np[0] = (255, 0, 255)
            np[1] = (255, 0, 255)
            np[2] = (255, 0, 255)
            np[3] = (255, 0, 255)
            #Je mais a jour les RGB pour affiché de nouveau réglage
            np.show()
            if ( button_b.is_pressed() == True ):
                RobotStart = 0

                #======================/
                #=====|Recherche|=====/
                #====================/
            while ( robot.distance() > DistanceLimit and pin13.read_digital() == 1 and pin14.read_digital() == 1 and accelerometer.get_z() < AccAvancer ):
                neopixel.NeoPixel.clear
                #Je selectionne toute les RBG pour les définir en bleu
                np = neopixel.NeoPixel(microbit.pin15, 4)
                np[0] = (0, 0, 255)
                np[1] = (0, 0, 255)
                np[2] = (0, 0, 255)
                np[3] = (0, 0, 255)
                #Je mais a jour les RGB pour affiché de nouveau réglage
                np.show()
                print("Recherche:",Recherche)
                if ( Recherche == 1 ): #Si le mode Recherche est a 1 commencer la recherche a droite
                    robot.run(0,0,50)
                    robot.run(1,1,50)
                    #J'allume la LED avant-droite
                    pin12.write_digital(1)
                    pin8.write_digital(0)
                    print('╔═══════════════╦╕')
                    print('║Robot de combat║>Recherche Activée Rotation sur la Droite !')
                    print('╚═══════════════╩╛')

                if ( Recherche == 0 ): #Si la Recherche est a 0 commencer la recherche a gauche
                    robot.run(0,1,50)
                    robot.run(1,0,50)
                    #J'allume la LED avant-gauche
                    pin8.write_digital(1)
                    pin12.write_digital(0)
                    print('╔═══════════════╦╕')
                    print('║Robot de combat║>Recherche Activée Rotation sur la Gauche !')
                    print('╚═══════════════╩╛')

            #==================================/
            #=====|Si il se fait pousser|=====/
            #================================/
            if ( accelerometer.get_z() > AccAvancer ):
                if ( Recherche == 1 ):
                    robot.run(0,0,255)
                    robot.run(1,1,255)
                    #J'allume la LED avant-droite
                    pin12.write_digital(1)
                    pin8.write_digital(0)
                if ( Recherche == 0 ):
                    robot.run(0,1,255)
                    robot.run(1,0,255)
                    #J'allume la LED avant-gauche
                    pin8.write_digital(1)
                    pin12.write_digital(0)

    #=========================================/
    #=====|Sinon si le Robot est éteint|=====/
    #=======================================/
    if ( RobotStart == 0 ):
        #J'arréte tout les mouvement
        Avancer = NULL
        Droite = NULL
        Gauche = NULL
        Reculer = NULL
        Recherche = -1
        #J'éteint les LED a l'avant du Robot
        pin12.write_digital(0)
        pin8.write_digital(0)
        #Je définis toute les RGB en vert
        np = neopixel.NeoPixel(microbit.pin15, 4)
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        #Je mais a jour les RGB pour affiché de nouveau réglage
        np.show()
        #Robot Stop
        robot.run(0,0,0)
        robot.run(1,0,0)

    #========================/
    #=====|Déplacement|=====/
    #======================/
    #(Abandonner car trop lent)
    #if ( Avancer == 1 ): #Marche avant vitesse Max
    #    robot.run(0,0,255)
    #    robot.run(1,0,255)
    #else:
        #Robot Stop
    #    robot.run(0,0,0)
    #    robot.run(1,0,0)
    #    if ( Reculer == 1 ): #Marche arriére vitesse Max
    #        robot.run(0,1,255)
    #        robot.run(1,1,255)
    #    else:
    #        #Robot Stop
    #        robot.run(0,0,0)
    #        robot.run(1,0,0)