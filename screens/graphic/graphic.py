import matplotlib.pyplot as plt
from entities.statistic import Statistics

class Graphic:
    def draw_graphic():
        print(Statistics.X)
        print(Statistics.Gains)
        plt.title("Grafik Adı")
        plt.plot(Statistics.X, Statistics.Gains, label="Kazanç")
        plt.plot(Statistics.X, Statistics.Steps, label="Adım Sayısı")
        plt.legend()
        plt.show()