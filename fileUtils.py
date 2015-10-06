import os
class FileUtils :
    def __init__(self):
        pass
    
    def recupKey (self, fichier):
        return list(map(int,self.recupLine(fichier).split()))
        
    
    def recupEncrypt(self, fichier) :
        return self.recupLine(fichier)
    
    def recupLine (self, fichier):
        fileLine = open(fichier, 'r')
        line = fileLine.read()
        fileLine.close()
        return line

    def formatKey (self, key) :
        accu = ''
        accu = str(len(key)) + '\n'
        tmp = 0
        for i in key :
            accu += str(i) 
            if tmp < len(key) - 1 :
                accu += '\n'
            tmp = tmp + 1
        return accu
    
    def writeContent(self, string, fichier) :
        fileWrite = open(fichier,'w')
        fileWrite.write(string)
        fileWrite.close()
        
    def readKey (self, fichier, number):
        i = 0
        tmp = []
        fileRead = open(fichier,'r')
        nb = 0
        tmp2 = 0
        for j in fileRead:
            if nb == 0 :
                tmp.clear()
                nb = int(j)
            else :
                tmp.append(int(j))
            if tmp2 == nb - 1 :
                if i == number :
                    break
                i = i + 1
                tmp2 = 0
                nb = 0
            tmp2 = tmp2 + 1
        fileRead.close()
        return tmp
        
        
