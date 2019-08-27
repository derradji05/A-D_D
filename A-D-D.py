#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from time import *
from datetime import datetime
sleep(2)
print("\033[1;31m")
file_shape = open("01110010.txt",'r')     #shape-tool
text = file_shape.read()                       #Read-shape-tool
print (text)
sleep(1)
print ("")
print ("")
print ("\033[1;32mWelcome Guys ∞≠≈")
print ("")         #Space-tool
print ("") #space-02
print ("")
print ("")                #space-03
sleep(1)
print("\033[1;31m=01= \033[1;32m--- \033[1;37m Extract \033[1;31m? \033[1;32mIP \033[1;31m? \033[1;37mAdress [Phone \033[1;31m/ \033[1;37mWebSite]")
print("")
sleep(0.451)
print("\033[1;31m=02= \033[1;32m--- \033[1;37mView information about network connections ")
print("")
sleep(0.451)
print("\033[1;31m=03= \033[1;32m--- \033[1;37mScan IP Address")
print("")
sleep(0.451)
print("\033[1;31m=04= \033[1;32m--- \033[1;37mScan For AppLication Server Version")
print("")
sleep(0.451)
print("\033[1;31m=05= \033[1;32m--- \033[1;37mScan Port \033[1;31m80\033[1;32m,\033[1;31m25\033[1;32m,\033[1;31m443\033[1;32m,\033[1;31mSMTP\033[1;32m,\033[1;31mHTTP")
sleep(1)
print("")
print("")
number_12 = input("\033[1;31mEnter A Nubmber Of Tool ???>\033[1;32m ")
if number_12 == "01" or number_12 == "1":
    print("")
    print("\033[1;31m")                                    #Checking_IP
    fil00_shape = open("ssɹʍd.txt",'r')
    text_00 = fil00_shape.read()
    print (text_00)
    sleep(1)
    print("\033[1;31m")
    os.system("figlet IP")
    sleep(1)
    target = input("\033[1;32mEnter The Desired GoaL !> \033[1;31m")
    target = target.replace("http://", "")
    target = target.replace("https://", "")
    sleep(1)
    cmd = 'ping' + " " + target
    print("\033[1;31m[*] \033[1;32mWaiting targets\033[1;31m, \033[1;32mPress Ctrl + C to \033[1;31mexit...")
    print("")
    os.system(cmd)
    print("")
    sleep(2)
elif number_12 == "02" or number_12 == "2":
    print("\033[1;31m")                                               #View information
    fil01_shape = open("647270726F.txt",'r')
    text_01 = fil01_shape.read()
    print (text_01)
    sleep(1)
    print("\033[1;32m")
    os.system("netstat")
    print("\033[1;37m")
elif number_12 == "03" or number_12 == "3":
    print("\033[1;31m")
    fil02_shape = open("150145154154157.txt",'r')          #Scanner-IP
    text_02 = fil02_shape.read()
    print (text_02)
    sleep(1)
    print("\033[1;32m")
    os.system("pkg install nmap")
    os.system("clear")
    sleep(1)
    print("")
    target_01 = input("\033[1;32mEnter IP The Victim !> \033[1;31m")
    sleep(1)
    cmd_01 = 'nmap' + " " + target_01
    os.system(cmd_01)
    print("")
    print("\033[1;32m")
    os.system("figlet Completed")
    print("\033[1;37m")
elif number_12 == "04" or number_12 == "4":
    print("\033[1;31m")
    fil03_shape = open("@.txt",'r')           #Scan For AppLication Server
    text_03 = fil03_shape.read()
    print (text_03)
    sleep(1)
    print("\033[1;32m")
    os.system("pkg install nmap")
    os.system("clear")
    sleep(1)
    print("")
    target_02 = input("\033[1;32mEnter IP The Victim !> \033[1;31m")
    sleep(1)
    cmd_02 = 'nmap -sV' + " " + target_02
    os.system(cmd_02)
    print("")
    print("\033[1;32m")
    os.system("figlet Completed")
    print("\033[1;37m")
elif number_12 == "05" or number_12 == "5":
    sleep(2)
    print("\033[1;31m")     #PORT-CHECK-IP
    fil04_shape = open("010001000110010101110010.txt",'r')
    text_04 = fil04_shape.read()
    print (text_04)
    sleep(4)
    print("\033[1;32m")
    os.system("pkg install nmap")
    sleep(1)
    print("")
    print("\033[1;31m-01- \033[1;32m=== \033[1;37mScan With \033[1;32mPort 80")
    print("")
    sleep(0.55)
    print("\033[1;31m-01- \033[1;32m=== \033[1;37mScan With \033[1;32mPort 80")
    print("")
    sleep(0.55)
    print("\033[1;31m-02- \033[1;32m=== \033[1;37mScan With \033[1;32mPort 25")
    print("")
    sleep(0.55)
    print("\033[1;31m-03- \033[1;32m=== \033[1;37mScan With \033[1;32mPort 443")
    print("")
    sleep(0.55)
    print("\033[1;31m-04- \033[1;32m=== \033[1;37mScan With \033[1;32mPort SMTP")
    print("")
    sleep(0.55)
    print("\033[1;31m-05- \033[1;32m=== \033[1;37mScan With \033[1;32mPort HTTP")
    print("")
    print("")
    print("")
    tar_1 = input("Enter \033[1;31mIP \033[1;37mTarget !> \033[1;32m")
    sleep(0.564)
    port = input("Enter Number The \033[1;31mPort \033[1;37m!> \033[1;32m")
    if port == "01" or port == "1":
        print("")
        sleep(1)
        cmd_121 = "nmap -p 80" + tar_1
        print("\033[1;32m")
        os.system(cmd_121)
        print("\033[1;37m")
    elif port == "02" or port == "2":
        print("")
        sleep(1)
        cmd_122 = "nmap -p 25" + tar_1
        print("\033[1;32m")
        os.system(cmd_122)
        print("\033[1;37m")
    elif port == "03" or port == "3":
        print("")
        sleep(1)
        cmd_123 = "nmap -p 443" + tar_1
        print("\033[1;32m")
        os.system(cmd_123)
        print("\033[1;37m")
    elif port == "04" or port == "4":
        print("")
        sleep(1)
        cmd_124 = "nmap -p 80,25,443" + tar_1
        print("\033[1;32m")
        os.system(cmd_124)
        print("\033[1;37m")
    elif port == "05" or port == "5":
        print("")
        sleep(1)
        cmd_125 = "nmap -p smtp" + tar_1
        print("\033[1;32m")
        os.system(cmd_125)
        print("\033[1;37m")
    elif port == "06" or port == "6":
        print("")
        sleep(1)
        cmd_126 = "nmap -p http" + tar_1
        print("\033[1;32m")
        os.system(cmd_126)
        print("\033[1;37m")
else:
    print("\033[1;31m")
    os.system("figlet Error")
    print("\033[1;37m")
#FINISH

