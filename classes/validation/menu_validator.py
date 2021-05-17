from pygame.constants import SCALED
from entities.screen import Screen
import validators

class Menu_Validator:
    
    def control():
        control_list = []
        control_list.append(validators.between(Screen.matrix_x_y[0], min=2))
        control_list.append(validators.between(Screen.matrix_x_y[1], min=2))

        control_list.append(validators.between(Screen.agent_x_y[0], min=0))
        control_list.append(validators.between(Screen.agent_x_y[0], max = (Screen.matrix_x_y[0] -1)))

        control_list.append(validators.between(Screen.agent_x_y[1], min=0))
        control_list.append(validators.between(Screen.agent_x_y[1], max = (Screen.matrix_x_y[1]) -1))

        control_list.append(validators.between(Screen.goal_x_y[0], min=0))
        control_list.append(validators.between(Screen.goal_x_y[0], max = (Screen.matrix_x_y[0]) -1))

        control_list.append(validators.between(Screen.goal_x_y[1], min=0))
        control_list.append(validators.between(Screen.goal_x_y[1], max = (Screen.matrix_x_y[1]) -1))

        control_list.append(validators.between(Screen.hurdle_rate, min=1, max = 9))

        control_list.append(validators.between(Screen.learning_rate, min=0.1, max = 1))

        for i in control_list:
            if i != True:
                return False
        return True
