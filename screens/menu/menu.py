from screens.graphic.graphic import Graphic
import pygame
import pygame_menu
from entities.screen import Screen
from classes.matrix.matrix import Matrix
from classes.agent.agent import Agent
from screens.maze.maze import Maze
from screens.game.game import Game

class Menu:
    pygame.init()
    surface = pygame.display.set_mode((Screen.window_width, Screen.window_height))

    menu = pygame_menu.Menu('Q-Learning', Screen.window_width, Screen.window_height, theme=pygame_menu.themes.THEME_DARK)
    
    def set_mode(value):
        Screen.mode = value

    def start_the_game():
        my_matrix = Matrix(Screen.matrix_x_y[0], Screen.matrix_x_y[1], Screen.agent_x_y, Screen.goal_x_y, Screen.hurdle_rate)
        my_agent = Agent(my_matrix.matrix_map, my_matrix.matrix_r,
                my_matrix.matrix_q, Screen.learning_rate,
                my_matrix.start_point, my_matrix.goal_point)

        Screen.resize(my_matrix.row, my_matrix.column)

        maze = Maze(my_matrix.matrix_map, my_matrix.row, my_matrix.column)
        game = Game(maze, Screen.window_width, Screen.window_height, Screen.agent_x_y)
        game.on_execute(my_agent, my_matrix)
    
    def set_matrix_x(value):
        Screen.matrix_x_y[0] = value

    def set_matrix_y(value):
        Screen.matrix_x_y[1] = value

    def set_matrix_hurdle_rate(value):
        Screen.hurdle_rate = value

    def set_learning_rate(value):
        Screen.learning_rate = value
    
    def set_agent_x(value):
        Screen.agent_x_y[0] = value
    
    def set_agent_y(value):
        Screen.agent_x_y[1] = value

    def set_goal_x(value):
        Screen.goal_x_y[0] = value

    def set_goal_y(value):
        Screen.goal_x_y[1] = value

    def show_graphic():
        Graphic.draw_graphic()

    def start_menu(self):
        self.menu.mainloop(self.surface)

    menu.add.label('Oyun Alanı')
    menu.add.text_input('X: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.matrix_x_y[0], onchange=set_matrix_x)
    menu.add.text_input('Y: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.matrix_x_y[1], onchange=set_matrix_y)
    
    menu.add.text_input('Engel Oranı(10 üzerinden): ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.hurdle_rate, onchange=set_matrix_hurdle_rate)
    menu.add.text_input('Öğrenme Oranı: ', input_type=pygame_menu.locals.INPUT_FLOAT, default=Screen.learning_rate, onchange=set_learning_rate)
    
    menu.add.label('Ajanın Konumu')
    menu.add.text_input('X: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.agent_x_y[0], onchange=set_agent_x)
    menu.add.text_input('Y: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.agent_x_y[1], onchange=set_agent_y)
    
    menu.add.label('Hedef Konumu')
    menu.add.text_input('X: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.goal_x_y[0], onchange=set_goal_x)
    menu.add.text_input('Y: ', input_type=pygame_menu.locals.INPUT_INT, default=Screen.goal_x_y[1], onchange=set_goal_y)

    menu.add.toggle_switch('Sadece bulunan yol gözüksün', Screen.mode,
        state_text=('Hayır', 'Evet'), onchange=set_mode)

    menu.add.button('Öğren', start_the_game)
    menu.add.button('Grafik', show_graphic)
    menu.add.button('Kapat', pygame_menu.events.EXIT)