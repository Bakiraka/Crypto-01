#!/usr/bin/env python
###################################################################
####    Merchant program taking an invoice and a signed check  ####
####    as a parameter and checking if the client didn't edit  ####
####    the invoice and that the check is correct              ####
####    Arguments : - invoice file                             ####
####                - signed check                             ####
####                - client's public key                      ####
####    Output : Either that the check is fine or not          ####
###################################################################
import sys
import FileUtils
import Facture
import RSAtools

if( len(sys.argv) < 4 ):
    print("You need to put all of the arguments (invoice file, signed check and client's Pk)")
    sys.exit()

# file opening
try:
    invoice_file = open(sys.argv[1], 'r')
    signedcheck_file = open(sys.argv[2], 'r')
    clientkey_file = open(sys.argv[3], 'r')
except (OSError, IOError) as error:
    print("Error reading file : ", error)
    sys.exit()

#Getting the infos from the files
clepub_client = FileUtils.recupKey(sys.argv[3])

facture = Facture(sys.argv[1])

clepub_client_bankciphered = signedcheck_file.readline()
sum_n_id_ciphered = signedcheck_file.readline()

ciphered_check_w_clientpk = ""
for lines in signedcheck_file:
    ciphered_check_w_clientpk += lines

sum_n_id_clear = decrypt_pk_str(clepub_client, sum_n_id_ciphered)
sum_n_id = sum_n_id_clear.split(" ")
if(sum_n_id[0] != facture.getUid()):
    print
if(sum_n_id[1] != facture.getTotalSomme()):
    print
