class align_simple:

    def __init__(self):
        self.alignmentmatrix = []
        self.route = []
        self.totalscore = -1000000
        self.editDistance = 100000
        self.gap_start_penalty = 10
        self.gap_e_pen = 1
        self.scoreIndex = {'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5,
            'E': 6, 'G': 7, 'H': 8, 'I': 9, 'L': 10, 'K': 11, 'M': 12, 'F': 13,
            'P': 14, 'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19, 'B': 20,
            'Z': 21, 'X': 22, '*': 23}
        self.blosum62 = [[4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2,
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
            self.setBlosumScores()
            self.sumscore()
            self.findMax()
            self.makeRoute()
            self.reverseRoute()
            self.createAlignment()

    def getDistance(self):
        temp = 0
        for i in range(0, len(self.alseq1)):
            if (self.alseq1[i] != self.alseq2[i]):
                temp += 1
        return temp

    def getSimilarityScore(self):
        return self.alignmentmatrix[len(self.alignmentmatrix) - 1][len(self.
            alignmentmatrix[0]) - 1].getScore()

    def initMatrix(self, init):
###        print str(len(self.seq1)), str(len(self.seq2))
        for y in range(0, len(self.seq1) + 1):
            tempList = []
            for x in range(0, len(self.seq2) + 1):
                start_score = score()
                if(y == 0) and (x != 0):
                    start_score.giveOrigin([y, x - 1])
                elif(y != 0) and (x == 0):
                    start_score.giveOrigin([y - 1, x])
                tempList.append(start_score)
            self.alignmentmatrix.append(tempList)
###        self.printmatrix()

    def printmatrix(self):
        for char1 in range(0, len(self.alignmentmatrix)):
            print "[",
            for char2 in range(0, len(self.alignmentmatrix[char1])):
                if(char2 == 0) and (char1 != 0):
                    print self.seq1[char1 - 1] + " ",
                elif(char1 == 0) and (char2 != 0):
                    print self.seq2[char2 - 1] + " ",
                else:
                    print str(self.alignmentmatrix[char1][char2].
                    getScore()) + " ",
            print("]")
        print "\n"

    def get(self, i, j):
        return self.alignmentmatrix[i][j]

    def put(self, i, j, value):
        self.alignmentmatrix[i][j] = value

    def setBlosumScores(self):
        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
###                print (str(self.scoreIndex[self.
###                seq1[i - 1]]) + " & " + str(self.scoreIndex[self.seq2[j-1]]))
###                print str(self.blosum62[self.scoreIndex[self.seq1[i - 1]]]
###                [self.scoreIndex[self.seq2[j - 1]]])
                temp = self.blosum62[self.scoreIndex[self.seq1[i - 1]]][self.
                scoreIndex[self.seq2[j - 1]]]
###                print (temp, self.alignmentmatrix[i][j].getScore())
                self.alignmentmatrix[i][j].changeScore(temp, [- 1. - 1])
###                print self.alignmentmatrix[i][j].getScore()
###        self.printmatrix()

    def getPenalty(self, length):
        if (length == 0):
            return 0
        elif(length == 1):
            return self.gap_start_penalty
        else:
            return self.gap_start_penalty + self.gap_e_pen * (length - 1)

    def getMax(self, yIndex, xIndex, direction):
        maxVal = -1000000
        origin = {}
        tempcounter = 1
        penalty = 0
        if (direction == 'up'):
            while(yIndex - tempcounter >= 0):
###                print "up y:", yIndex, " temp: ", tempcounter, " X:", xIndex
#                if (yIndex != len(self.seq1)):             End Gap removal
#                   if (xIndex != len(self.seq2)):          *****************
                penalty = self.getPenalty(tempcounter)
###                print "Penalty: ", penalty
                uptotal = self.alignmentmatrix[yIndex - tempcounter][
                    xIndex].getScore() - penalty
                if(uptotal > maxVal):
                    maxVal = uptotal
                    origin = [yIndex - tempcounter, xIndex]
###                    print "NEW MAX:", maxVal, " from ", origin
                elif(uptotal == maxVal):
                    print "*** There is a getMax equality upwards ***"
                tempcounter += 1
        elif(direction == 'left'):
            while(xIndex - tempcounter >= 0):
###                print "left y", yIndex, " temp:", tempcounter, " X:", xIndex
                lefttemp = self.alignmentmatrix[yIndex][
                xIndex - tempcounter].getScore() - self.getPenalty(tempcounter)
                if(lefttemp > maxVal):
                    maxVal = lefttemp
                    origin = [yIndex, xIndex - tempcounter]
###                    print "NEW MAX:", maxVal
                elif(lefttemp == maxVal):
                    print "*** There is a match during getMax left ***"
                tempcounter += 1
###        print "exiting max", maxVal
        package = [maxVal, origin]
        return package

    def sumscore(self):
        for h in range(1, len(self.alignmentmatrix)):
            for k in range(1, len(self.alignmentmatrix[0])):
###                print "Checking at " + str(h) + " " + str(k)
                temp = self.alignmentmatrix[h][k].getScore()
                old = self.alignmentmatrix[h - 1][k - 1].getScore()
###                print "!", old
                a = old + temp
                b = self.getMax(h, k, 'up')
                c = self.getMax(h, k, 'left')
###                print "diag",a," s", temp, " d", old, " u", b[0], " l:", c[0]
                if ((a >= b[0]) and (a >= c[0])):
###                    print "Diag wins"
                    self.alignmentmatrix[h][k].changeScore(a, [h - 1, k - 1])
                elif (b[0] > a) and (b[0] > c[0]):
###                    print "Above wins"
                    self.alignmentmatrix[h][k].changeScore(b[0], [b[1][0],
                    b[1][1]])
                elif (c[0] > a) and (c[0] > b[0]):
###                    print "left wins"
                    self.alignmentmatrix[h][k].changeScore(c[0], [c[1][0],
                    c[1][1]])
                else:
                    print "Fix Tie-Breaker"
###                self.printmatrix()
###        self.printmatrix()

    def findMax(self):
        biggestValue = -100000
        startIndex = [0, 0]
        for y in range(1, len(self.alignmentmatrix)):
            for x in range(1, len(self.alignmentmatrix[y])):
                if(self.alignmentmatrix[y][x].getScore() >= biggestValue):
###                    temp = self.alignmentmatrix[y][x].getScore()
###                    print "Biggest: ", biggestValue, " vs ", temp
                    biggestValue = self.alignmentmatrix[y][x].getScore()
                    startIndex = [y, x]
        return startIndex

    def makeRoute(self):
        y = len(self.alignmentmatrix) - 1
        x = len(self.alignmentmatrix[0]) - 1
        routeIndex = [y, x]
        while((y >= 0) and (x >= 0)):
###            print routeIndex
            self.route.append(routeIndex)
            routeIndex = self.alignmentmatrix[y][x].getOrigin()
            y = routeIndex[0]
            x = routeIndex[1]

    def printRoute(self):
        print("printRoute - Length of sequence route is " +
        str(len(self.route)))
        for i in range(0, len(self.route)):
            print("printRoute - x: " + str(self.route[i][0]) + " y: " +
            str(self.route[i][1]))

    def reverseRoute(self):
        revRoute = []
###        print "testroute - ", self.route
        for i in range(len(self.route) - 1, -1, -1):
            revRoute.append(self.route[i])
###        print"testrev ", revRoute
        self.route = revRoute[:]
###        print "reverseRoute - ", self.route

    def createAlignment(self):
        print "seq1 = ", self.seq1
        print "seq2 = ", self.seq2
        self.alseq1 = ""
        self.alseq2 = ""
        for i in range(len(self.route) - 1, 0, -1):
###            print i
###            print self.route
###            print "1: " + str(self.route[i][0]) +" 2: "+str(self.route[i][1])
###            print "v1: " + str(self.route[i - 1][0] + 1) +" v2: "+str(self.
###            route[i - 1][1] + 1)
            if ((self.route[i][0] == 0) and (self.route[i][1] == 0)):
                break
            elif (self.route[i][0] == self.route[i - 1][0] + 1):
###                print "s1 is adding " + str(self.seq1[self.route[i][0] - 1])
                self.alseq1 = self.seq1[self.route[i][0] - 1] + self.alseq1
            elif (self.route[i][0] == self.route[i - 1][0]):
                self.alseq1 = "*" + self.alseq1
            else:
                print "idk"
            if (self.route[i][1] == self.route[i - 1][1] + 1):
###                print "s2 is adding " + str(self.seq2[self.route[i][1] - 1])
                self.alseq2 = self.seq2[self.route[i][1] - 1] + self.alseq2
            elif (self.route[i][1] == self.route[i - 1][1]):
                self.alseq2 = "*" + self.alseq2
            else:
                print "idk"
        print "aligned1: ", self.alseq1
        print "aligned2: ", self.alseq2


class score:

    def __init__(self):
        self.value = 0
        self.parent = [-1, -1]
        self.gapNum = 0

    def changeScore(self, newValue, origination):
        self.value = newValue
        self.parent = origination

    def getScore(self):
        return self.value

    def getOrigin(self):
        return self.parent

    def giveOrigin(self, origination):
        self.parent = origination

    def getGaps(self):
        return self.gapNum


dynpro = align_simple()
dynpro.startAlignment("ASDCWVE", "ADVE")
print "Score: ", dynpro.getDistance()
print "Similarity: ", dynpro.getSimilarityScore()
