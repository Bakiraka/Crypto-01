#!/usr/bin/env python

###################################################################
####    Merchant program generating and invoice                ####
####    Arguments (optionals) : Number of products             ####
####    The invoice will be of the form :                      ####
####    unique id                                              ####
####    product1 price1                                        ####
####    product2 price2                                        ####
####    sum                                                    ####
###################################################################
import merchant_tools
import random
import sys

#checking the arguments
if( len(sys.argv) >= 2 ):
    #Number of products generated
    try:
        number_of_products = int(sys.argv[1])
    except (ValueError):
        print("Number of products given in parameter is wrong !")
        sys.exit()
    if(number_of_products < 1):
        print("Number of products given in parameter is wrong !")
        sys.exit()
else:
    #We'll generate up to 5 products
    number_of_products = random.randrange(1, 6)

#Guid generation
#unique_number = str(merchant_tools.randomnumber())
unique_number = str(merchant_tools.randomnumber())
while(merchant_tools.check_uid_exist(unique_number)):
    unique_number = str(merchant_tools.randomnumber())
merchant_tools.save_unique_id(unique_number)
#unique_number = guid_generation.generate_uuid()

#products_list initialisation
products_list = []

#Product generation
sum = 0
for i in range(0, number_of_products * 2):
    product_number = random.randrange(0, 100)
    product_name = "Product" + str(product_number)
    #Price generation (kindof random, depending on product name, but always the same)
    random.seed(product_number)
    product_cost = random.randrange(product_number, (product_number * 10) + 10, 2)
    products_list = products_list + [ product_name, str(product_cost)]
    sum += product_cost

#File writing
invoice_file = open('invoice.txt', 'w')
invoice_file.write( unique_number + "\n")
for i in range(0, number_of_products * 2, 2):
    invoice_file.write(products_list[i] + " " + products_list[i+1] + " 1")
    invoice_file.write("\n")
invoice_file.write(str(sum))

invoice_file.close()
