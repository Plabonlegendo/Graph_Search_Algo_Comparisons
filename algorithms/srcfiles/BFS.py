import puzzlebox as pb
import numpy as nump
from queue import PriorityQueue

class BFS:
    index = 0
    str_to_index = dict()
    index_to_str = dict()
    goal = ""
    parent = dict()
    que = list()

    def __init__(self):
        pass

    def bfs(self,puzzlebox):
        for i in range (puzzlebox.boxsize*puzzlebox.boxsize):
            self.goal = self.goal + str(i)+","
        #print(self.goal)

        if puzzlebox.puzzleboxtostr() == self.goal:
            ans = list()
            ans.insert(0,puzzlebox)
            return ans
        self.str_to_index.clear()
        self.index_to_str.clear()
        self.parent.clear()
        self.que.clear()
        self.index = 0
        self.str_to_index[puzzlebox.puzzleboxtostr()] = self.index
        self.index_to_str[self.index] = puzzlebox
        self.index = self.index +1
        self.que.append(puzzlebox)
        #print(self.index)
        moves = ["Right","Left","Up","Down"]

        while(len(self.que)>0):
            tebox = self.que.pop(0)
            #print(tebox.puzzleboxtostr())
            #print(len(self.str_to_index))
            #print(tebox.box)
#            if len(self.str_to_index)%1000 == 0 :
#                print(len(self.str_to_index))
            for move in moves:
                #print (move)
                netebox = tebox.select(move)
                if netebox != False :
                    #print(netebox.puzzleboxtostr())
                    if not (netebox.puzzleboxtostr() in self.str_to_index):
                        #print(netebox.puzzleboxtostr())
                        netebox.parent = tebox
                        netebox.move = move
                        netebox.depth = tebox.depth + 1
                        self.str_to_index[netebox.puzzleboxtostr()] = self.index
                        self.index_to_str[self.index] = netebox
                        self.index = self.index + 1
                        self.que.append(netebox)

                        if(netebox.puzzleboxtostr() == self.goal):
                            ans = list()
                            while netebox is not None :
                                ans.insert(0,netebox)
                                netebox = netebox.parent
                            return ans

        return False
