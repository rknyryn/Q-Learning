import random

class Matrix:
    row = 10
    column = 10
    goal_point = [0,0]
    start_point = [0,0]
    matrix_map = []
    matrix_r = []
    matrix_q = []
    hurdle_rate = 7

    goal_puan = 100
    way_puan = -0.01
    wall_puan = -5

    def __init__(self, row, column, start_point, goal_point, hurdle_rate):
        self.row = row
        self.column = column
        self.goal_point = goal_point
        self.start_point = start_point
        self.hurdle_rate = hurdle_rate

        self.create_matrix()
        self.fill_matrix_r_q()
        self.fill_matrix_r()
    
    #MATRİS DOLDURMA FONKSİYONLARI
    def create_matrix(self):
        for i in range(self.row):
            temp = []
            for j in range(self.column):
                x = random.randint(0,10)
                if x < self.hurdle_rate:
                    temp.append(1)
                else:
                    temp.append(0)
            self.matrix_map.append(temp)
        self.matrix_map[self.start_point[0]][self.start_point[1]] = 0
        self.matrix_map[self.goal_point[0]][self.goal_point[1]] = 100
    
    def fill_matrix_r_q(self):
        for i in range(self.row * self.column):
            a = []
            b = []
            for j in range(8):
                a.append(-10)
                b.append(0)
            self.matrix_r.append(a)
            self.matrix_q.append(b)

    def fill_matrix_r(self):
        r_count = 0
        for i in range(self.row):
            for j in range(self.column):
                self.controls(i, j, r_count)
                r_count = r_count + 1

    def update_matrix_q(self, calculated_value, update_point):
        self.matrix_q[update_point[0]][update_point[1]] = calculated_value
        return
    
    #MAP MATRİSTEKİ DEĞERİN R ve Q MATRİSİNDEKİ KAÇINCI SIRADA OLDUĞUNU DÖNDÜREN FONKSİYON
    def get_sequence(self, location):
        return (location[0]*self.column) + location[1]

    #R TABLOSU İÇİN KONTROLLER
    def controls(self, x, y, r):
        self.control_up(x, y, r)
        self.control_up_right(x, y, r)
        self.control_right(x, y, r)
        self.control_right_down(x, y, r)
        self.control_down(x, y, r)
        self.control_down_left(x, y, r)
        self.control_left(x, y, r)
        self.control_left_up(x, y, r)

    def control_up(self, x, y, r):
        if(x-1 >= 0):
            if(x-1 == self.goal_point[0] and y ==self.goal_point[1]):
                self.matrix_r[r][0] = self.goal_puan
            elif(self.matrix_map[x-1][y] == 0):
                self.matrix_r[r][0] = self.way_puan
            else:
                self.matrix_r[r][0] = self.wall_puan

    def control_up_right(self, x, y, r):
        if(x-1 >= 0 and y+1 <= self.row -1):
            if(x-1 == self.goal_point[0] and y+1 ==self.goal_point[1]):
                self.matrix_r[r][1] = self.goal_puan
            elif(self.matrix_map[x-1][y+1] == 0):
                self.matrix_r[r][1] = self.way_puan
            else:
                self.matrix_r[r][1] = self.wall_puan

    def control_right(self, x, y, r):
        if(y+1 <= self.column-1):
            if(x == self.goal_point[0] and y+1 ==self.goal_point[1]):
                self.matrix_r[r][2] = self.goal_puan
            elif(self.matrix_map[x][y+1] == 0):
                self.matrix_r[r][2] = self.way_puan
            else:
                self.matrix_r[r][2] = self.wall_puan

    def control_right_down(self, x, y, r):
        if(y+1 <= self.column -1 and x+1 <= self.row -1):
            if(x+1 == self.goal_point[0] and y+1 ==self.goal_point[1]):
                self.matrix_r[r][3] = self.goal_puan
            elif(self.matrix_map[x+1][y+1] == 0):
                self.matrix_r[r][3] = self.way_puan
            else:
                self.matrix_r[r][3] = self.wall_puan

    def control_down(self, x, y, r):
        if(x+1 <= self.row -1):
            if(x+1 == self.goal_point[0] and y ==self.goal_point[1]):
                self.matrix_r[r][4] = self.goal_puan
            elif(self.matrix_map[x+1][y] == 0):
                self.matrix_r[r][4] = self.way_puan
            else:
                self.matrix_r[r][4] = self.wall_puan
    
    def control_down_left(self, x, y, r):
        if(x+1 <= self.row -1 and y-1 >= 0):
            if(x+1 == self.goal_point[0] and y-1 ==self.goal_point[1]):
                self.matrix_r[r][5] = self.goal_puan
            elif(self.matrix_map[x+1][y-1] == 0):
                self.matrix_r[r][5] = self.way_puan
            else:
                self.matrix_r[r][5] = self.wall_puan

    def control_left(self, x, y, r):
        if(y-1 >= 0):
            if(x == self.goal_point[0] and y-1 ==self.goal_point[1]):
                self.matrix_r[r][6] = self.goal_puan
            elif(self.matrix_map[x][y-1] == 0):
                self.matrix_r[r][6] = self.way_puan
            else:
                self.matrix_r[r][6] = self.wall_puan

    def control_left_up(self, x, y, r):
        if(x-1 >= 0 and y-1 >= 0):
            if(x-1 == self.goal_point[0] and y-1 ==self.goal_point[1]):
                self.matrix_r[r][7] = self.goal_puan
            elif(self.matrix_map[x-1][y-1] == 0):
                self.matrix_r[r][7] = self.way_puan
            else:
                self.matrix_r[r][7] = self.wall_puan

    #AJANIN BULUNDUĞU KONUM OYUN ALANI İÇERİSİNDE Mİ KONTROLÜ
    def location_control(self, movePoint):
        if(movePoint[0] >= 0 and movePoint[0] <= self.row -1):
            if(movePoint[1] >= 0 and movePoint[1] <= self.column -1):
                return True
            return False
        return False

    def reset_matrix(self):
        self.matrix_q.clear()
        self.matrix_r.clear()
        self.matrix_map.clear()

        self.create_matrix()
        self.fill_matrix_r_q()
        self.fill_matrix_r()