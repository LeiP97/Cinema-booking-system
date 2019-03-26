#!/usr/bin/env python3
import pickle
import numpy as np
class Employee:
    def Login(self, employeeUser):
        while True:
            username = input('Username: ')
            if username == employeeUser[0]:
                password = input('Password: ')
                if password == employeeUser[1]:
                    print('\nWelcome to cinema management system! *EMPLOYEE ONLY*')
                    print('****************************************************')
                    break
                else:
                    print('Unvalid password. Please enter again.')
            else:
                print('Unvalid username. Please enter again.')
                    
    def option(self):                    
        print('''\nOptions:
              1. Add a film
              2. Room setting for a specified film/date/time
              3. Basic information for a given film/date/time
              4. Export a list of cinema infomation
              5. Log out''')
        while True:
            a = input('Please select an option with number:')
            if a not in ['1','2','3','4','5']:
                print('Unvalid option. Please select again.')
            else:
                return a
                
    def AddFilm(self, info):
        filmName = input('Please input new film\'s name: ').strip()
        ReadyWrite = filmName + ','
        while True:
            dt = input('Please input date and time(eg.01/02/2018-5pm): ').strip()
            if  14 <= len(dt) <= 15:
                if dt not in info:
                    info[dt] = [filmName]
                    info[dt].append(np.full((7, 7), chr(9723)))
                    info[dt].append(0)
                    info[dt].append(49)
                    ReadyWrite = ReadyWrite + dt + ','       #文件里的顺序和info表的顺序不一致
                    print(filmName + ' for ' + dt + ' has been added.')
                else:
                    print('This date and time has been planned, please enter other dates and times.')
                    continue
            else:
                print('Unvalid input. Please enter again.')
                continue
            f = input('Have finished writting all dates and times for this film? (Y/N): ')
            if f.upper() == 'Y':
                briefsdes = input('Please input brief description of this film: ')
                #-----将description写进descriptionList----------#
                with open('description.txt', 'rb') as des:
                    descriptionList = pickle.load(des)
                descriptionList[filmName] = briefsdes
                with open('description.txt', 'wb') as des:
                   pickle.dump(descriptionList, des)
                #-----------写完---------------------------------#
                ReadyWrite = ReadyWrite + briefsdes + '\n'
                with open('employee.txt', 'a') as emp:
                    emp.write(ReadyWrite)
                break
    
    def RoomSetting(self, info):       #打印当前room setting
        ROW = [chr(ord('A') + x) for x in range(7)]
        while True:
            a = input('Pleaase input date/time/film (eg.01/01/2018-3pm, film): ')
            dtf = a.split(',')
            if len(dtf) != 2:
                print('Unvalid input. Please enter again.')
                continue
            if dtf[0] in info and dtf[1].strip() == info[dtf[0]][0]:
                seat = info[dtf[0]][1]
                print('\n     Screen')
                for i in range(7):
                    print(ROW[i], end = ' ')
                    for j in range(7):
                        print(seat[i,j], end = ' ')
                    print('')
                print('  1 2 3 4 5 6 7')
                print(chr(9723) + ': avaible')
                print(chr(9724) + ': booked')
                break
            else:
                print('Unvalid input. Please enter again.')
            
    def basicInfo(self, info):
        flag = 1
        while flag:
            a = input('Pleaase input date/time/film: (eg.01/01/2018-3pm, film) ')
            dtf = a.split(',')
            if dtf[0] in info and dtf[1].strip() == info[dtf[0]][0]:
                flag = 0
                book = info[dtf[0]][2]
                availble = info[dtf[0]][3]
                print('Total numbe of seats: 49')
                print('Booked ones: ', book)
                print('Availble ones: ', availble)
            else:
                print('Unvalid inpput. Please enter again.')
                
    def exportList(self, info):
        for i in info:
            print(info[i][0], i, 'Booked Ones: ', info[i][2], 'Available Ones: ', info[i][3])