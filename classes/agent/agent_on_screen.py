from pygame_menu.menu import SELECT_KEY
from entities.screen import Screen

class Agent_On_Screen:
    point = [0, 0]

    def __init__(self, start) -> None:
        self.point[0] = start[0] * Screen.square_size
        self.point[1] = start[1] * Screen.square_size

    def move(self, direction):
        if direction == 0:
            self.move_up()
        elif direction == 1:
            self.move_up_right()
        elif direction == 2:
            self.move_right()
        elif direction == 3:
            self.move_right_down()
        elif direction == 4:
            self.move_down()
        elif direction == 5:
            self.move_down_left()
        elif direction == 6:
            self.move_left()
        elif direction == 7:
            self.move_leftUp()

    def move_up(self):
        self.point[1] -= Screen.square_size

    def move_up_right(self):
        self.move_up()
        self.move_right()

    def move_right(self):
        self.point[0] += Screen.square_size
    
    def move_right_down(self):
        self.move_right()
        self.move_down()

    def move_down(self):
        self.point[1] += Screen.square_size

    def move_down_left(self):
        self.move_down()
        self.move_left()


    def move_left(self):
        self.point[0] -= Screen.square_size
    
    def move_leftUp(self):
        self.move_left()
        self.move_up()
 