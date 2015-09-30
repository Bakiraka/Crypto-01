#!/usr/bin/env python
###################################################################
####    Merchant program taking an invoice and a signed check  ####
####    as a parameter and checking if the client didn't edit  ####
####    the invoice and that the check is correct              ####
####    Arguments : - invoice file                             ####
####                - signed check                             ####
####                - client's public key                      ####
####                - merchant's public key                    ####
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
    merchant_key = open(sys.argv[4], 'r')
except (OSError, IOError) as error:
    print("Error reading file : ", error)
    sys.exit()

#Getting the infos from the files
clepub_client = FileUtils.recupKey(sys.argv[3])
facture = Facture(sys.argv[1])
clepub_merchant = FileUtils.recupKey(sys.argv[4])

#Lecture du chèque
clepub_merchant_clientciphered = signedcheck_file.readline()
clepub_client_bankciphered = signedcheck_file.readline()
sum_n_id_ciphered = signedcheck_file.readline()
ciphered_check_w_clientpk = ""
for lines in signedcheck_file:
    ciphered_check_w_clientpk += lines

#Decyphering the cypher of the sum and of the id by the client
sum_n_id_clear = decrypt_pk_str(clepub_client, sum_n_id_ciphered)
sum_n_id = sum_n_id_clear.split(" ")
#Checking if they are the same than the one on the invoice
if(sum_n_id[0] != facture.getUid()):
    print("Elements différents lors de la vérification (UID de la facture)")
if(sum_n_id[1] != facture.getTotalSomme()):
    print("Elements différents lors de la vérification (Somme totale de la facture)")

#checking if the merchant's public key ciphered by the client is right
if(RSAtools.decrypt(clepub_client, clepub_merchant_clientciphered) != clepub_merchant)
    print("Elements différents lors de la vérification (clée du marchant chiffrée par le client)")
