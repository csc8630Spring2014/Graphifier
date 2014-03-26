class align_simple:

    def __init__(self):
        self.alignmentmatrix = []
        self.route = []

    def getSequences(self, filelocation, filelocation2):
        checkFile = open(filelocation)
        for line in checkFile:
            if line[:1] == ">":
                continue
            else:
                self.seq1 = line
        checkFile = open(filelocation2)
        for line in checkFile:
            if line[:1] == ">":
                continue
            else:
                self.seq2 = line

    def initMatrix(self, init):
        start_score = score(0)
        self.seq1 = self.seq1[0:-1]
        self.seq2 = self.seq2[0:-1]
        for char1 in self.seq1:
#            print("new x")
            tempList = []
            for char2 in self.seq2:
#                print("new y")
                tempList.append(start_score)
            self.alignmentmatrix.append(tempList)

    def printmatrix(self):
        for char1 in range(0, len(self.alignmentmatrix)):
            print "[",
            for char2 in range(0, len(self.alignmentmatrix[char1])):
                print str(self.alignmentmatrix[char1][char2].getScore()) + " ",
            print("]")
        print "\n"

    def get(self, i, j):
        return self.alignmentmatrix[i][j]

    def put(self, i, j, value):
        self.alignmentmatrix[i][j] = value

    def align(self):
        for i in range(0, len(self.seq1)):
            for j in range(0, len(self.seq2)):
                #tempScore = score(self.alignmentmatrix[i][j].getScore())
                if (self.seq1[i: i + 1] == self.seq2[j: j + 1]):
                    tempScore = score('M')
                    self.put(i, j, tempScore)
                #else:
                #    self.put(i, j, tempScore)

    def sumscore(self):
        for h in range(0, len(self.alignmentmatrix)):
            for k in range(0, len(self.alignmentmatrix[0])):
                print "sumScore - score = " + str(self.alignmentmatrix[h][k].
                getScore())
                if (self.alignmentmatrix[h][k].getScore() == 'M'):
                    print "sumScore - location", h, k
                    print "sumScore - Before: " + str(self.
                    alignmentmatrix[h][k].getScore())
                    self.printmatrix()
                    if (h == 0) and (k == 0):
                        print "sumScore - inital"
                        self.alignmentmatrix[h][k].changeScore(1)
                        self.sumafter(h, k, 1)
                    elif h == 0:
                        print "sumScore -", 1
                        self.sumafter(h, k, self.alignmentmatrix[h][k - 1].
                        getScore() + 1)
                    elif k == 0:
                        print "sumScore -", 2
                        self.sumafter(h, k, self.alignmentmatrix[h - 1][k].
                        getScore() + 1)
                    else:
                        print "sumScore -", 3
                        if ((self.alignmentmatrix[h - 1][k].getScore() >=
                        self.alignmentmatrix[h][k - 1].getScore()) and
                        (self.alignmentmatrix[h - 1][k].getScore() >
                        self.alignmentmatrix[h - 1][k - 1].getScore())):
                            print "sumScore -", 4
                            print "sumScore -", (self.
                            alignmentmatrix[h - 1][k].getScore())
                            self.sumafter(h, k, self.alignmentmatrix[h - 1][k].
                            getScore() + 1)
                        elif (self.alignmentmatrix[h][k - 1].getScore() >
                        self.alignmentmatrix[h - 1][k].getScore() and
                        self.alignmentmatrix[h][k - 1].getScore() >
                        self.alignmentmatrix[h - 1][k - 1].getScore()):
                            print "sumScore -", 5
                            print "sumScore -", (self.alignmentmatrix[h][k - 1].
                            getScore())
                            self.sumafter(h, k, int(self.
                            alignmentmatrix[h][k - 1].getScore()) + 1)
                        elif (self.alignmentmatrix[h - 1][k - 1].getScore() >=
                        self.alignmentmatrix[h][k - 1].getScore() and
                        self.alignmentmatrix[h - 1][k - 1].getScore() >=
                        self.alignmentmatrix[h - 1][k].getScore()):
                            print "sumScore -", 6
                            print "sumScore -", (self.alignmentmatrix[h - 1]
                            [k - 1].getScore())
                            self.sumafter(h, k, self.alignmentmatrix
                            [h - 1][k - 1].getScore() + 1)
#            self.sumafter(h, k, self.alignmentmatrix[h][k].getScore())

    def sumafter(self, y, x, new):
        print "sumAfter - Start sumAfter starting at ", x, y
        self.printmatrix()
        for h in range(y, len(self.alignmentmatrix)):
            for k in range(x, len(self.alignmentmatrix[0])):
                if (h == y) and (k == x):
                    self.alignmentmatrix[h][k] = score(new)
                elif (self.alignmentmatrix[h][k].getScore() != 'M'):
                    self.alignmentmatrix[h][k] = score(new)
#                    print "changed" + str(k) + " " + str(h) + " to " + str(
#                    new) + " actual value: " + str(
#                    self.alignmentmatrix[h][k].getScore())
        print "sumAfter - End sumAfter"
        self.printmatrix()

    def findRoute(self, temproute, xIndex, yIndex):
        print "findRoute - ", xIndex, yIndex
        if ((xIndex == 0) and (yIndex == 0)):
            print "findroute - 0,0"
            temproute.append([0, 0])
        elif (xIndex == 0):
            print "findRoute - 0,y"
            temproute.append([xIndex, yIndex])
            temproute = (self.findRoute(temproute,
            xIndex, yIndex - 1))
        elif (yIndex == 0):
            print"findRoute - x,0"
            temproute.append([xIndex, yIndex])
            temproute = (self.findRoute(temproute,
            xIndex - 1, yIndex))
        else:
            print ("findRoute - getting score of [" + str(xIndex) + "," +
            str(yIndex) + "]")
            int(self.alignmentmatrix[xIndex - 1][yIndex].getScore())
            above = int(self.alignmentmatrix[xIndex - 1][yIndex].getScore())
            left = self.alignmentmatrix[xIndex][yIndex - 1].getScore()
            diag = self.alignmentmatrix[xIndex - 1][yIndex - 1].getScore()
            print ("findRoute - s: " + str(self.alignmentmatrix[xIndex][yIndex].
            getScore()) + " a: " + str(above) + " l: " + str(left) + " d: " +
            str(diag))
            if ((left > above) and (left > diag)):
                print ("findRoute - LEFT is best, adding [" + str(xIndex - 1) +
                 "," + str(yIndex) + "]")
                temproute.append([xIndex, yIndex])
                temproute = self.findRoute(temproute,
                xIndex, (yIndex - 1))
            elif ((above > left) and (above > diag)):
                print ("findRoute - ABOVE is best, adding [" + str(xIndex) +
                "," + str(yIndex - 1) + "]")
                temproute.append([xIndex, yIndex])
                temproute = self.findRoute(temproute,
                (xIndex - 1), yIndex)
            elif ((diag >= left) and (diag >= above)):
                print ("findRoute - DIAG is best, adding [" + str(xIndex - 1) +
                "," + str(yIndex - 1) + "]")
                temproute.append([xIndex, yIndex])
                temproute = self.findRoute(temproute,
                (xIndex - 1), (yIndex - 1))
            elif ((above == left) and (above > diag)):
                print "findRoute - TIE is best"
                temproute.append([xIndex, yIndex])
                temproute = self.betterRoute(temproute, xIndex, yIndex)
                print "temproute-", temproute
            else:
                print "This shouldnt happen"
        return temproute

    def betterRoute(self, temproute, startX, startY):
        temproute1 = temproute[:]
        print ("better route - routing from: " + str(startX) + "," +
        str(startY))
        route1 = self.findRoute(temproute, startX - 1, startY)
        route2 = self.findRoute(temproute1, startX, startY - 1)
        max1 = self.getMax(route1)
        max2 = self.getMax(route2)
        print "Comparing Route maxes - 1: " + str(max1) + " 2: " + str(max2)
        if (max1 >= max2):
            print "Adding 1", route1
            return route1
        else:
            print "Adding 2", route2
            return route2

    def getMax(self, routeToFindMaxOf):
        print "getMax -", routeToFindMaxOf
        maxScore = 0
        for i in range(0, len(routeToFindMaxOf)):
            x = routeToFindMaxOf[i][0]
            y = routeToFindMaxOf[i][1]
            maxScore += self.alignmentmatrix[x][y].getScore()
        print "getMax -", maxScore, " for route", routeToFindMaxOf
        return maxScore

    def printRoute(self):
        print("printRoute - Length of sequence route is " +
        str(len(self.route)))
        for i in range(0, len(self.route)):
            print("printRoute - x: " + str(self.route[i][0]) + " y: " +
            str(self.route[i][1]))

    def reverseRoute(self):
        revRoute = []
        print "testroute - ", self.route
        for i in range(len(self.route) - 1, -1, -1):
            revRoute.append(self.route[i])
        print"testrev ", revRoute
        self.route = revRoute[:]
        print "reverseRoute - ", self.route

    def createAlignment(self):
        print "seq1 = ", self.seq1
        print "seq2 = ", self.seq2
        self.alseq1 = ""
        self.alseq2 = ""
        for i in range(0, len(self.route) - 1):
            print "1: " + str(self.route[i][0]) + " 2: " + str(self.route[i][1])
            print "v1: " + str(self.route[i + 1][0] - 1) + " v2: " + str(self.
            route[i + 1][1] - 1)
            if (self.route[i][0] == self.route[i + 1][0] - 1):
                print "s1 is adding " + str(self.seq1[self.route[i + 1][0]])
                self.alseq1 += self.seq1[self.route[i + 1][0]]
            elif (self.route[i][0] == self.route[i + 1][0]):
                self.alseq1 += "*"
            else:
                print "idk"
            if (self.route[i][1] == self.route[i + 1][1] - 1):
                print "s2 is adding " + str(self.seq2[self.route[i + 1][1]])
                self.alseq2 += self.seq2[self.route[i + 1][1]]
            elif (self.route[i][1] == self.route[i + 1][1]):
                self.alseq2 += "*"
            else:
                print "idk"
        print "aligned1: ", self.alseq1
        print "aligned2: ", self.alseq2


class score:

    def __init__(self, init):
#        self.s1 = []
#        self.s2 = []
        self.score = init

    def changeScore(self, value):
        self.score = value

    def getScore(self):
        return self.score


dynpro = align_simple()
dynpro.getSequences('./align1', './align2')
dynpro.initMatrix(0)
dynpro.printmatrix()
dynpro.align()
dynpro.printmatrix()
dynpro.sumscore()
dynpro.printmatrix()
dynpro.findRoute(dynpro.route, len(dynpro.alignmentmatrix) - 1,
len(dynpro.alignmentmatrix[0]) - 1)
dynpro.reverseRoute()
dynpro.printmatrix()
dynpro.printRoute()
dynpro.createAlignment()