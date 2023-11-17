import puzzlebox as pb
import numpy as nump
from queue import PriorityQueue

class UCS():
    index = 0
    str_to_index = dict()
    index_to_str = dict()
    goal = ""

    prior_que = PriorityQueue()

    def __init__(self):
        pass

    def ucs(self , puzzlebox):
        self.goal =""

        for i in range (puzzlebox.boxsize*puzzlebox.boxsize):
            self.goal = self.goal + str(i)+","

        self.str_to_index.clear()
        self.index_to_str.clear()
        while not self.prior_que.empty():
            self.prior_que.get()

        if puzzlebox.puzzleboxtostr() == self.goal:
            ans = list()
            ans.insert(0,puzzlebox)
            return ans
        self.index = 0
        self.str_to_index[puzzlebox.puzzleboxtostr()] = self.index
        self.index_to_str[self.index] = puzzlebox
        self.index = self.index +1
        self.prior_que.put((0,puzzlebox))

        moves = ["Right","Left","Up","Down"]

        while self.prior_que:
            tebox = self.prior_que.get()
            tempbox = tebox[1]
            #print(tempbox.box)
#            if len(self.str_to_index)%1000 == 0 :
#                print(len(self.str_to_index))
            #print(len(self.str_to_index))
            for move in moves :
                #print(move)
                netebox = tempbox.select(move)
                if netebox != False:
                    #print(netebox.box)
                    if not (netebox.puzzleboxtostr() in self.str_to_index):
                        netebox.depth = tempbox.depth +1
                        netebox.parent = tempbox
                        netebox.move = move
                        self.str_to_index[tempbox.puzzleboxtostr()] = self.index
                        self.index_to_str[self.index] = tempbox
                        self.index = self.index + 1
                        self.prior_que.put((netebox.depth,netebox))
                        #print("habijabi")
                        if netebox.puzzleboxtostr() == self.goal :
                            ans = list()
                            while netebox != None:
                                ans.insert(0,netebox)
                                netebox = netebox.parent
                            return ans

        return False
