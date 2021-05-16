class Statistics:
    X = []
    Gains = []
    Steps = []

    def add(gain,step):
        Statistics.Gains.append(gain)
        Statistics.Steps.append(step)
        Statistics.X.append(len(Statistics.X) + 1)