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
        
