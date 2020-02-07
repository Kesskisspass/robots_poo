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
    actions = "Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'd' pour aller à Droite,\n - 'q' pour Quitter \n"
else:
    print("Classe 2")
    actions = "Veuillez entrer une action:\n - 'a' pour Avancer,\n - 'g' pour aller à Gauche,\n - 'd' pour aller à Droite,\n - 't' pour activer le Turbo !\n - 'q' pour Quitter \n"


# Proposition des actions disponibles
def ask_actions():
    action = input(actions)
    return action
action = ask_actions()

while((action != "a") | (type != "g") | (action != "d") | (type != "t") | (type != "q")):
    if(action != "q"):
        if(action == "a"):
            robot._avance()
            action = ask_actions()
        elif(action == "g"):
            robot._gauche()
            action = ask_actions()
        elif(action == "d"):
            robot._droite()
            action = ask_actions()
        else:
            robot._switch_turbo()
            action = ask_actions()
    else:
        print("*****\nVous quittez le jeu, au revoir !\n*****")
        break
