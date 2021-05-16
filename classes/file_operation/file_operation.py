from os import write
from texttable import Texttable

class File_Operation:
    fileName = ""
    f = any

    def __init__(self) -> None:
        self.fileName = "output.txt"

    def OutputFile(self, mapMatrix,startPoint,targetPoint,lastPath):
        f = open(self.fileName, "w+")
        outputText = ""
        outputText = outputText +"               Harita Bilgileri                   \n"
        outputText = outputText +"--------------------------------------------------\n"
        outputText = outputText +"Duvar             : [K] harfi ile gosterilmektedir\n"
        outputText = outputText +"Yol               : [G] harfi ile gosterilmektedir\n"
        outputText = outputText +"Harita yuksekligi : "+str(len(mapMatrix))+"\n"
        outputText = outputText +"Harita genisligi  : "+str(len(mapMatrix[0]))+"\n"
        outputText = outputText +"Baslangic noktasi : X:"+str(startPoint[0])+" Y:"+str(startPoint[1])+"\n"
        outputText = outputText +"Hedef noktasi     : X:"+str(targetPoint[0])+" Y:"+str(targetPoint[1])+"\n"
        outputText = outputText +"--------------------------------------------------\n"
        for y in range(len(mapMatrix)):
            outputText = outputText+"[ "
            for x in range(len(mapMatrix[y])):
                if mapMatrix[y][x] == 0:
                    outputText = outputText + "("+str(y)+","+str(x)+",G) "
                else:
                    outputText = outputText + "("+str(y)+","+str(x)+",K) "
            outputText = outputText + "],\n"
        outputText = outputText +"--------------------------------------------------\n"
        outputText = outputText + "Bulunan en kisa yol adimlari:\n"
        t = Texttable()
        pathTextArray = [['ADIM SAYISI', 'X','Y']]
        for location in range(len(lastPath)):
            step = str(location+1) + ". adim"
            pathTextArray.append([step,str(lastPath[location][0]),str(lastPath[location][1])])

        t.add_rows(pathTextArray)
        outputText = outputText + t.draw()
        f.write(outputText)
        f.close()
