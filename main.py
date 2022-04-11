import ipaddress
import math
############################################### a function to validate the ip address ########
def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address))

########################### main function to read and check and split the ip ##########
def checkip () :
    ipclass="a"
    userip= input ("please enter the ip  ")
    # userip=useripandmask[0:-3]
    # mask=useripandmask[-3:18:-1]
    import re

    splitted= (re.split('[. | /]',userip))
    print (splitted[0])
    validate_ip_address(userip[:-3])
    firstoc=splitted[0]
    firstoc=int(firstoc)
    if firstoc >= 10 and  firstoc < 127 :
        ipclass="a"
        submask="255.0.0.0"
        #print("the class of ip you entered is :", ipclass, "the subnetMask for this class is :", submask)

    elif firstoc >= 128 and  firstoc < 192 :
        ipclass="b"
        submask="255.255.0.0"
        #print("the class of ip you entered is :", ipclass, "the subnetMask for this class is :", submask)

    elif firstoc >= 192 and  firstoc < 254:
        ipclass = "c"
        submask="255.255.255.0"
        #print("the class of ip you entered is :", ipclass, "the subnetMask for this class is :", submask)

    else :
        print ("please run again with a legal usable ip address ")
    return splitted,ipclass,submask
############################### subnetting ##########################3
workip,ipclass,submask=checkip()
print(workip,submask,ipclass)
if ipclass =="a" :
    ipclass="8"
elif ipclass =="b":
    ipclass="16"
elif ipclass =="c":
    ipclass="24"
else:
    print("something went wrong no class returned please run again with right values ")
print("ipclass was replaces by cidr number that matches the class entered :",ipclass )
subnet_num=2**(int(workip[4])-int(ipclass))
hosts_num=2**(32-int(workip[4]))
print("the number of subnets available :: ",subnet_num)
print("the number of host available :: ",hosts_num-2)