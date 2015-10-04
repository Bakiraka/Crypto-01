#!/usr/bin/env python
###################################################################
####    Bank program taking a check verified by the merchant   ####
####    as a parameter and checking if the check hasn't already####
####    been cashed before                                     ####
####    Arguments : - check file                               ####
####                - client's public key                      ####
####                - merchant's public key                    ####
####                - (optional) file that the bank uses to    ####
####                    verify checks                          ####
####    Output : Either that the check is fine or not          ####
###################################################################
import FileUtils
import RSAtools

#Checking the number of arguments for the optional file
checkfile_specified = False
if( len(sys.argv) >= 5):
    checkfile_specified = True

#Making sure the arguments and the files are there
try:
    check_file = open(sys.argv[1], 'r')
    clientkey_file = open(sys.argv[2], 'r')
    merchantkey_file = open(sys.argv[3], 'r')
    if( checkfile_specified):
        checkfile = open(sys.argv[4], 'r')
    else:
        checkfile = open("checkfile", 'r')
except (OSError, IOError) as error:
    print("Error reading file : ", error)
    sys.exit()
finally:
    checkfile.close()
    clientkey_file.close()
    merchantkey_file.close()

#Getting client's key and merchant's original key
clientkey_original = FileUtils.recupKey(sys.argv[2])
merchant_key_original = FileUtils.recupKey(sys.argv[3])
#Getting merchant's key ciphered by the client
merchant_key_ciphered = check_file.readline()
#Deciphering
merchant_key_deciphered = RSAtools.decrypt( clientkey_original, merchant_key_ciphered)
#Verification
if( merchant_key_deciphered != merchant_key_original):
    print("La clé du marchant dans le chèque n'est pas la même que celle fournie !\n")

#Getting client's key ciphered by the bank
clientkey_ciphered = checkfile.readline()
#Getting the bank's private key
bank_privatekey = FileUtils.recupKey('bankPk')
#Deciphering the client's key
clientkey_deciphered = RSAtools.decrypt( bank_privatekey, clientkey_ciphered)
#Verification
if( clientkey_deciphered != clientkey_original):
    print("La clé du client dans le chèque n'est pas la même que celle fournie !\n")

#Getting the ciphered uid and sum from the check
uidciphered = checkfile.readline()
sumciphered = checkfile.readline()

#Making sure the check hasn't already been cashed
