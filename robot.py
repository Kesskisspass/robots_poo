class Robot:

    """
    Classe des robots 1ère génération
    """

    direction=["Nord","Est","Sud","Ouest"]

    def __init__(self,nom,x=0,y=0,index_direction=1):
        self.nom = nom
        self.x = x
        self.y = y
        self.direction = index_direction

    def _avance(self):
        if(self.direction == 0):
            self.x += 1
        elif(self.direction == 1):
            self.y += 1
        elif(self.direction == 2):
            self.x -= 1
        else:
            self.y -= 1

    def _droite(self):
        if(self.direction < 3):
            self.direction += 1
            return
        self.direction = 0

    def _etat(self):
        print(f"Position x:{self.x}, y: {self.y}, Direction: {Robot.direction[self.direction]} ")
