import numpy as nump
from copy import deepcopy
import copy

class puzzlebox:
    zerox=0
    zeroy=0
    boxsize = 0
    depth = 0
    move = ""
    parent = None
    box = nump.full((1,1),0)

    def __init__(self , boxsize, returntype):
        self.boxsize = boxsize
        if returntype == 0:
            self.box = nump.random.permutation(self.boxsize*self.boxsize)
            self.box = nump.reshape(self.box,(boxsize,boxsize))

            for i in range(boxsize):
                for j in range(boxsize):
                     if self.box[i][j] == 0:
                        zerox = i
                        zeroy = j
        elif returntype == 1:
            read = open("datafile/input.txt")
            read_line = read.readlines()
            read.close()
            #print(read_line)
            self.boxsize = int(read_line[0])
            self.box = nump.full((self.boxsize,self.boxsize),0)

            i=0
            for cs in read_line:
                if cs == read_line[0]:
                    continue
                strs= cs.split()
                #print(strs)
                j=0
                for num in strs:
                    self.box[i][j] = int(num)
                    if(self.box[i][j] == 0):
                        self.zerox = i
                        self.zeroy = j
                    j=j+1
                i=i+1

    def __cmp__(self, other):
        return True

    def __gt__(self, other):
        return True

    def puzzleboxtostr(self):
        puzzlestr = ""

        for i in range (self.boxsize):
            for j in range(self.boxsize):
                puzzlestr = puzzlestr + str(self.box[i][j]) +","
        return puzzlestr

    def isvalid(self,x,y):
        if(x>=0 and x<self.boxsize and y>=0 and y<self.boxsize):
                return True
        return False

    def Right(self):
        if not (self.isvalid(self.zerox,self.zeroy-1)):
            return False
        tempbox = puzzlebox(1,0)
        tempbox.zerox= self.zerox
        tempbox.zeroy= self.zeroy
        tempbox.box = copy.deepcopy(self.box)
        tempbox.boxsize = self.boxsize
        tempbox.box[tempbox.zerox][tempbox.zeroy] , tempbox.box[tempbox.zerox][tempbox.zeroy-1] = tempbox.box[tempbox.zerox][tempbox.zeroy-1] , tempbox.box[tempbox.zerox][tempbox.zeroy]
        tempbox.zeroy = tempbox.zeroy-1

        return tempbox

    def left(self):
        if not (self.isvalid(self.zerox,self.zeroy+1)):
            return False
        tempbox = puzzlebox(1,0)
        tempbox.zerox= self.zerox
        tempbox.zeroy= self.zeroy
        tempbox.box = copy.deepcopy(self.box)
        tempbox.boxsize = self.boxsize
        tempbox.box[tempbox.zerox][tempbox.zeroy] , tempbox.box[tempbox.zerox][tempbox.zeroy+1] = tempbox.box[tempbox.zerox][tempbox.zeroy+1] , tempbox.box[tempbox.zerox][tempbox.zeroy]
        tempbox.zeroy = tempbox.zeroy+1

        return tempbox

    def up(self):
        if not (self.isvalid(self.zerox+1,self.zeroy)):
            return False
        tempbox = puzzlebox(1,0)
        tempbox.zerox= self.zerox
        tempbox.zeroy= self.zeroy
        tempbox.box = copy.deepcopy(self.box)
        tempbox.boxsize = self.boxsize
        tempbox.box[tempbox.zerox][tempbox.zeroy] , tempbox.box[tempbox.zerox+1][tempbox.zeroy] = tempbox.box[tempbox.zerox+1][tempbox.zeroy] , tempbox.box[tempbox.zerox][tempbox.zeroy]
        tempbox.zerox = tempbox.zerox+1

        return tempbox

    def down(self):
        if not (self.isvalid(self.zerox-1,self.zeroy)):
            return False
        tempbox = puzzlebox(1,0)
        tempbox.zerox= self.zerox
        tempbox.zeroy= self.zeroy
        tempbox.box = copy.deepcopy(self.box)
        tempbox.boxsize = self.boxsize
        tempbox.box[tempbox.zerox][tempbox.zeroy] , tempbox.box[tempbox.zerox-1][tempbox.zeroy] = tempbox.box[tempbox.zerox-1][tempbox.zeroy] , tempbox.box[tempbox.zerox][tempbox.zeroy]
        tempbox.zerox = tempbox.zerox-1

        return tempbox

    def select(self,action):
        if action == "Right":
            return self.Right()
        elif action == "Left":
            return self.left()
        elif action == "Up":
            return self.up()
        elif action == "Down":
            return self.down()

    def manhat_distance(self):
        distance = 0

        for i in range(self.boxsize):
            for j in range(self.boxsize):
                currentvalue = self.box[i][j]
                xvalue = currentvalue//self.boxsize
                yvalue = currentvalue%self.boxsize

            distance = distance + abs(xvalue - i)+abs(yvalue-1)
        return distance

    def displace_distance(self):
        distance = 0

        for i in range(self.boxsize):
            for j in range(self.boxsize):
                currentvalue = self.boxsize[i][j]
                xvalue = currentvalue//self.boxsize
                yvalue = currentvalue%self.boxsize
        if not(i == xvalue and j == yvalue):
            distance = distance + 1
        return distance
