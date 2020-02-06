class Robot:

    """
    Classe des robots
    """

    direction=["Nord","Est","Sud","Ouest"]

    def __init__(self,nom,x=0,y=0,index_direction=2)
        self.nom = nom
        self.x = x
        self.y = y
        self.direction = index_direction

    def __avance():
        if(self_direction == 1):
            self.x += 1
        elif(self.direction == 2):
            self.y += 1
        elif(self.direction == 3):
            self.x -= 1
        else:
            self.y -= 1

    def __droite():
        if(self.direction < 4):
            self.direction += 1
            return
        self.direction = 0

    def __etat():
        print(f"Position x:{self.x}, y: {self.y}, Direction: {self.direction}, ")

    
