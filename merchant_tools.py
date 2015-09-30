#!/usr/bin/env python
import uuid
import random

#basic unique id random generation
def randomnumber():
    return random.getrandbits( 150)

#guid generation
def generate_uuid():
    return str(uuid.uuid4())

def save_unique_id(uid):
    uids_file = open("idgenerated", 'a')
    uids_file.write(str(uid) + "\n")
    uids_file.close()

def check_uid_exist(uid):
    try:
        uids_file = open("idgenerated", 'r')
    except (OSError, IOError) as error:
        print("Could not check if the uid exists, Error reading file : ", error)
        return False
    line = uids_file.readline()
    while(line):
#        print("comparing " + line + " and " + uid)
        if(uid in line):
            print("uid already exists !")
            uids_file.close()
            return True
        line = uids_file.readline()
    uids_file.close()
    return False
