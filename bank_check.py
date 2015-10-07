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
import FileUtils
import RSAtools
import os.path

#Making sure the arguments and the files are there
try:
    check_file = open(sys.argv[1], 'r')
    clientkey_file = open(sys.argv[2], 'r')
    merchantkey_file = open(sys.argv[3], 'r')
finally:
    clientkey_file.close()
    merchantkey_file.close()

#Getting client's key and merchant's original key
clientkey_original = FileUtils.recupKey(sys.argv[2])
merchant_key_original = FileUtils.recupKey(sys.argv[3])
#Getting merchant's key ciphered by the client and deciphering it
merchant_key_ciphered = check_file.readline()
merchant_key_deciphered = RSAtools.decrypt( clientkey_original, merchant_key_ciphered)

if( merchant_key_deciphered != merchant_key_original):
    print("La clé du marchant dans le chèque n'est pas la même que celle fournie !\n")

#Getting client's key ciphered by the bank and bank's private key
clientkey_ciphered = check_file.readline()
bank_privatekey = FileUtils.recupKey('bankPk')
#Deciphering the client's key
clientkey_deciphered = RSAtools.decrypt( bank_privatekey, clientkey_ciphered)
#Verification
if( clientkey_deciphered != clientkey_original):
    print("La clé du client dans le chèque n'est pas la même que celle fournie !\n")

#Getting the ciphered uid and sum from the check and deciphering it
uidciphered = check_file.readline()
uiddeciphered = RSAtools.decrypt(clientkey_deciphered,uidciphered)

saved_idandkey = []
somethingswrong = False
####Making sure the check hasn't already been cashed
#Verifying if we already have or not a file with the merchant's 40 first key characters
mercfirstchar = merchant_key_deciphered[:40]
if(os.path.isfile(mercfirstchar))
    #openning the file and checking if the id/client's key couple isn't there already
    with open(mercfirstchar, 'r') as merchant_historyfile:
    for line in merchant_historyfile:
        saved_idandkey = line.split(" ", 2)
        if(saved_idandkey[0] == uiddeciphered && saved_idandkey[1] == clientkey_original):
            print("Le couple identifiant unique/clée de client dans ce chèque est reconnu comme déjà ayant été encaissé !")
            somethingswrong = True

if(somethingswrong == False):
    filetowrite = open(mercfirstchar, 'a')
    filetowrite.write(uidciphered + " " + clientkey_original + "\n")
    filetowrite.close()
