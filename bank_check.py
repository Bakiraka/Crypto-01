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

checkfile_specified = False
if( len(sys.argv) >= 5):
    checkfile_specified = True

#file opening
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
