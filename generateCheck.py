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
    clientpkencrypt = fileutil.readKey('clientPkEncode',0)
    clientpkencrypt2 = fileutil.readKey('clientPkEncode',1)
    commercantpk1 = rsatool.cryptblock(clientsk, commercantpk[0])
    commercantpk2 = rsatool.cryptblock(clientsk, commercantpk[1])
    cryptUid = rsatool.decrypt(clientsk, fact.getUid())
    cryptSum = rsatool.decrypt(clientsk, fact.getTotalSomme())
    checkTotal = open(fichierout, 'w')
    checkTotal.write(str(clientpkencrypt) + '\n' + str(clientpkencrypt2) + '\n')
    checkTotal.write(fileutil.formatKey(commercantpk1) + '\n' + fileutil.formatKey(commercantpk2) + '\n')
    checkTotal.write(str(cryptUid) + '\n' + str(cryptSum))
    checkTotal.close()
    
    
