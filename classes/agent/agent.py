from entities.statistics import Statistics
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
    step_count = 0
    total_q_value = 0

    # MATRİSLERİ, ÖĞRENME KATSAYISINI, BAŞLANGIÇ VE HEDEF KONUMUNU ALIYOR
    def __init__(self, matrix_map, matrix_r, matrix_q, learning_rate, start_point, goal_point):
        self.matrix_map = matrix_map
        self.matrix_r = matrix_r
        self.matrix_q = matrix_q
        self.learning_rate = learning_rate
        self.start_point = start_point
        self.goal_point = goal_point
        self.current_location = start_point
    
    # Q VE R TABLOSUNDAN AJANIN GİTTİĞİ YÖNDEKİ PUANINI HESAPLIYOR
    def calculate_value(self, agent_point, action, move_point, maximum):
        r_value = self.matrix_r[agent_point][action]
        if move_point >= 0 and move_point < maximum:
            q_value = self.learning_rate * max(self.matrix_q[move_point])
        else:
            q_value = -10
            self.path.clear()
        self.total_q_value += r_value + q_value
        return r_value + q_value

    # Q TABLOSUNDAN EN BÜYÜK DEĞERLİ OLAN YÖNÜ SEÇİYOR. EĞER AYNI DEĞERDE 1'DEN FAZLA YÖN VARSA ARALARINDAN RASTGELE SEÇİM YAPIYOR
    def choose_action(self, agent_point):
        max_value = max(self.matrix_q[agent_point])
        same_index = []
        for i in range(len(self.matrix_q[agent_point])):
            if max_value == self.matrix_q[agent_point][i]:
                same_index.append(i)
        return choice(same_index)

    # SEÇİLEN YÖNE GÖRE AJANIN HANGİ KONUMDA OLACAĞINI GERİ DÖNDÜRÜYOR
    def move_point(self, action):
        if action == 0:
            return [self.current_location[0]-1, self.current_location[1], 0]
        elif action == 1:
            return [self.current_location[0]-1, self.current_location[1]+1, 1]
        elif action == 2:
            return [self.current_location[0], self.current_location[1]+1, 2]
        elif action == 3:
            return [self.current_location[0]+1, self.current_location[1]+1, 3]
        elif action == 4:
            return [self.current_location[0]+1, self.current_location[1], 4]
        elif action == 5:
            return [self.current_location[0]+1, self.current_location[1]-1, 5]
        elif action == 6:
            return [self.current_location[0], self.current_location[1]-1, 6]
        elif action == 7:
            return [self.current_location[0]-1, self.current_location[1]-1, 7]
        return

    # AJANIN HAREKETİNİ KONTROL EDİYOR. EĞER HEDEFE ULAŞTIYSA VEYA ENGELE ÇARPTIYSA İLGİLİ İŞLEMLERİ GERÇEKLEŞTİRİYOR.
    def move_agent(self, move_point):
        if self.matrix_map[move_point[0]][move_point[1]] == 100:
            Statistics.add(self.total_q_value,self.step_count + 1)
            self.step_count = 0
            self.total_q_value = 0
            self.path.append(move_point)
            self.finished_path = self.path.copy()
            self.path.clear()
            self.goal_path_count += 1
            self.set_agent_point(self.start_point)

        elif self.matrix_map[move_point[0]][move_point[1]] == 1:
            self.step_count = 0
            self.total_q_value = 0
            self.path.clear()
            self.set_agent_point(self.start_point)
        else:
            self.step_count =  self.step_count + 1
            self.path.append(move_point)
            self.set_agent_point(move_point)

    # AJANIN MATRİS ÜZERİNDEKİ KONUMUNU DEĞİŞTİRİYOR
    def set_agent_point(self, move_point):
        self.current_location = move_point

    # HEDEFE ULAŞMA DURUMUNU KONTROL EDİYOR. EĞER HESAPLANAN DEĞER SAYISI KADAR HEDEFE ULAŞTIYSA ARAMA İŞLEMİNİ BİTİRMEK İÇİN FALSE DÖNDÜRÜYOR
    def goal_control(self):
        if self.goal_path_count >= (len(self.matrix_map[0]) * len(self.matrix_map))/2:
            return False
        return True