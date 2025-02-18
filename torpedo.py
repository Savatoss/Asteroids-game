RADIUS_TORPEDO=4
TORPEDO_LIFE = 200
class Torpedo:
    def __init__(self,x_pos,y_pos,head_dir):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = 0
        self.y_velocity = 0
        self.life = TORPEDO_LIFE
        self.dir = head_dir
    def radius(self):
        """
        a method that returns the radius of a torpedo
        :return: returns the radius of a torpedo
        """
        return RADIUS_TORPEDO
