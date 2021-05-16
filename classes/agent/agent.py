from random import choice

class Agent:
    start_point = [0,0]
    goal_point= [0,0]
    current_location= [0,0]
    direction = 0
    learning_rate = 0.8
    # actionList = ["up", "up-right" "right", "right-down", "down", "down-left", "left", "left-up"]

    matrix_map = []
    matrix_r = []
    matrix_q = []
    path = []
    finished_path = []
    goal_path_count = 0

    def __init__(self, matrix_map, matrix_r, matrix_q, learning_rate, start_point, goal_point):
        self.matrix_map = matrix_map
        self.matrix_r = matrix_r
        self.matrix_q = matrix_q
        self.learning_rate = learning_rate
        self.start_point = start_point
        self.goal_point = goal_point
        self.current_location = start_point
        
    def calculate_value(self, agent_point, action, move_point, maximum):
        r_value = self.matrix_r[agent_point][action]
        if move_point >= 0 and move_point < maximum:
            q_value = self.learning_rate * max(self.matrix_q[move_point])
        else:
            q_value = -10
            self.path.clear()
        return r_value + q_value

    def choose_action(self, agent_point):
        max_value = max(self.matrix_q[agent_point])
        same_index = []
        for i in range(len(self.matrix_q[agent_point])):
            if max_value == self.matrix_q[agent_point][i]:
                same_index.append(i)
        return choice(same_index)

    def move_point(self, action):
        if action == 0:
            return [self.current_location[0]-1, self.current_location[1]]
        elif action == 1:
            return [self.current_location[0]-1, self.current_location[1]+1]
        elif action == 2:
            return [self.current_location[0], self.current_location[1]+1]
        elif action == 3:
            return [self.current_location[0]+1, self.current_location[1]+1]
        elif action == 4:
            return [self.current_location[0]+1, self.current_location[1]]
        elif action == 5:
            return [self.current_location[0]+1, self.current_location[1]-1]
        elif action == 6:
            return [self.current_location[0], self.current_location[1]-1]
        elif action == 7:
            return [self.current_location[0]-1, self.current_location[1]-1]
        return

    def move_agent(self, move_point):
        if self.matrix_map[move_point[0]][move_point[1]] == 100:
            self.path.append(self.goal_point)
            self.finished_path = self.path.copy()
            self.path.clear()
            self.goal_path_count += 1
            self.set_agent_point(self.start_point)

        elif self.matrix_map[move_point[0]][move_point[1]] == 1:
            self.path.clear()
            self.set_agent_point(self.start_point)
        else:
            self.path.append(move_point)
            self.set_agent_point(move_point)

    def set_agent_point(self, move_point):
        self.current_location = move_point

    def goal_control(self):
        if self.goal_path_count >= (len(self.matrix_map[0]) * len(self.matrix_map))/2:
            return False
        return True