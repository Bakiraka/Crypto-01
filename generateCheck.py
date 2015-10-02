import sys
from facture import Facture
from fileUtils import FileUtils
from RSAtools import RSAtools
if __name__ == '__main__' :
    fichier = sys.argv [1]
    fichierout = sys.argv [2]
    fact = Facture(fichier)
    rsatool = RSAtools()
    print(fact.toString())
    fileutil = FileUtils()
    clientsk = fileutil.recupKey('clientSk')
    commercantpk = fileutil.recupKey('commercantPk')
    clientpkencrypt = fileutil.recupKey('clientPkEncode')
    commercantpk1 = rsatool.decrypt(clientsk, commercantpk[0])
    commercantpk2 = rsatool.decrypt(clientsk, commercantpk[1])
    cryptUid = rsatool.decrypt(clientsk, fact.getUid())
    cryptSum = rsatool.decrypt(clientsk, fact.getTotalSomme())
    checkTotal = open(fichierout, 'w')
    checkTotal.write(str(clientpkencrypt [0]) + '\n' + str(clientpkencrypt [1]) + '\n')
    checkTotal.write(str(commercantpk1) + '\n' + str(commercantpk2) + '\n')
    checkTotal.write(str(cryptUid) + '\n' + str(cryptSum))
    checkTotal.close()
    
    
