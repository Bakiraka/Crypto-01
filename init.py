import os
from RSAtools import RSAtools
from fileUtils import FileUtils
# This file generate :
# RSA public and private key for the bank, the commercant and the client
# Crypt of the public key of client by the bank SK, To garantee that the client is in this bank
if __name__ == '__main__' :
    rsa = RSAtools()
    fileUtil = FileUtils()
    # generation des clés RSA
    rsaClient = rsa.generateRSAkey(1024)
    rsaCommercant = rsa.generateRSAkey(1024)
    rsaBanque = rsa.generateRSAkey(1024)

    """n,e,d"""
    # ecriture des clés dans leur fichiers respectifs
    clientpk = open('clientPk','w')
    clientpk.write(str(rsaClient [0])+' '+str(rsaClient [1]))
    clientpk.close()
    clientsk = open('clientSk','w')
    clientsk.write(str(rsaClient [0])+' '+str(rsaClient [2]))
    clientsk.close()
    commercantpk = open('commercantPk','w')
    commercantpk.write(str(rsaCommercant [0])+' '+str(rsaCommercant [1]))
    commercantpk.close()
    commercantsk = open('commercantSk','w')
    commercantsk.write(str(rsaCommercant [0])+' '+str(rsaCommercant [2]))
    commercantsk.close()
    banquepk = open('banquePk','w')
    banquepk.write(str(rsaBanque [0])+' '+str(rsaBanque [1]))
    banquepk.close()
    banquesk = open('banqueSk','w')
    banquesk.write(str(rsaBanque [0])+' '+ str(rsaBanque [2]))
    banquesk.close()
    print([rsaClient [0],rsaClient[1]])
    # Cryptage de la clé publique du client par la clé secrete de la banque
    # Test des fonctions de cryptage et decryptage par bloc
    clientpkencode = rsa.cryptblock(fileUtil.recupKey('banqueSk'), rsaClient [0])
    clientpkdecode = rsa.decryptblock(fileUtil.recupKey('banquePk'), clientpkencode)
    clientpkencode2 = rsa.cryptblock(fileUtil.recupKey('banqueSk'), rsaClient [1])
    clientpkdecode2 = rsa.decryptblock(fileUtil.recupKey('banquePk'), clientpkencode2)
    fileUtil.writeContent(fileUtil.formatKey(clientpkencode) + '\n' + fileUtil.formatKey(clientpkencode2), "clientPkEncode")
    print ([clientpkdecode,clientpkdecode2])


    
