import sys
from facture import Facture
from fileUtils import FileUtils
from RSAtools import RSAtools
if __name__ == '__main__' :
    ''' recupération des deux parametres'''
    fichier = sys.argv [1]
    fichierout = sys.argv [2]
    fact = Facture(fichier)
    rsatool = RSAtools()
    print(fact.toString())
    fileutil = FileUtils()
    ''' recuperation des clés RSA'''
    clientsk = fileutil.recupKey('clientSk')
    commercantpk = fileutil.recupKey('commercantPk')
    clientpkencrypt = fileutil.readKey('clientPkEncode',0)
    clientpkencrypt2 = fileutil.readKey('clientPkEncode',1)
    '''crypt de la clé publique du commercant par le client'''
    commercantpk1 = rsatool.cryptblock(clientsk, commercantpk[0])
    commercantpk2 = rsatool.cryptblock(clientsk, commercantpk[1])
    ''' crypt des informations de la facture par le client'''
    cryptUid = rsatool.cryptblock(clientsk, fact.getUid())
    cryptSum = rsatool.cryptblock(clientsk, fact.getTotalSomme())
    checkTotal = open(fichierout, 'w')
    ''' stockage des informations de la forme :
          1) la clé publique du client cryptée par la banque
          2) la clé publique du commercant cryptée par le client
          3) le crypté de L'Uid et le Montant de la facture
    '''
    checkTotal.write(fileutil.formatKey(clientpkencrypt) + '\n' + fileutil.formatKey(clientpkencrypt2) + '\n')
    checkTotal.write(fileutil.formatKey(commercantpk1) + '\n' + fileutil.formatKey(commercantpk2) + '\n')
    checkTotal.write(fileutil.formatKey(cryptUid) + '\n' + fileutil.formatKey(cryptSum))
    checkTotal.close()
    
    
