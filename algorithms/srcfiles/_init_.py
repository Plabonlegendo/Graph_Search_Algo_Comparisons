import numpy as nump
import puzzlebox as pb
import matplotlib.pyplot as plt
import BFS
import UCS
import GBFS
import Astar
import DLS
import IDS
import time

user_choice = 0

while True :
    user_choice = input("Please choose a option\n 1. input from user\n 2.Algorithm Performence\n")
    user_choice = int(user_choice)

    if user_choice == 1 :
        puzbox = pb.puzzlebox(None,returntype = 1)

        output = open("out.txt","w+")

        algo = input("please choose a option\n 1.BFS\n2.UCS\n3.GBFS\n4.Astar\n5.DLS\n6.IDS\n")
        algo = int(algo)

        print("the algorithm is Running.the output will be written in out.txt")

        if algo == 1:
            starttime = time.time()
            output.write("BFS is Running\n")
            ans = BFS.BFS()
            ans = ans.bfs(puzbox)
            finishtime = time.time()
            processTime = finishtime-starttime
            #print("Time taken: " + str(processTime) + "\n")
            outp5ut.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                #print("Number of steps: " + str(len(ans)-1) + "\n\n")
                for puzbox in ans:
                    #print(puzbox.move + "\n")
                    output.write(puzbox.move + "\n\n")
                    output.write(str(puzbox.box) + "\n\n")

        elif algo == 2:
            starttime = time.time()
            output.write("UCS is Running\n")
            ans = UCS.UCS()
            ans = ans.ucs(puzbox)
            finishtime = time.time()
            processTime = finishtime-starttime
            #print("Time taken: " + str(processTime) + "\n")
            output.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                #print("Number of steps: " + str(len(ans)-1) + "\n\n")
                for puzbox in ans:
                    #print(puzbox.move + "\n")
                    output.write(puzbox.move + "\n\n")
                    output.write(str(puzbox.box) + "\n\n")

        elif algo == 3:
            starttime = time.time()
            output.write("GBFS is Running\n")
            ans = GBFS.GBFS()
            ans = ans.gbfs(puzbox)
            finishtime = time.time()
            processTime = finishtime-starttime
            #print("Time taken: " + str(processTime) + "\n")
            output.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                #print("Number of steps: " + str(len(ans)-1) + "\n\n")
                for puzbox in ans:
                    #print(puzbox.move + "\n")
                    output.write(puzbox.move + "\n\n")
                    output.write(str(puzbox.box) + "\n\n")

        elif algo == 4:
            starttime = time.time()
            output.write("Astar is Running\n")
            ans = Astar.Astar()
            ans = ans.astar(puzbox)
            finishtime = time.time()
            processTime = finishtime-starttime
            #print("Time taken: " + str(processTime) + "\n")
            output.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                #print("Number of steps: " + str(len(ans)-1) + "\n\n")
                for puzbox in ans:
                    #print(puzbox.move + "\n")
                    output.write(puzbox.move + "\n\n")
                    output.write(str(puzbox.box) + "\n\n")
        elif algo == 5:
            starttime = time.time()
            output.write("DLS is Running\n")
            ans = DLS.DLS()
            ans = ans.dls(puzbox,20)
            finishtime = time.time()
            processTime = finishtime-starttime
            output.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                if ans == -1:
                    output.write("Cutoff Occured. No solution"+ "\n\n")
                else:
                    output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                    for box in ans:
                        output.write(box.move + "\n\n")
                        output.write(str(box.box) + "\n\n")

        elif algo == 6:
            starttime = time.time()
            output.write("IDS is Running\n")
            ans = IDS.IDS()
            ans = ans.ids(puzbox)
            finishtime = time.time()
            processTime = finishtime-starttime
            #print("Time taken: " + str(processTime) + "\n")
            output.write("Time taken: " + str(processTime) + "\n")
            if ans == False:
                output.write("No solution\n\n")
            else:
                output.write("Number of steps: " + str(len(ans)-1) + "\n\n")
                #print("Number of steps: " + str(len(ans)-1) + "\n\n")
                for puzbox in ans:
                    #print(puzbox.move + "\n")
                    output.write(puzbox.move + "\n\n")
                    output.write(str(puzbox.box) + "\n\n")
        else :
            print("input is not valid .try again\n")
        output.close()

    elif user_choice == 2:
        timeData = []
        nodeData = []
        stepData = []
        for i in range(6):
            timeData.append([0.0]*20)
            nodeData.append([0.0]*20)
            stepData.append([0.0]*20)

        for i in range(1,21):
            boxy = pb.puzzlebox(3,0)

            file_read = open("datafile/"+ str(i) + ".txt", "r")
            lines = file_read.readlines()
            file_read.close()
            boxy.box = nump.full((boxy.boxsize,boxy.boxsize), 0)
            x = 0
            for cur_str in lines:
                nums = cur_str.split()
                y = 0
                for numnum in nums:
                    boxy.box[x][y] = int(numnum)
                    if boxy.box[x][y] == 0 :
                        boxy.zerox = x
                        boxy.zeroy = y
                    y = y + 1
                x = x + 1

            #print(boxy.box)

            print("BFS algo",i)
            starttime = time.time()
            answer = BFS.BFS()
            ans = answer.bfs(boxy)
            finishtime = time.time() - starttime
            timeData[0][i-1] = finishtime
            nodeData[0][i-1] = len(answer.str_to_index)
            stepData[0][i-1] = len(ans) - 1

            print("UCS algo",i)
            start = time.time()
            answer = UCS.UCS()
            ans = answer.ucs(boxy)
            finish = time.time() - start
            timeData[1][i-1] = finish
            nodeData[1][i-1] = len(answer.str_to_index)
            stepData[1][i-1] = len(ans) - 1

            print("DLS_",i)
            start = time.time()
            answer = DLS.DLS()
            ans = answer.dls(boxy,20)
            finish = time.time() - start
            timeData[4][i-1] = finish
            nodeData[4][i-1] = len(answer.str_to_ind)
            stepData[4][i-1] = len(ans) - 1

            print("IDS algo",i)
            start = time.time()
            answer = IDS.IDS()
            ans = answer.ids(boxy)
            finish = time.time() - start
            timeData[5][i-1] = finish
            nodeData[5][i-1] = len(answer.str_to_ind)
            stepData[5][i-1] = len(ans) - 1

            print("GBFS algo",i)
            start = time.time()
            answer = GBFS.GBFS()
            ans = answer.gbfs(boxy)
            finish = time.time() - start
            timeData[2][i-1] = finish
            nodeData[2][i-1] = len(answer.str_to_index)
            stepData[2][i-1] = len(ans) - 1

            print("Astar algo",i)
            start = time.time()
            answer = Astar.Astar()
            ans = answer.astar(boxy)
            finish = time.time() - start
            timeData[3][i-1] = finish
            nodeData[3][i-1] = len(answer.str_to_index)
            stepData[3][i-1] = len(ans) - 1

        print(timeData)
        print(nodeData)
        print(stepData)
        xaxis = nump.arange(1,21)
        plt.plot(xaxis,timeData[0], linestyle = '-', label = "BFS algo")
        plt.plot(xaxis,timeData[1], linestyle = '-', label = "UCS algo")
        plt.plot(xaxis,timeData[2], linestyle = '-', label = "GBFS algo")
        plt.plot(xaxis,timeData[3], linestyle = '-', label = "Astar algo")
        plt.plot(xaxis,timeData[4], linestyle = '-', label = "DLS algo")
        plt.plot(xaxis,timeData[5], linestyle = '-', label = "IDS algo")
        plt.grid()
        plt.legend()
        plt.title("Time graph")
        plt.show()

        xaxis = nump.arange(1,21)
        plt.plot(xaxis,nodeData[0], linestyle = '-', label = "BFS algo")
        plt.plot(xaxis,nodeData[1], linestyle = '-', label = "UCS algo")
        plt.plot(xaxis,nodeData[2], linestyle = '-', label = "GBFS algo")
        plt.plot(xaxis,nodeData[3], linestyle = '-', label = "Astar algo ")
        plt.plot(xaxis,nodeData[4], linestyle = '-', label = "DLS algo")
        plt.plot(xaxis,nodeData[5], linestyle = '-', label = "Astar algo")
        plt.grid()
        plt.legend()
        plt.title("Node graph")
        plt.show()

        xaxis = nump.arange(1,21)
        plt.plot(xaxis,stepData[0], linestyle = '-', label = "BFS algo")
        plt.plot(xaxis,stepData[1], linestyle = '-', label = "UCS algo")
        plt.plot(xaxis,stepData[2], linestyle = '-', label = "GBFS algo")
        plt.plot(xaxis,stepData[3], linestyle = '-', label = "Astar algo")
        plt.plot(xaxis,stepData[4], linestyle = '-', label = "DLS algo")
        plt.plot(xaxis,stepData[5], linestyle = '-', label = "IDS algo")
        plt.grid()
        plt.legend()
        plt.title("Step graph")
        plt.show()

    else:
        print("Invalid Input, Try again")
