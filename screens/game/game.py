from entities.screen import Screen
from classes.agent.agent_on_screen import Agent_On_Screen
from classes.file_operation.file_operation import File_Operation
from pygame.locals import *
import pygame

class Game:
    def __init__(self, maze, window_width, window_height, agent_x_y):
        self._window_width = window_width
        self._window_height = window_height
        self._running = True
        self._display_surf = None
        self._agent_surf = None
        self._agent = Agent_On_Screen(agent_x_y)

        self._block_surf = None
        self._goal_surf = None
        self._trace_surf = None
        self.maze = maze
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self._window_width,self._window_height), pygame.HWSURFACE)
        pygame.display.set_caption('Q-Learning')
        self._running = True

        self._trace_surf = pygame.image.load('./images/trace.png')
        self._agent_surf = pygame.image.load("./images/agent.png")
        self._block_surf = pygame.image.load("./images/block.png")
        self._goal_surf = pygame.image.load("./images/goal.png")

        self._trace_surf = pygame.transform.scale(self._trace_surf, (Screen.square_size, Screen.square_size))
        self._agent_surf = pygame.transform.scale(self._agent_surf, (Screen.square_size, Screen.square_size))
        self._block_surf = pygame.transform.scale(self._block_surf, (Screen.square_size, Screen.square_size))
        self._goal_surf = pygame.transform.scale(self._goal_surf, (Screen.square_size, Screen.square_size))
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render_finished(self, my_agent, my_matrix):
        self._display_surf.fill((20,20,20))
        self.maze.draw(self._display_surf, self._block_surf, self._goal_surf, my_agent.goal_point)
        self._display_surf.blit(self._agent_surf,(self._agent.point[0], self._agent.point[1]))

        if my_agent:
            self._display_surf.blit(self._trace_surf,(my_agent.start_point[1]*Screen.square_size, my_agent.start_point[0]*Screen.square_size))
            for i in my_agent.finished_path:
                self._display_surf.blit(self._trace_surf,(i[1]*Screen.square_size, i[0]*Screen.square_size))
            self._display_surf.blit(self._agent_surf,(i[1]*Screen.square_size, i[0]*Screen.square_size))
            
        pygame.display.flip()

        fo = File_Operation()
        fo.OutputFile(my_matrix.matrix_map, my_agent.start_point, my_agent.goal_point, my_agent.finished_path)
    
    def on_render(self, my_agent):
        self._display_surf.fill((20,20,20))
        self.maze.draw(self._display_surf, self._block_surf, self._goal_surf, my_agent.goal_point)
        self._display_surf.blit(self._agent_surf,(self._agent.point[0], self._agent.point[1]))

        if my_agent:
            self._display_surf.blit(self._agent_surf,(my_agent.start_point[1]*Screen.square_size, my_agent.start_point[0]*Screen.square_size))
            for i in my_agent.path:
                self._display_surf.blit(self._trace_surf,(i[1]*Screen.square_size, i[0]*Screen.square_size))
        pygame.display.flip()
 
    def on_cleanup(self):
        Screen.reset_window_size()
        pygame.display.set_mode((Screen.window_width, Screen.window_height))
        self._running = False

    def on_execute(self, my_agent, my_matrix):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            while(my_agent.goal_control()):
                agent_point = my_matrix.get_sequence(my_agent.current_location)
                action = my_agent.choose_action(agent_point)
                move_point = my_agent.move_point(action)
                calculate_value = my_agent.calculate_value(agent_point, action, my_matrix.get_sequence(move_point), my_matrix.row*my_matrix.column)
                my_matrix.update_matrix_q(calculate_value, [agent_point, action])
                
                if Screen.mode == False:
                    self.on_render(my_agent)

                if(my_matrix.location_control(move_point)):
                    my_agent.move_agent(move_point)
                else:
                    my_agent.set_agent_point(my_agent.start_point)

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render_finished(my_agent, my_matrix)
        self.on_cleanup()