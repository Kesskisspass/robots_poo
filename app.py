from robot import Robot
from robotng import RobotNG

name = input("Veuillez créer un robot, choisissez un nom: \n")

type = 0
while((type != "1") | (type != "2")):
    type = input("Bien, veuillez maintenant choisir le type de robot:\n -'1' pour normal \n -'2' pour nouvelle génération\n")
    if(int(type) == 1):
        robot = Robot(name)
        break
    elif(int(type) == 2):
        robot = RobotNG(name)
        break
    else:
        print("Veuillez choisir 1 ou 2 !")
robot._etat()

action = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")

while((action != "a") | (type != "g") | (action != "d") | (type != "t") | (type != "q")):
    if(action != "q"):
        if(action == "a"):
            robot._avance()
            action = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")

        elif(action == "g"):
            robot._gauche()
            action = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")

        elif(action == "d"):
            robot._droite()
            action = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")

        else:
            robot._switch_turbo()
            action = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")
    else:
        print("*****\nVous quittez le jeu, au revoir !\n*****")
        break
