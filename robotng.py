from robot import Robot

class RobotNG(Robot):
    """Classe des robots de nouvelle génération"""


    def __init__(self,nom):
        super(RobotNG, self).__init__(nom)
        self._turbo = False

    def _avance(self,nb=1):
        if(self._turbo):
            nb *= 3
        if(self.direction == 0):
            self.x += nb
        elif(self.direction == 1):
            self.y += nb
        elif(self.direction == 2):
            self.x -= nb
        else:
            self.y -= nb

    def _gauche(self):
        if(self.direction > 0):
            self.direction += 1
            return
        self.direction = 3

    def _demiTour(self):
        if(self.direction < 2):
            self.direction += 2
        else:
            self.direction -= 2

    def _switch_turbo(self):
        if(self._turbo):
            self._turbo = False
        else:
            self._turbo = True
