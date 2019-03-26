#!/usr/bin/env python3
import datetime
import pickle

#descriptionList = {'Life of Pi':'''A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.''',
 #              'Manchester by the Sea':'''A depressed uncle is asked to take care of his teenage nephew after the boy's father dies.''',
  #             'American Beauty':'''A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.''',
   #            'Forrest Gump':'''The presidencies of Kennedy and Johnson, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.''',
    #           'Once Upon a Time in America':'''A former Prohibition-era Jewish gangster returns to the Lower East Side of Manhattan over thirty years later, where he once again must confront the ghosts and regrets of his old life.''',
     #          'Titanic':'''A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.'''}

#with open('description.txt', 'wb') as des:
 #   pickle.dump(descriptionList, des)

class character(Exception):
    pass

class Customer:
        
    def Login(self, customerUser):
        while True:
            self.username = input('Username: ')
            if self.username in customerUser:
                password = input('Password: ')
                if password == customerUser[self.username]:
                    print('\nWelcome to cinema booking system! *CUSTOMER ONLY*')
                    print('***************************************************')
                    break
                else:
                    print('Unvalid password. Please enter again.')
            else:
                print('Unvalid username. Please enter again.')
                
    def option(self):                    
        print('''\nOptions:
              1. Update your profile (email or phone number)
              2. Select a date to see what films available
              3. Book a Seat
              4. Cancel your upcoming booking
              5. Check you current booking history
              6. Log out''')
        while True:
            a = input('Please select an option with number:')
            if a not in ['1','2','3','4','5','6']:
                print('Unvalid option. Please select again.')
            else:
                return a
            
    def update(self, contact):
        while True:
                k = input('What do you want to change: 1.email 2.phone number: (please enter the number): ')
                if k == '1':
                    e = input('Please input your new email: ')
                    contact[self.username][0] = e
                    print('Your change has been saved.')
                    break
                elif k == '2':
                    p = input('Please input your new phone number: ')
                    contact[self.username][1] = p
                    print('Your change has been saved.')
                    break
                else:
                    print('Invalid input. Please enter again.')
                    
    def available(self, info):
            with open('description.txt', 'rb') as des:
                descriptionList = pickle.load(des)
            date = input('Please input a date(eg. 01/02/2014): ')
            flag = 0
            for i in info:
                if i[0:10] == date:
                    flag = 1
                    print(i)
                    print(info[i][0])
            #----------print description----------------------#
                    for j in descriptionList:
                        if j == info[i][0]:
                            print(descriptionList[j])
            #-------print roomsetting-------------------------#
                    ROW = [chr(ord('A') + x) for x in range(7)]
                    seat = info[i][1]
                    print('\n     Screen')
                    for i in range(7):
                        print(ROW[i], end = ' ')
                        for j in range(7):
                            print(seat[i,j], end = ' ')
                        print('')
                    print('  1 2 3 4 5 6 7')
                    print(chr(9723) + ': avaible')
                    print(chr(9724) + ': booked')
                    print('')
            if flag == 0:
                print('No films available in your selected date or your input is not formatted.')
                
    def book(self, info, history):   #exception
        flag = 1
        while flag:
            a = input('Please input date/time/film(eg.01/01/2018-3pm, film): ')
            dtf = a.split(',')
            try:
                dtf[1] = dtf[1].strip()
            except:
                print('Invalid input. Please enter again.')
                continue
            if dtf[0] in info and dtf[1] == info[dtf[0]][0]:
                flag = 0
                flag1 = 1  #判断s是否按格式输入
                while True:
                    while flag1:
                        try:
                            s = input('Select a seat (eg. A1): ')
                            if s[0] not in ['A','B','C','D','E','F','G'] or int(s[1]) not in range(1,8) or len(s) != 2:
                                raise character
                            flag1 = 0
                        except:
                            print('Unvalid input. Please input in format, eg. A1.')
                    if info[dtf[0]][1][ord(s[0]) - 65][int(s[1]) - 1] == chr(9724):
                        print('This seat has been booked. Please select another one.')
                        break
                    elif info[dtf[0]][1][ord(s[0]) - 65, int(s[1]) - 1] == chr(9723):
                        info[dtf[0]][1][ord(s[0]) - 65, int(s[1]) - 1] = chr(9724) #把info里相应座位变黑
                        info[dtf[0]][2] += 1                                       #booked 加1
                        info[dtf[0]][3] -= 1                                       #available 减1
                        print('Your reservation is sucessful!')
                        history[self.username].append([dtf[0], dtf[1], s])
                        print('Your booking summary: ')
                        print(dtf[0], dtf[1], s)
                        break
                    else:
                        print('Invalid input. Please enter again.')
            else:
                print('Invalid input. Please enter again.')
                
    def deletehistory(self, history, info):
        while True:
            dt = input('Please input date and time (eg. 01/09/2019-6pm):')
            flag1 = 0
            flag2 = 0
            for i in history[self.username]:
                if i[0] == dt:
                    flag1 = 1
                    if dt[-2:] == 'pm':
                        dt = dt[0:11] + str(int(dt[11:-2]) + 12)
                    else:
                        dt = dt[0:-2]
                    d1 = datetime.datetime.strptime(dt, '%d/%m/%Y-%H')
                    d2 = datetime.datetime.strptime('11/01/2019-09', '%d/%m/%Y-%H')
                    delta = d1 - d2
                    if delta.days > 0: 
                        info[i[0]][1][ord(i[2][0]) - 65][int(i[2][1]) - 1] = chr(9723) #把info里相应座位变白
                        info[i[0]][2] -= 1                                             #booked 减1
                        info[i[0]][3] += 1                                             #available 加1
                        history[self.username].remove(i)
                        print('Deletion Successful!')
                        flag2 = 1
            if flag2 == 1 and flag1 == 1:
                break
            if flag2 == 0 and flag1 == 1:
                print('You can only delete future booking record.')
                break
            if flag1 == 0:
                print('No such booking history or your inout is not formatted.')
                break
            
    def checkHistory(self, history):
        print('Here is your booking history.')
        for i in history[self.username]:
            print(i)