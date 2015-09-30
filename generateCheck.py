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
    clientpkencrypt = fileutil.recupEncrypt('clientPkEncode')
    toCrypt = str(fact.getUid()) + ' ' + str(fact.getTotalSomme())
    crypt = rsatool.encrypt_sk_str(clientsk, toCrypt)
    check = clientpkencrypt + '\n' + str(crypt)
    checkEncrypt = rsatool.encrypt_sk_str(clientsk, toCrypt)
    checkTotal = open(fichierout, 'w')
    checkTotal.write(check + '\n' + str(checkEncrypt))
    checkTotal.close()
    
    
