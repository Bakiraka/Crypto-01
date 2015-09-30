import os
class Facture :
    uid = 0
    liste = []
    sommetotale = 0
    def __init__(self, fichier) :
        global uid
        global liste
        global sommetotale
        uid = 0
        liste = []
        sommetotale = 0
        cmp = 0
        lastline = ''
        fichierlecture = open(fichier, "r")
        for line in fichierlecture :
            lastline = line
            if cmp == 0 :
                uid = int(line)
            else :
                liste.append(line)
            cmp += 1
        liste.remove(lastline)
        sommetotale = int(lastline)

    def toString(self) :
        accu = str(uid) + '\n'
        for l in liste :
            accu = accu + l
        accu = accu + str(sommetotale)
        return accu
    def getUid(self) :
        return uid
    def getElements (self) :
        return liste
    def getTotalSomme (self) :
        return sommetotale
        
