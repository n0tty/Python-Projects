#!/usr/bin/python


#Greetz
def greet():
  print \
  """
  MongoDB Connector and database names extractor using Python v2.7 by n0tty\n
  legendtanoybose@gmail.com
  https://github.com/n0tty

__________
\\______   \\ ____  ______ ____
 |    |  _//  _ \\/  ___// __ \\
 |    |   (  <_> )___ \\\\  ___/
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/
  """


greet()


#Module start
import pymongo
import time

print ""
print "Reason:"
print "I built this because of unavailability of internet to download the 155+ MB of MongoDB client on a linux system to generate a PoC during a PenTest"
print ""

time.sleep(1)

ip_address=raw_input("Please enter the IP address of the server: ")

while True:
        try:
                port=input("Please input the port number (default is 27017): ")
                if (port<=1 or port>=65535):
                        port=27017
                        print "You have entered a invalid port number and hence default port (27017) has been selected"
                break
        except SyntaxError:
                print "You have entered a invalid port number and hence default port (27017) has been selected"
                port=27017
                break

databases=[]

try:
        print "Connecting..."
        conn = pymongo.Connection(ip_address,port)
        print "[+] Connection is Successful"
        time.sleep(2)
        print "[*] Extracting Database Names"
        try:
                databases = conn.database_names()
                print "[+] Got Database Names successfully"
                time.sleep(2)
                print "[*] Dumping database names: "
                for x in range(0,len(databases)):
                        print databases[x]
                        time.sleep(1)
        except pymongo.errors,f:
                        print "Fail to extract databases: %s" % f
except pymongo.errors.ConnectionFailure,e:
        print "Failed to connect to the database: %s" % e



