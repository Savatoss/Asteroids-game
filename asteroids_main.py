from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import math
import random

DEFAULT_ASTEROIDS_NUM = 5
ship = Ship()
DEGREE = 7
DELTA_X = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
DELTA_Y = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y
ASTEROID_SIZE = 3
INCREASE_SCORE1 = 100
INCREASE_SCORE2 = 50
INCREASE_SCORE3 = 20
WIN_TITLE ="YOU WIN"
WIN_MSG = "Congratulations"
WARNING_TITLE = "You have been hit"
WARNING_MSG = "You lost a life point"
LOSS_TITLE = "GAME OVER"
LOSS_MSG = "YOU LOST"
QUIT_TITLE = "YOU QUIT"
QUIT_MSG = "HA HA"

class GameRunner:
    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.asteroids_lst = []
        self.torpedo_lst=[]
        self.lives= 3
        self.score=0


        for i in range(asteroids_amount):
            x_pos = random.randrange(self.__screen_min_x, self.__screen_max_x)
            y_pos = random.randrange(self.__screen_min_y, self.__screen_max_y)
            asteroid = Asteroid(x_pos, y_pos, ASTEROID_SIZE)
            if asteroid.has_intersection(ship) == False:
                self.asteroids_lst.append(asteroid)
                self.__screen.register_asteroid(self.asteroids_lst[i], asteroid.size)
                self.__screen.draw_asteroid(asteroid, x_pos, y_pos)


    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def new_heading(self):
        """
        a method that changes the head degree in the ship
        :return: the new head direction
        """
        if self.__screen.is_right_pressed():
            ship.head_dir -= DEGREE
            return ship.head_dir

        elif self.__screen.is_left_pressed():
            ship.head_dir += DEGREE
            return ship.head_dir

    def acceleration(self,obj,num):
        """
        a method that calculates the acceleration of an object
        :param obj:an object from a class
        :param num:(int)
        :return:None
        """
        if (self.__screen.is_up_pressed() and num == 1)or (num == 2):
            new_speed_x = ship.x_velocity + num*(math.cos(math.radians(ship.head_dir)))
            new_speed_y = ship.y_velocity + num*(math.sin(math.radians(ship.head_dir)))
            obj.x_velocity = new_speed_x
            obj.y_velocity = new_speed_y

    def new_pos(self, obj):
        """
        a method that reinstate the ship's position in both axis through a a formula
        :param obj:an object from a class
        :return: returns the new position in both coordinates
        """
        new_pos_x = Screen.SCREEN_MIN_X + (obj.x_pos + obj.x_velocity - Screen.SCREEN_MIN_X) % DELTA_X
        new_pos_y = Screen.SCREEN_MIN_Y + (obj.y_pos + obj.y_velocity - Screen.SCREEN_MIN_Y) % DELTA_Y
        obj.x_pos = new_pos_x
        obj.y_pos = new_pos_y
        return new_pos_x, new_pos_y

    def move_asteroids(self):
        """
        a method that moves the asteroids on the screen
        :return: None
        """
        for i in range(len(self.asteroids_lst)):
            new_pos_x, new_pos_y = self.new_pos(self.asteroids_lst[i])
            self.__screen.draw_asteroid(self.asteroids_lst[i], new_pos_x, new_pos_y)

    def collision(self):
        """
        a method that omits one life point when there is a collision between the ship and the asteroid
        and shows a messages when hit, also it ends the game when the number of lives is zero
        :return: None
        """
        for i in self.asteroids_lst:
            if i.has_intersection(ship):
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(i)
                self.asteroids_lst.remove(i)
                if self.lives > 1:
                    self.lives -= 1
                    self.__screen.show_message(WIN_TITLE, WARNING_MSG)
                else:
                    self.__screen.show_message(LOSS_TITLE,LOSS_MSG)
                    self.__screen.end_game()
                    sys.exit()


    def shoot(self):
        """
        a method that puts and moves the appropriate torpedos on screen
        :return:None
        """
        if self.__screen.is_space_pressed() and len(self.torpedo_lst) <= 10:
            torpedo=Torpedo(ship.x_pos,ship.y_pos,ship.head_dir)
            self.acceleration(torpedo, 2)
            self.torpedo_lst.append(torpedo)
            self.__screen.register_torpedo(torpedo)
            self.__screen.draw_torpedo(torpedo,ship.x_pos,ship.y_pos,ship.head_dir)

    def score_increase(self,obj):
        """
        a method that increases the score of the game in accordance to the size of the asteroid and displays it on screen
        :param obj: an object from a class
        :return: None
        """
        if obj.size == 1:
            self.score += INCREASE_SCORE1
        elif obj.size == 2:
            self.score += INCREASE_SCORE2
        elif obj.size == 3:
            self.score += INCREASE_SCORE3
        self.__screen.set_score(self.score)

    def update_torpedo(self):
        """
        a method that updates the time a torpedo is displayed on screen
        :return: None
        """
        for i in self.torpedo_lst:
            if i.life > 0:
                new_pos_x, new_pos_y = self.new_pos(i)
                self.__screen.draw_torpedo(i, new_pos_x, new_pos_y,i.dir)
                i.life -= 1
            else:
                self.torpedo_lst.remove(i)
                self.__screen.unregister_torpedo(i)

    def hit(self):
        """
        a method when a torpedo hits an asteroids it breaks into parts and then it displays the different
        size parts on screen
        :return:None
        """
        for i in self.asteroids_lst:
            for j in self.torpedo_lst:
                if i.has_intersection(j):
                    self.score_increase(i)
                    if i.size == 1:
                        self.__screen.unregister_asteroid(i)
                        self.asteroids_lst.remove(i)
                        self.torpedo_lst.remove(j)
                        self.__screen.unregister_torpedo(j)
                    else:
                        i.size -= 1
                        divisor =math.sqrt((i.x_velocity)**2+(i.y_velocity)**2)
                        i.x_velocity=(i.x_velocity + j.x_velocity)/divisor
                        i.y_velocity=(i.y_velocity+j.y_velocity)/divisor
                        asteroid2 = Asteroid(i.x_pos,i.y_pos,i.size)
                        asteroid1 = Asteroid(i.x_pos,i.y_pos,i.size)
                        asteroid1.x_velocity = i.x_velocity
                        asteroid1.y_velocity = i.y_velocity
                        asteroid2.x_velocity = -1*i.x_velocity
                        asteroid2.y_velocity = -1*i.y_velocity
                        self.asteroids_lst.append(asteroid1)
                        self.asteroids_lst.append(asteroid2)
                        self.__screen.register_asteroid(asteroid1, i.size)
                        self.__screen.register_asteroid(asteroid2, i.size)
                        self.__screen.draw_asteroid(asteroid1, i.x_pos, i.y_pos)
                        self.__screen.draw_asteroid(asteroid2, i.x_pos, i.y_pos)
                        self.__screen.unregister_asteroid(i)
                        self.asteroids_lst.remove(i)
                        self.torpedo_lst.remove(j)
                        self.__screen.unregister_torpedo(j)

    def _game_loop(self):
        # TODO: Your code goes here
        self.new_heading()
        self.acceleration(ship,1)
        ship.x_pos, ship.y_pos = self.new_pos(ship)
        self.__screen.draw_ship(ship.x_pos, ship.y_pos, ship.head_dir)
        self.move_asteroids()
        self.collision()
        self.shoot()
        self.update_torpedo()
        self.hit()
        if self.__screen.should_end():
            self.__screen.show_message(QUIT_TITLE,QUIT_MSG)
            self.__screen.end_game()
            sys.exit()
        elif len(self.asteroids_lst) == 0:
            self.__screen.show_message(WIN_TITLE,WIN_MSG)
            self.__screen.end_game()
            sys.exit()



def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
