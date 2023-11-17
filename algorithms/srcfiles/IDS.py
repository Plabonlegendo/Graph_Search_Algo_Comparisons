import puzzlebox as pb
import numpy as nump
from queue import PriorityQueue

class IDS():
    index = 0
    str_to_ind = dict()
    ind_to_str = dict()
    goal = ""


    def __init__(self):
        pass

    def recursive_dls(self ,box, limit):
        if box.puzzleboxtostr() == self.goal :
            ans = list()
            while box != None :
                ans.insert(0,box)
                box = box.parent
            return ans

        elif limit == 0 :
            return -1;

        else :
            #print(box.box, ' ', limit)

            cutoff = False

            moves = ["Right","Left","Up","Down"]

            for move in moves :
                tebox = box.select(move)
                if tebox != False :
                    pair = (tebox.puzzleboxtostr() ,limit)
                    #if len(self.str_to_ind)%1000 == 0 :
                    #    print(len(self.str_to_ind))

                    if not ( pair in self.str_to_ind):
                        tebox.parent = box
                        tebox.move = move
                        tebox.depth = box.depth + 1
                        self.str_to_ind[(tebox.puzzleboxtostr(),limit)] = self.index
                        self.ind_to_str[self.index] = tebox
                        self.index = self.index + 1

                        returntype = self.recursive_dls(tebox, limit -1)

                        if returntype == -1:
                            cutoff = True
                        elif returntype != False:
                            return returntype

            if cutoff == True :
                return -1
            else :
                return False

    def ids(self , box):
        self.goal = ""

        for i in range (box.boxsize*box.boxsize):
            self.goal = self.goal + str(i) + ","

        if box.puzzleboxtostr() == self.goal :
            ans = list()
            ans.insert(0,box)
            return ans

        limit = 0
        while True :
            self.str_to_ind.clear()
            self.ind_to_str.clear()
            self.index = 0

            self.str_to_ind[(box.puzzleboxtostr(),limit)] = self.index
            self.ind_to_str[self.index] = box
            self.index = self.index + 1

            returntype = self.recursive_dls(box, limit)

            if returntype != -1 :
                return returntype
            else :
                limit = limit + 1
