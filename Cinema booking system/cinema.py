#!/usr/bin/env python3

import numpy as np
import random
import copy
import datetime
import pickle
from manage import Employee
from usage import Customer
#--------if you can't run sucessfully because can't find files, please use the code below and change path----#
#import os
#os.chdir("/Users/ll/Indouctory_programming/Final_Coursework/Lei_Peng/code")

#info = {(datetime):[film, seat, booked, available]}
def configuration():
    lines = []
    newlines = []
    global filmlist
    filmlist = ['Life of Pi', 'Manchester by the Sea', 'American Beauty', 'Forrest Gump', 'Once Upon a Time in America']
    global info
    info ={}
    global emptysetting
    emptysetting = np.full((7, 7), chr(9723))
    #global datetimelist
    #datetimelist = []
    with open('backup.txt') as back:
        lines = back.readlines()
    for i in range(5):
        a = lines[i].strip('\n')
        newlines.append(a.split(','))
    for i in range(5):
        for j in newlines[i][1:-2]:  #evey j = one datetime
            info[j] = [newlines[i][0]]
            info[j].append(np.full((7, 7), chr(9723)))
            info[j].append(0)
            info[j].append(49)
    #--------info = {(datetime):[film, seatSettinig, booked, available]} has been generated------------#
    description = {}
    
'''configuration()
with open('ip.txt', 'wb') as ip:
    pickle.dump(info, ip)'''
    
def Divide():
    print('\nWelcome to  GLORIA cinema!')
    while True:
        identity = input('Are you our employee? (Y/N) *For quit please input Q: ')
        if identity.upper() == 'Y':
            return 'Y'
        elif identity.upper() == 'N':
            return 'N'
        elif identity.upper() == 'Q':
            return 'Q'
        else:
            print('Unvalid input, please enter again!')
            
'''contact = {'Simon':['s.atkinson@gmail.com', '46859791249'], 'Russell':['is.r.barnes@outlook.com','5793926492']}
history = {'Simon':[], 'Russell':[]}'''
#history = { name:[[datetime, film, seat], [2],[3]...] }
customerUser = {'Simon':'123', 'Russell':'456'}
employeeUser = ['staff', '123']
emptysetting = np.full((7, 7), chr(9723))
#configuration()
while True:
    with open('ip.txt', 'rb') as ip:
        info = pickle.load(ip)
    D = Divide()
    if D == 'Y':
        flag = 1
    elif D == 'N':
        flag = 0
    elif D == 'Q':
        print('')
        print('Thank you for using this system. See you soon!')
        print('')
        break
    if flag:       #employee or customer
        e = Employee()
        e.Login(employeeUser)
        flagforE = 1
        while flagforE:     #if employee choose log out
            selection = e.option()
            if selection == '1':
                e.AddFilm(info)
            elif selection == '2':
                e.RoomSetting(info)
            elif selection == '3':
                e.basicInfo(info)
            elif selection == '4':
                e.exportList(info)
            elif selection == '5':
                with open('ip.txt', 'wb') as ip:
                    pickle.dump(info, ip)
                print('Log out Sucessful!')
                flagforE = 0

    else:
        c = Customer()
        c.Login(customerUser)
        flagforC = 1
        with open('customer.txt', 'rb') as customer:
            contact = pickle.load(customer)
            history = pickle.load(customer)
        while flagforC:      #if employee choose log out
            selection = c.option()
            if selection == '1':
                c.update(contact)
            elif selection == '2':
                c.available(info)
            elif selection == '3':
                c.book(info, history)
            elif selection == '4':
                c.deletehistory(history, info)
            elif selection == '5':
                c.checkHistory(history)
            elif selection == '6':
                with open('customer.txt', 'wb') as customer:
                    pickle.dump(contact, customer)
                    pickle.dump(history, customer)
                with open('ip.txt', 'wb') as ip:
                    pickle.dump(info, ip)
                print('Log out Sucessful!')
                flagforC = 0
