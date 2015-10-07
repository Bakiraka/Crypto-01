#!/usr/bin/env python
###################################################################
####    Bank program taking a check verified by the merchant   ####
####    as a parameter and checking if the check hasn't already####
####    been cashed before                                     ####
####    Arguments : - check file                               ####
####                - client's public key                      ####
####                - merchant's public key                    ####
####    Output : Either that the check is fine or not          ####
####    How does a bank check if a check has been cashed       ####
####        or not ?                                           ####
####    - Save a file with the 40 first number of each         ####
####       merchant's key it encounters                        ####
####     -> inside the file, puts on each line, the unique     ####
####      number the merchant has produced and the customer's  ####
####      key, separated by a space                            ####
####    If it's fine, the bank with cash the check and add     ####
####        the line to the right file                         ####
###################################################################
from fileUtils import FileUtils
from RSAtools import RSAtools
import os.path
import sys

fileutils = FileUtils()
rsatools = RSAtools()
#Making sure the arguments and the files are there
clientkey_file = open(sys.argv[2], 'r')
merchantkey_file = open(sys.argv[3], 'r')

#Getting client's key and merchant's original key
clientkey_original = fileutils.recupKey(sys.argv[2])
merchant_key_original = fileutils.recupKey(sys.argv[3])

#Getting client's key ciphered by the bank and bank's private key
clientkeybanqueciphered = []
clientkeybanqueciphered.append(fileutils.readKey(sys.argv[1],2))
clientkeybanqueciphered.append(fileutils.readKey(sys.argv[1],3))

bank_publickey = fileutils.recupKey('banquePk')
#Deciphering the client's key
clientkey_deciphered = [rsatools.decryptblock(bank_publickey, clientkeybanqueciphered[0]), rsatools.decryptblock(bank_publickey, clientkeybanqueciphered[1])]

#Verification
if( clientkey_deciphered != clientkey_original):
    print("La clé du client dans le chèque n'est pas la même que celle fournie !\n")


#Getting merchant's key ciphered by the client and deciphering it
merchantkeyclientciphered = []
merchantkeyclientciphered.append( fileutils.readKey(sys.argv[1],0))
merchantkeyclientciphered.append( fileutils.readKey(sys.argv[1],1))
merchant_key_deciphered = [rsatools.decryptblock( clientkey_deciphered, merchantkeyclientciphered[0]), rsatools.decryptblock( clientkey_deciphered, merchantkeyclientciphered[1])]

if( merchant_key_deciphered != merchant_key_original):
    print("La clé du marchant dans le chèque n'est pas la même que celle fournie !\n")

#Getting the ciphered uid and sum from the check and deciphering it
uidciphered = fileutils.readKey(sys.argv[1],4)
uiddeciphered = rsatools.decryptblock(clientkey_deciphered,uidciphered)

saved_idandkey = []
somethingswrong = False
####Making sure the check hasn't already been cashed
#Verifying if we already have or not a file with the merchant's 40 first key characters
mercfirstchar = str(merchant_key_deciphered [0]) [:40]
if(os.path.isfile(mercfirstchar + ".sv")):
    #openning the file and checking if the id/client's key couple isn't there already
    with open(mercfirstchar + ".sv", 'r') as merchant_historyfile:
        for line in merchant_historyfile:
            if(int(line) == uiddeciphered):
                print("Le couple identifiant unique/clée de client dans ce chèque est reconnu comme déjà ayant été encaissé !")
                somethingswrong = True

if(somethingswrong == False):
    filetowrite = open(mercfirstchar + ".sv", 'a')
    filetowrite.write(str(uiddeciphered) + "\n")
    filetowrite.close()
    print("ok !\n")
