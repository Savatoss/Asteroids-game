import math
import random
ASTROID_SIZE = 3
SPEED_RANGE = [1,4]
R1=10
R2=5
class Asteroid:
    def __init__(self,x_pos,y_pos,size=ASTROID_SIZE):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velocity = self.random_velocity()
        self.y_velocity = self.random_velocity()
        self.size = size

    def random_velocity(self):
        """
        a methos that return a random value for the asteroids speed
        :return: return a random value for the asteroids speed
        """
        return random.randint(SPEED_RANGE[0],SPEED_RANGE[1]+1)



    def has_intersection(self, obj):
        """
        a methos that calculates the interesction between two objects
        :param obj: object from a class
        :return: a boolean
        """
        distance = math.sqrt(pow(obj.x_pos-self.x_pos,2)+pow(obj.y_pos-self.y_pos,2))
        if distance <= self.radius() + obj.radius():
            return True
        return False

    def radius(self):
        """
        a method that returns the radius of an asteroid
        :return: returns the radius of an asteroid
        """
        return self.size * R1 - R2
