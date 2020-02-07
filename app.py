from robot import Robot
from robotng import RobotNG

# Le joueur choisit le nom de son robot
name = input("Veuillez créer un robot, choisissez un nom: \n")

# Puis son type (Robot ou RobotNG)
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
# Affichage de l'état initial
robot._etat()

if(robot.__class__.__name__ == "Robot"):
    print("Classe 1")
    actions = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'd' pour aller à Droite,\n - 'q' pour Quitter \n")
else:
    print("Classe 2")
    actions = input("Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n")


# Proposition des actions disponibles
action = actions

while((action != "a") | (type != "g") | (action != "d") | (type != "t") | (type != "q")):
    if(action != "q"):
        if(action == "a"):
            robot._avance()
            action = actions
        elif(action == "g"):
            robot._gauche()
            action = actions
        elif(action == "d"):
            robot._droite()
            action = actions
    else:
        robot._switch_turbo()
        action = actions
    print("*****\nVous quittez le jeu, au revoir !\n*****")
    break
