from entities.screen import Screen

class Maze:
    def __init__(self, mapMatrix ,row, column) -> None:
        self._row = row
        self._column = column
        self._maze = mapMatrix
    
    def draw(self, displaySurf, imageSurf, goalSurf, goalPoint):
        for i in range(self._row):
            for j in range(self._column):
                if self._maze[i][j] == 1:
                    displaySurf.blit(imageSurf,( j * Screen.square_size , i * Screen.square_size))
                elif self._maze[i][j] == 100:
                    displaySurf.blit(goalSurf,(goalPoint[1]*Screen.square_size, goalPoint[0]*Screen.square_size))