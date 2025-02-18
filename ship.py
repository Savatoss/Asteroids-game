y_pos = 0
x_pos = 0
head_dir = 0
RADIUS_SHIP=1

class Ship:

    def __init__(self):
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.x_velocity = 0
        self.y_velocity = 0
        self.head_dir = head_dir

    def radius(self):
        """
        a method that returns the ships radius
        :return: ship's radius
        """
        return RADIUS_SHIP
