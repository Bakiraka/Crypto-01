#!/usr/bin/env python
###################################################################
####    Merchant program generating and invoice                ####
####    Arguments : Name of the invoice                        ####
####                invoice_sum in the invoice                 ####
####                (optional) Number of products              ####
####    Output : Invoice generated                             ####
####    The invoice will be of the form :                      ####
####    unique id                                              ####
####    product1 price1 quantityofproduct1                     ####
####    product2 price2 quantityofproduct1                     ####
####    invoice_sum                                            ####
###################################################################
import merchant_tools
import random
import sys

#checking the arguments
if( len(sys.argv) < 3 ):
    print("Not enough arguments provided, exiting...")
    sys.exit()
else:
    if( len(sys.argv) == 4):
        #Number of products generated
        try:
            invoice_nbrof_products = int(sys.argv[3])
        except (ValueError):
            print("Number of products given in parameter is wrong !")
            sys.exit()
        if(invoice_nbrof_products < 1):
            print("Number of products given in parameter is wrong !")
            sys.exit()
    else:
        #We'll generate up to 5 products
        invoice_nbrof_products = random.randrange(1, 6)
    nameofinvoice = sys.argv[1]
    invoice_sum = int(sys.argv[2])

if(int(invoice_nbrof_products) > invoice_sum):
    print("Can't create an invoice of " + str(invoice_nbrof_products) + " products with a total sum of " + str(invoice_sum))
    print("\nExiting...")
    sys.exit()

#Guid generation
unique_number = str(merchant_tools.randomnumber())
while(merchant_tools.check_uid_exist(unique_number)):
    unique_number = str(merchant_tools.randomnumber())
merchant_tools.save_unique_id(unique_number)
#unique_number = guid_generation.generate_uuid()

print("Generating " + str(invoice_nbrof_products))
#Products generation
products_list = []
invoice_rest = invoice_sum
i = invoice_nbrof_products
while i > 0:
    product_number = random.randrange(0, 100)
    product_name = "Product" + str(product_number)
    #Price generation (kindof random, depending on product name, but always the same)
    #random.seed(product_number)
    try:
        if(i == 1):
            product_cost = invoice_rest
        elif(i == invoice_rest):
            product_cost = 1
        else:
            product_cost = random.randrange(1, invoice_rest - i, 2)
    except ValueError as e:
        print(str(e))
        print("Bleme")
        print("nbr of products :" + str(invoice_nbrof_products) + "\ni :" + str(i) + "\nRest : " + str(invoice_rest))
        product_cost = 1
    products_list.append([product_name, str(product_cost)])
    invoice_rest = invoice_rest - product_cost
    i = i - 1

#Messing with the list generated
random.shuffle(products_list)

#File writing
invoice_file = open(nameofinvoice, 'w')
invoice_file.write( unique_number + "\n")
for i in range(0, invoice_nbrof_products):
    invoice_file.write(products_list[i][0] + " " + products_list[i][1] + " 1")
    invoice_file.write("\n")
invoice_file.write(str(invoice_sum))
invoice_file.close()
