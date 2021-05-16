import matplotlib.pyplot as plt
from entities.statistics import Statistics

class Graphic:
    def draw_graphic():
        #kazançların/maliyetin(episode via cost) ve bölüm adım sayısının (episode via step) 
        plt.figure("Kazanç ve Adım Sayısı")
        plt.title("Kazanç ve Adım Sayısı")
        plt.plot(Statistics.X, Statistics.Gains, label="Kazanç")
        plt.plot(Statistics.X, Statistics.Steps, label="Adım Sayısı")
        plt.xlabel("Hedefe ulaşan yol sayısı")
        plt.ylabel("Kazanç miktarı ve hedefe ulaştığı adım sayısı")
        plt.legend()
        plt.show()
        