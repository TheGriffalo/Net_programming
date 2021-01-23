import os.path
import sys

#Checking IP address file and content validity
def ip_file_valid():

    #Prompting user for input
    ip_file = input("\n# Enter IP file pathand name e.g. /files/xyz.txt: ")

    #Checking if the file exists
    if os.path.isfile(ip_file) == True:
        print("\n *IP file is valid :)\n")

    else:
        print("\n* File {} does not exist ;( Please check and try again.\n".format(ip_file))



ip_file_valid()

