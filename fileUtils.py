import os
class FileUtils :
    def __init__(self):
        pass
    ''' recupere les clés RSA de leur fichier '''
    def recupKey (self, fichier):
        return list(map(int,self.recupLine(fichier).split()))

    ''' recupere un seul crypté '''
    def recupEncrypt(self, fichier) :
        return self.recupLine(fichier)

    ''' recupere la premiere ligne d'un fichier '''
    def recupLine (self, fichier):
        fileLine = open(fichier, 'r')
        line = fileLine.read()
        fileLine.close()
        return line

    ''' prend en parametre une clé, et le formatte dans le format a mettre dans un fichier '''
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

    ''' écrit une chaine de caractere dans un fichier '''
    def writeContent(self, string, fichier) :
        fileWrite = open(fichier,'w')
        fileWrite.write(string)
        fileWrite.close()

    ''' lit le neme crypté du fichier et le met dans le format nécessaire pour être décrypté '''
    def readKey (self, fichier, number):
        i = 0
        tmp = []
        fileRead = open(fichier,'r')
        nb = 0
        tmp2 = 0
        ''' on lit toute les lignes '''
        for j in fileRead:
            ''' si il s'agit d'un début d'encrypt, on stocke le nombre de ligne de celui ci'''
            if nb == 0 :
                tmp.clear()
                nb = int(j)
    #        sinon, on le stocke dans notre liste
            else :
                tmp.append(int(j))
    #         si on arrive a la fin de la clé, si c'est la clé qu'on veut on stop, sinon on remet a zero les compteurs et on incremente le compteur de clé
            if tmp2 == nb - 1 :
                if i == number :
                    break
                i = i + 1
                tmp2 = 0
                nb = 0
            tmp2 = tmp2 + 1
        ''' fermeture du fichier '''
        fileRead.close()
        return tmp
