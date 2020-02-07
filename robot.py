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
        self._etat()

    def _droite(self):
        if(self.direction < 3):
            self.direction += 1
        else:
            self.direction = 0
        self._etat()

    def _etat(self):
        str_turbo = ""
        try:
            if(self._turbo):
                str_turbo = "le mode Turbo est activé"
            elif(self._turbo == False):
                str_turbo = "le mode Turbo est desactivé"
            pass
        except AttributeError:
            str_turbo = "pas de mode Tubo sur ce modèle"
        print(f"====\n{self.nom} est un robot de type {self.__class__.__name__},\nPosition x:{self.x}, y: {self.y}, \nDirection: {Robot.direction[self.direction]}, \n{str_turbo}\n=====\n")
