#!/usr/bin/env python3

from random import randint

def select():
    char = ['0','X']
    if randint(0,1) == 1:
        return char[::-1]
    return char
        
def game_board(x,y,z):
    print('|'.join(x))
    print('-'*5)
    print('|'.join(y))
    print('-'*5)
    print('|'.join(z))
    print('-'*5)
    
def game(Y,M):
    if 1 <= Y <= 3:
        Y -= 1
        a[Y] = M
    if 4 <= Y <= 6:
        Y -= 4
        b[Y] = M
    if 7 <= Y <= 9:
        Y -= 7
        c[Y] = M
def computer():
    r = randint(1,9)
    while r in lsthm+lstcom and len(lsthm + lstcom) < 9:
        r = randint(1,9)
    if len(lsthm + lstcom) < 9:
        lstcom.append(r)
        game(r,comsyb)
    
def result(A,B):
    winners = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for i in winners:
        if i[0] in A and i[1] in A and i[2] in A:
            print('***Congradulations! You won!***')
            return True
        if i[0] in B and i[1] in B and i[2] in B:
            print('Sorry! You lose!')
            return True

a = [' ',' ',' ']
b = [' ',' ',' ']
c = [' ',' ',' ']
lsthm = []
lstcom = []

hmsyb, comsyb = select()
print('human is {}, compuer is {}'.format(hmsyb,comsyb))
game_board(a,b,c)

while True:
    num = int(input('# Make your move ![1-9]:'))
    if num in lstcom+lsthm or num < 1 or num > 9:
        print('Invalid number! Try again!')
        continue
    lsthm.append(num)
    game(num,hmsyb)
    computer()
    game_board(a,b,c)
    if len(lsthm + lstcom) == 9 and not result(lsthm,lstcom):
        print('Draw!')
        break
    if result(lsthm,lstcom):
        break