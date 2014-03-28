class align_simple:

    def __init__(self):
        self.alignmentmatrix = []
        self.route = []
        self.scoreIndex = {'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5,
            'E': 6, 'G': 7, 'H': 8, 'I': 9, 'L': 10, 'K': 11, 'M': 12, 'F': 13,
            'P': 14, 'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19, 'B': 20,
            'Z': 21, 'X': 22, '*': 23}
        self.scores = [[4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2,
            -1, 1, 0, -3, -2, 0, -2, -1, 0, -4], [1, 5, 0, -2, -3, 1, 0,
            -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1, -4], [
            2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3,
            3, 0, -1, -4], [-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1,
            -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1, -4], [0, -3, -3, -3, 9,
             -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3,
            -2, -4], [-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1,
            0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1, -4], [-1, 0, 0, 2, -4, 2,
            5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4],
            [0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2,
            -2, -3, -3, -1, -2, -1, -4], [-2, 0, 1, -1, -3, 0, 0, -2, 8, -3,
            -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1, -4], [-1, -3, -3,
            -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3,
            -3, -1, -4], [-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0,
            -3, -2, -1, -2, -1, 1, -4, -3, -1, -4], [-1, 2, 0, -1, -3, 1, 1,
            -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1, -4],
            [-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1,
            -1, 1, -3, -1, -1, -4], [-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0,
            -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1, -4], [-1, -2, -2, -1,
            -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2,
            -1, -2, -4], [1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1,
            4, 1, -3, -2, -2, 0, 0, 0, -4], [0, -1, 0, -1, -1, -1, -1, -2, -2,
            -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0, -4], [-3, -3,
            -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2,
            -3, -4, -3, -2, -4], [-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1,
            -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1, -4], [0, -3, -3, -3,
            -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2,
            -1, -4], [-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0,
            -1, -4, -3, -3, 4, 1, -1, -4], [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3,
            -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4], [0, -1, -1,
            -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1,
            -1, -1, -1, -4], [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,
            -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 1]]

    def startAlignment(self, sequence1, sequence2):
            self.alignmentmatrix = []
            self.route = []
            self.seq1 = sequence1
            self.seq2 = sequence2
            self.initMatrix(0)
            self.match()
            self.sumscore()
            self.route = self.findRoute(self.route,
            len(self.alignmentmatrix) - 1,
            len(self.alignmentmatrix[0]) - 1)
            self.reverseRoute()
            self.printmatrix()
            self.printRoute()
            self.createAlignment()

    def initMatrix(self, init):
        start_score = score(0)
        print str(len(self.seq1)), str(len(self.seq2))
        for char1 in range(0, len(self.seq1) + 1):
#            print("new x")
            tempList = []
            for char2 in range(0, len(self.seq2) + 1):
#                print("new y")
                tempList.append(start_score)
            self.alignmentmatrix.append(tempList)
        self.printmatrix()

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

    def match(self):
        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
                tempScore = score(self.
                    scores[self.scoreIndex[self.seq1[i - 1]]][self.
                    scoreIndex[self.seq2[j - 1]]])
                self.put(i, j, tempScore)


                #tempScore = score(self.alignmentmatrix[i][j].getScore())
                #if (self.seq1[i: i + 1] == self.seq2[j: j + 1]):
                #    tempScore = score('M')
                #    self.put(i, j, tempScore)
                #else:


    def sumscore(self):
        for h in range(1, len(self.alignmentmatrix)):
            for k in range(1, len(self.alignmentmatrix[0])):
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
        for h in range(y, len(self.alignmentmatrix) + 1):
            for k in range(x, len(self.alignmentmatrix[0]) + 1):
                if (h == y) and (k == x):
                    self.alignmentmatrix[h][k] = score(new)
                elif (self.alignmentmatrix[h][k].getScore() != 'M'):
                    self.alignmentmatrix[h][k] = score(new)
#                    print "changed" + str(k) + " " + str(h) + " to " + str(
#                    new) + " actual value: " + str(
#                    self.alignmentmatrix[h][k].getScore())
        print "sumAfter - End sumAfter"
        self.printmatrix()

    def findRoute(self, tempFoundRoute, xIndex, yIndex):
        tempScore = self.alignmentmatrix[xIndex][yIndex].getScore()
        print "findRoute - ", xIndex, yIndex
        if ((xIndex == 0) and (yIndex == 0)):
            print "findroute - 0,0"
            tempFoundRoute.append([0, 0, tempScore, 'S'])
        elif (xIndex == 0):
            print "findRoute - 0,y"
            tempFoundRoute.append([xIndex, yIndex, tempScore, 'H'])
            tempFoundRoute = (self.findRoute(tempFoundRoute,
            xIndex, yIndex - 1))
        elif (yIndex == 0):
            print"findRoute - x,0"
            tempFoundRoute.append([xIndex, yIndex, tempScore, 'V'])
            tempFoundRoute = (self.findRoute(tempFoundRoute,
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
                tempFoundRoute.append([xIndex, yIndex, tempScore, 'H'])
                tempFoundRoute = self.findRoute(tempFoundRoute,
                xIndex, (yIndex - 1))
            elif ((above > left) and (above > diag)):
                print ("findRoute - ABOVE is best, adding [" + str(xIndex) +
                "," + str(yIndex - 1) + "]")
                tempFoundRoute.append([xIndex, yIndex, tempScore, 'V'])
                tempFoundRoute = self.findRoute(tempFoundRoute,
                (xIndex - 1), yIndex)
            elif ((diag >= left) and (diag >= above)):
                print ("findRoute - DIAG is best, adding [" + str(xIndex - 1) +
                "," + str(yIndex - 1) + "]")
                tempFoundRoute.append([xIndex, yIndex, tempScore, 'D'])
                tempFoundRoute = self.findRoute(tempFoundRoute,
                (xIndex - 1), (yIndex - 1))
            elif ((above == left) and (above > diag)):
                print "findRoute - TIE is best"
                tempFoundRoute.append([xIndex, yIndex, tempScore, 'T'])
                tempFoundRoute = self.betterRoute(tempFoundRoute, xIndex,
                yIndex)
                print "tempFoundRoute-", tempFoundRoute
            else:
                print "This shouldnt happen"
        print "returning ************", tempFoundRoute
        return tempFoundRoute

    def betterRoute(self, tempBetterRoute, startX, startY):
        BetterRoute = tempBetterRoute[:]
        print ("better route - routing from: " + str(startX) + "," +
        str(startY))
        route1 = self.findRoute(tempBetterRoute, startX - 1, startY)
        route2 = self.findRoute(BetterRoute, startX, startY - 1)
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
        for i in range(len(self.route) - 1, 0, -1):
            print i
            print "1: " + str(self.route[i][0]) + " 2: " + str(self.route[i][1])
            print "v1: " + str(self.route[i - 1][0] + 1) + " v2: " + str(self.
            route[i - 1][1] + 1)
            if ((self.route[i][0] == 0) and (self.route[i][1] == 0)):
                break
            elif (self.route[i][0] == self.route[i - 1][0] + 1):
                print "s1 is adding " + str(self.seq1[self.route[i][0] - 1])
                self.alseq1 = self.seq1[self.route[i][0] - 1] + self.alseq1
            elif (self.route[i][0] == self.route[i - 1][0]):
                self.alseq1 = "*" + self.alseq1
            else:
                print "idk"
            if (self.route[i][1] == self.route[i - 1][1] + 1):
                print "s2 is adding " + str(self.seq2[self.route[i][1] - 1])
                self.alseq2 = self.seq2[self.route[i][1] - 1] + self.alseq2
            elif (self.route[i][1] == self.route[i - 1][1]):
                self.alseq2 = "*" + self.alseq2
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
dynpro.startAlignment("GACTTAC", "CGTGAATTCAT")
