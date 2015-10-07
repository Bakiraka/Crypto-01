#!/usr/bin/env python
###################################################################
####    Merchant program taking an invoice and a signed check  ####
####    as a parameter and checking if the client didn't edit  ####
####    the invoice and that the check is correct              ####
####    Arguments : - invoice file                             ####
####                - signed check                             ####
####    Output : Either that the check is fine or not          ####
###################################################################
import sys
from facture import Facture
from fileUtils import FileUtils
from RSAtools import RSAtools

if( len(sys.argv) < 4 ):
    print("You need to put all of the arguments (invoice file, signed check and client's Pk)")
    sys.exit()

# file opening
try:
    invoice_file = open(sys.argv[1], 'r')
    signedcheck_file = open(sys.argv[2], 'r')
except (OSError, IOError) as error:
    print("Error reading file : ", error)
    sys.exit()
fileutils = FileUtils()
rsatools = RSAtools()

#Getting the infos from the files
clepub_client = fileutils.recupKey(sys.argv[3])
facture = Facture(sys.argv[1])
clepub_merchant_original = fileutils.recupKey("commercantPk")

bankPk = fileutils.recupKey("banquePk")

merchantkeyclientciphered = []
clientkeybanqueciphered = []

merchantkeyclientciphered.append( fileutils.readKey(sys.argv[2],0))
merchantkeyclientciphered.append( fileutils.readKey(sys.argv[2],1))

clientkeybanqueciphered.append(fileutils.readKey(sys.argv[2],2))
clientkeybanqueciphered.append(fileutils.readKey(sys.argv[2],3))

uid_ciphered = fileutils.readKey(sys.argv[2],4)
sum_ciphered = fileutils.readKey(sys.argv[2],5)
'''
print("######################################")
print(clientkeybanqueciphered)
print("######################################")
'''
clepub_client = [rsatools.decryptblock(bankPk, clientkeybanqueciphered[0]), rsatools.decryptblock(bankPk, clientkeybanqueciphered[1])]
clepub_merchant = [rsatools.decryptblock( clepub_client, merchantkeyclientciphered[0]), rsatools.decryptblock( clepub_client, merchantkeyclientciphered[1])]

#Decyphering the cypher of the sum and of the id by the client
uid_clear = rsatools.decryptblock(clepub_client, uid_ciphered)
sum_clear = rsatools.decryptblock(clepub_client, sum_ciphered)

#Checking if they are the same than the one on the invoice
if(uid_clear != facture.getUid()):
    print("Elements différents lors de la vérification (UID de la facture)")
if(sum_clear != facture.getTotalSomme()):
    print("Elements différents lors de la vérification (Somme totale de la facture)")
#checking if the merchant's public key ciphered by the client is right
if(clepub_merchant != clepub_merchant_original):
    print("Elements différents lors de la vérification (clée du marchant chiffrée par le client)")
