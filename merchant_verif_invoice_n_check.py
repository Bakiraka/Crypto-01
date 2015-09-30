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

if( len(sys.argv) < 4 ):
    print("You need to put all of the arguments (invoice file, signed check and client's Pk)")
    sys.exit()

# file opening
try:
    invoice_file = open(sys.argv[1], 'r')
    invoice_file = open(sys.argv[2], 'r')
    invoice_file = open(sys.argv[3], 'r')
except (OSError, IOError) as error:
    print("Error reading file : ", error)
    sys.exit()
