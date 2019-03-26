#!/usr/bin/env python3
import numpy as np
from copy import deepcopy

BLACK = [chr(9812 + x) for x in range(6, 12)]
BK, BQ, BR, BB, BKN, BP = BLACK
WHITE = [chr(9812 + x) for x in range(0, 6)]
WK, WQ, WR, WB, WKN, WP = WHITE

ROWNAME = [chr(ord('a') + x) for x in range(8)]
COLNAME = [chr(ord('1') + x) for x in range(8)]


def KING(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    if abs(dx) in [0, 1] and abs(dy) in [0, 1]:
        return True
    else:
        return False

def KNIGHT(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    if abs(dx) in [1, 2] and abs(dy) in [1, 2] and dx != dy:
        return True
    else:
        return False
    
def QUEEN(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    xl = np.linspace(pre[0], aft[0], abs(dx) + 1, dtype = int)
    yl = np.linspace(pre[1], aft[1], abs(dy) + 1, dtype = int)
    if abs(dx) ==0 and abs(dy) != 0:
        return list(zip(xl, yl))
    elif abs(dx) != 0 and abs(dy) == 0:
        return list(zip(xl, yl))
    elif abs(dx) == abs(dy):
        return list(zip(xl, yl))
    else:
        return False

def PAWN(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    #pawn can only have one step forward but first time 2 steps forward is ok (black or whitr, pawn can't step back) and eat others in cross way
    if b.BOARD[pre[0]][pre[1]] in WHITE:
        if dx == 1 and abs(dy) == 1 and b.BOARD[aft[0]][aft[1]] != '*':#eat others in cross way
            return True
        elif pre[0] == 1:#2 steps first time
            if dx in [1, 2] and dy == 0 and b.BOARD[aft[0]][aft[1]] == '*':#can't eat others forward
                return True
        elif dx == 1 and dy == 0 and b.BOARD[aft[0]][aft[1]] == '*':
            return True
        else:
            return False
    if b.BOARD[pre[0]][pre[1]] in BLACK:
        if dx == -1 and abs(dy) == 1 and b.BOARD[aft[0]][aft[1]] != '*':
            return True
        if pre[0] == 6:
            if dx in [-1, -2] and dy == 0 and b.BOARD[aft[0]][aft[1]] == '*':
                return True
        elif dx == -1 and dy == 0 and b.BOARD[aft[0]][aft[1]] == '*':
            return True
        else:
            return False

def BISHOP(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    xl = np.linspace(pre[0], aft[0], abs(dx) + 1, dtype = int)
    yl = np.linspace(pre[1], aft[1], abs(dy) + 1, dtype = int)
    if abs(dx) == abs(dy):
        return list(zip(xl, yl))
    else:
        return False

def ROOK(pre, aft):
    if pre == aft:
        return False
    dx, dy = aft[0] - pre[0], aft[1] - pre[1]
    xl = np.linspace(pre[0], aft[0], abs(dx) + 1, dtype = int)
    yl = np.linspace(pre[1], aft[1], abs(dy) + 1, dtype = int)
    if abs(dx) == 0 or abs(dy) == 0:
        return list(zip(xl, yl))
    else:
        return False

class board:
    def __init__(self):
        self.BOARD = np.full((8, 8), '*')
        self.BOARD[0, :] = [WR, WKN, WB, WQ, WK, WB, WKN, WR]
        self.BOARD[1, :] = [WP] * 8
        self.BOARD[-1, :] = [BR, BKN, BB, BQ, BK, BB, BKN, BR]
        self.BOARD[-2, :] = [BP] * 8
        self.gameStatus = 'Running'
        while True:
            self.turn = input('Please Enter Which First(enter B or W):')
            if self.turn not in ['B', 'W']:
                print('Invalid input, Please enter B or W...\n')
            else:
                break
        
    def print(self):
        for i in range(8):
            print('\n' + COLNAME[7-i], end = ' ')
            for j in range(8):
                print(self.BOARD[7-i][j], end = ' ')
        print('\n' + ' '*2 + ' '.join(ROWNAME))
    
    def getPos(self, piece):#available for king or queen
        for i in range(8):
            for j in range(8):
                if self.BOARD[i][j] == piece:
                    return (i, j)
                
    def getColor(self, pos):
        if self.BOARD[pos[0]][pos[1]] in WHITE:
            return 1
        elif self.BOARD[pos[0]][pos[1]] in BLACK:
            return 2
        else:
            return 3

    def whitecheck(self):
        wflag = 1
        for i in range(8):
            for j in range(8):
                if self.BOARD[i][j] == WK:
                    wflag = 0
        if wflag == 1:
            self.gameSatus = 'Black Wins!!!!'
            return True
        else:
            self.gameSatus = 'Running'
            return False
        
    def blackcheck(self):
        bflag = 1
        for i in range(8):
            for j in range(8):
                if self.BOARD[i][j] == BK:
                    bflag = 0
        if bflag == 1:
            self.gameSatus = 'White Wins!!!!'
            return True
        else:
            self.gameSatus = 'Running'
            return False

    def input(self):
        while True:
            try:
                if self.turn == 'B':
                    inp = input('Black Move(eg. a1b2):')
                else:
                    inp = input('White Move(eg. a1b2):')
                px, py, ax, ay = inp
                assert px in ROWNAME and ax in ROWNAME
                assert py in COLNAME and ay in COLNAME
                self.pre = [COLNAME.index(py), ROWNAME.index(px)]
                self.aft = [COLNAME.index(ay), ROWNAME.index(ax)]
                self.prepiece = self.BOARD[self.pre[0], self.pre[1]]
                self.aftpiece = self.BOARD[self.aft[0], self.aft[1]]
                #ensure don't eat your own piece
                if self.turn == 'B':
                    assert self.prepiece in BLACK and self.aftpiece not in BLACK
                    assert self.judgemove(self.pre, self.aft, self.prepiece)
                if self.turn == 'W':
                    assert self.prepiece in WHITE and self.aftpiece not in WHITE
                    assert self.judgemove(self.pre, self.aft, self.prepiece)
                #chang turn
                if self.turn =='B':
                    self.turn = 'W'
                else:
                    self.turn = 'B'
                break
            except:
                print('''Invalid Move. Please check:
                      1. input as format "a1b2"
                      2.move your own piece
                      3. don\'t beat yourself
                      4. make sure your move is valid
                      5. don\'t jump over other piece
                      ...''')
                
    def move(self):
        self.BOARD[self.aft[0]][self.aft[1]] = self.BOARD[self.pre[0]][self.pre[1]]
        self.BOARD[self.pre[0]][self.pre[1]] = '*'

    def judgemove(self, pre, aft, prepiece):
            if prepiece in [BK,WK]:
                path = KING(pre, aft)
                if path:
                    pathValid = True
                else:
                    pathValid = False
            elif prepiece in [BKN, WKN]:
                path = KNIGHT(pre, aft)
                if path:
                    pathValid = True
                else:
                    pathValid = False
            elif prepiece in [BQ, WQ]:
                path = QUEEN(pre, aft)#包括起点和终点的path上的坐标的列表，如[(1,2), (2,3)]
                if path:
                    pathValid = self.pathDEC(path, prepiece)
                else:
                    pathValid = False
            elif prepiece in [BP, WP]:
                path = PAWN(pre, aft)
                if path:
                    pathValid = True
                else:
                    pathValid = False
            elif prepiece in [BB, WB]:
                path = BISHOP(pre, aft)
                if path:
                    pathValid = self.pathDEC(path,prepiece)
                else:
                    pathValid = False
            elif prepiece in [BR, WR]:
                path = ROOK(pre, aft)
                if path:
                    pathValid = self.pathDEC(path, prepiece)
                else:
                    pathValid = False
            if pathValid:#pathValid是合法与否的标志（1.走法是否合规范 2.是否越子）
                return True
            else:
                return False

    def pathDEC(self, path, prepiece):#感觉这个prepiece有点多余
        flag = True
        for i in path[1:-1]:
            if self.BOARD[i[0], i[1]] != '*':
                return False
        return True
        
                
b = board()
while True:
    b.print()
    b.whitecheck()
    b.blackcheck()
    print('The Game Status is:', b.gameSatus)
    if b.gameSatus in ['Black Wins!!!!', 'White Wins!!!!']:
        break
    b.input()
    b.move()