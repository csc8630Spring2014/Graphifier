class align_simple:

    def __init__(self):
        self.alignmentmatrix = []
        self.route = []
        self.similarity = 0
        self.totalscore = -1000000
        self.editDistance = 100000
        self.gap_start_penalty = 10
        self.gap_extend_penalty = 1
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

    ### Starts the beef of the program, it is given the 2 sequences to ###
    ### compare                                                        ###
    def startAlignment(self, sequence1, sequence2):
            self.alignmentmatrix = []
            self.route = []
            self.seq1 = sequence1
            self.seq2 = sequence2
            self.initMatrix(0)
            self.setBlosumScores()
            self.sumscore()
            self.makeRoute()
            self.makeSubArray()
#            print self.subScoreMatrix
            self.reverseRoute()
            self.createAlignment()
#            self.printmatrix()

    ### Will return the edit distance (int) of the two sequences supplied ###
    ### during startMatrix                                               ###
    def getDistance(self):
        totalIdentities = 0
#        print "len 1 = ", len(self.seq1), len(self.alseq1)
#        print "len 2 = ", len(self.seq2), len(self.alseq2)
        ### Checks each index of aliignments for Identity (+1 for positive) ###
        for i in range(0, len(self.alseq1)):
            if (self.alseq1[i] != self.alseq2[i]):
                totalIdentities += 1
#        print "out of length ", len(self.route) + 1, " is ",
        return totalIdentities

    ### Returns the similarity SCORE (int) of the sequences ###
    def getSimilarityScore(self):
        return self.alignmentmatrix[len(self.alignmentmatrix) - 1][len(self.
            alignmentmatrix[0]) - 1].getScore()

    ### Returns the similarity NUMBER (int) of the sequences ###
    def getSimilarityNumber(self):
        return self.similarity

    ### Creates and initializes the matrix elements to 0 ###
    def initMatrix(self, init):
#        print str(len(self.seq1)), str(len(self.seq2))
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
#        self.printmatrix()

    ### Prints the whole alignment matrix ###
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

#    def get(self, i, j):
#        return self.alignmentmatrix[i][j]

#    def put(self, i, j, value):
#        self.alignmentmatrix[i][j] = value

    ### Converts 0 initialized matrix to a substitution matrix based on ###
    ### blosum62                                                       ###
    def setBlosumScores(self):
        for i in range(1, len(self.seq1) + 1):
            for j in range(1, len(self.seq2) + 1):
#                print (str(self.scoreIndex[self.
#                seq1[i - 1]]) + " & " + str(self.scoreIndex[self.seq2[j-1]]))
#                print str(self.blosum62[self.scoreIndex[self.seq1[i - 1]]]
#                [self.scoreIndex[self.seq2[j - 1]]])
                temp = self.blosum62[self.scoreIndex[self.seq1[i - 1]]][self.
                scoreIndex[self.seq2[j - 1]]]
#                print (temp, self.alignmentmatrix[i][j].getScore())
                self.alignmentmatrix[i][j].changeScore(temp, [- 1. - 1])
#                print self.alignmentmatrix[i][j].getScore()
#        self.printmatrix()

    ### Returns the calculated gap penalty based on size of gap given ###
    ### by length                                                       ###
    def getPenalty(self, length):
        if (length == 0):
            return 0
        else:
            return self.gap_start_penalty + self.gap_extend_penalty * (
                length - 1)

    ### Will calculate the maximum possible origin that the score at the
    ### current element could come from, yIndex and xIndex set the start
    ### point in the alignment matrix to start at and direction tells it which
    ### direction to check the max of
    def getMax(self, yIndex, xIndex, direction):
        maxVal = -1000000
        origin = {}
        ###Used to track distance from starting point
        tempcounter = 1
        penalty = 0
        if (direction == 'up'):
            ### Goes until it reaches the upper edge of the matrix
            while(yIndex - tempcounter >= 0):
#                print "up y:", yIndex, " temp: ", tempcounter, " X:", xIndex
                ### Will add a penalty if a gap is encountered
                if (xIndex != len(self.seq2)):
                    penalty = self.getPenalty(tempcounter)
                ### Will not add a gap penalty if it is a tail gap
                else:
                    penalty = 0
#                    print "Penalty: ", penalty
                uptotal = self.alignmentmatrix[yIndex - tempcounter][
                    xIndex].getScore() - penalty
                ### If new max value has been found then it will be
                ### applied as the current max value
                if(uptotal >= maxVal):
                    maxVal = uptotal
                    origin = [yIndex - tempcounter, xIndex]
#                    print "NEW MAX:", maxVal, " from ", origin
                tempcounter += 1
        elif(direction == 'left'):
            ### Will evaluate all entries until left matrix edge is encountered
            while(xIndex - tempcounter >= 0):
#                print "left y", yIndex, " temp:", tempcounter, " X:", xIndex
                ### Adds a gap penalty
                if (yIndex != len(self.seq1)):
                    penalty = self.getPenalty(tempcounter)
                ### Does not add a penalty if it is a tail gap
                else:
                    penalty = 0
#                    print "Penalty: ", penalty
                lefttemp = self.alignmentmatrix[yIndex][
                xIndex - tempcounter].getScore() - penalty
                ### If a new max value is found, it is assigned as
                ### the current max
                if(lefttemp >= maxVal):
                    maxVal = lefttemp
                    origin = [yIndex, xIndex - tempcounter]
#                    print "NEW MAX:", maxVal
                tempcounter += 1
#        print "exiting max", maxVal
        package = [maxVal, origin]
        return package

    ### Will go element by element in the alignment matrix and find the max
    ### value obtained in the diagonal, upwards, and left directions, placing
    ### the highest of the three in to the element
    def sumscore(self):
        ### Inspect each element in Sequence 1
        for h in range(1, len(self.alignmentmatrix)):
            ### Inspect each element in Sequence 2
            for k in range(1, len(self.alignmentmatrix[0])):
#                print "Checking at " + str(h) + " " + str(k)
                currentScore = self.alignmentmatrix[h][k].getScore()
                oldScore = self.alignmentmatrix[h - 1][k - 1].getScore()
#                print "!", old
                # a is diag, b is up, c is left direction max scores
                a = oldScore + currentScore
                b = self.getMax(h, k, 'up')
                c = self.getMax(h, k, 'left')
#                print "diag",a," s", temp, " d", old, " u", b[0], " l:", c[0]
                ### If the Diagonal Score is greater than or equal ###
                ### to up and down                               ###
                if ((a >= b[0]) and (a >= c[0])):
#                    print "Diag wins"
                    self.alignmentmatrix[h][k].changeScore(a, [h - 1, k - 1])
                ### If the Up Score is greater than diagonal and left ###
                elif (b[0] > a) and (b[0] > c[0]):
#                    print "Above wins"
                    self.alignmentmatrix[h][k].changeScore(b[0], [b[1][0],
                    b[1][1]])
                ### If the left score is greater than diagonal and up score
                elif (c[0] > a) and (c[0] > b[0]):
#                    print "left wins"
                    self.alignmentmatrix[h][k].changeScore(c[0], [c[1][0],
                    c[1][1]])
                ### If left and up tie AND are bigger than the diagonal
                else:
                    ### Will insert the gap in seq1 if it is shorter
                    if(len(self.seq1) > len(self.seq2)):
                        self.alignmentmatrix[h][k].changeScore(b[0], [b[1][0],
                        b[1][1]])
                    ### Will insert the gap in seq2 if it is shorter
                    elif(len(self.seq1) > len(self.seq2)):
                        self.alignmentmatrix[h][k].changeScore(c[0], [c[1][0],
                        c[1][1]])
                    ### If sequence lengths are the same, it will now sort
                    ### by alphabetical order
                    else:
                        alphaList = [self.seq1, self.seq2]
                        sorted(alphaList)
                        ### Will insert gap in seq1 if it is 1st alphabetically
                        if(alphaList[0] == self.seq1):
                            self.alignmentmatrix[h][k].changeScore(b[0],
                            [b[1][0], b[1][1]])
                        ### Will insert a gap in seq2 if it is 1st alphabetic
                        else:
                            self.alignmentmatrix[h][k].changeScore(c[0],
                            [c[1][0], c[1][1]])
#                self.printmatrix()
#        self.printmatrix()

    ### Will create a list of the order of traversal in the matrix to create
    ### the optimum global alignment
    def makeRoute(self):
        y = len(self.alignmentmatrix) - 1
        x = len(self.alignmentmatrix[0]) - 1
        routeIndex = [y, x]
        ### Will start at the bottom right node and add its origin variable
        ### to the route list, then goes to that element and adds it origin
        ### variable and so on until it reaches [0,0]
        while((y >= 0) and (x >= 0)):
#            print routeIndex
            self.route.append(routeIndex)
            routeIndex = self.alignmentmatrix[y][x].getOrigin()
            y = routeIndex[0]
            x = routeIndex[1]

    ### Will create a list of the original substitution scores matched from the
    ### route created.
    def makeSubArray(self):
        self.subScoreMatrix = []
#        print len(self.route), "length of route"
        ### Looks at and adds the original sub score score of each element
        ### of the route
        for i in range(len(self.route) - 1, -1, -1):
#            print self.route[i], self.alignmentmatrix[self.
#            route[i][0]][self.route[i][1]].getBase()
            self.subScoreMatrix.append(self.alignmentmatrix[self.
            route[i][0]][self.route[i][1]].getBase())

    ### A quick way to print the full route of the alignment ###
    def printRoute(self):
        print("printRoute - Length of sequence route is " +
        str(len(self.route)))
        for i in range(0, len(self.route)):
            print("printRoute - x: " + str(self.route[i][0]) + " y: " +
            str(self.route[i][1]))

    ### Will just take the elements of the route and reverse their order ###
    def reverseRoute(self):
        revRoute = []
#        print "testroute - ", self.route
        for i in range(len(self.route) - 1, -1, -1):
            revRoute.append(self.route[i])
#        print"testrev ", revRoute
        self.route = revRoute[:]
#        print "reverseRoute - ", self.route

    ### Will create the alignment from the route calculated   ###
    def createAlignment(self):
#        print "seq1 = ", self.seq1
#        print "seq2 = ", self.seq2
        self.alseq1 = ""
        self.alseq2 = ""
#        print self.route
        ###
        for i in range(1, len(self.route)):
#            print i
#            print self.route
#            print self.route[i - 1]
#            print self.route[i]
#            print "1: " + str(self.route[i][0]) +" 2: "+str(self.route[i][1])
#            print "v1: " + str(self.route[i - 1][0] + 1) +" v2: "+str(self.
#            route[i - 1][1] + 1)
            xChange = self.route[i][1] - self.route[i - 1][1]
            yChange = self.route[i][0] - self.route[i - 1][0]
#            print "Xchange: ", xChange, "Ychange: ", yChange
#            print self.alseq1
#            print self.alseq2
            if (yChange == 1) and (xChange == 1):
                self.alseq1 += self.seq1[self.route[i - 1][0]]
                self.alseq2 += self.seq2[self.route[i - 1][1]]
                if (self.subScoreMatrix[i] > 0):
                    self.similarity += 1
            elif(yChange > 0) and (xChange == 0):
                if (self.route[i - 1][0] == 0):
                    newSeq1Index = 0
                else:
                    newSeq1Index = self.route[i - 1][0]
#                print "yChange!"
#                print "Adding ", self.seq1[newSeq1Index:
#                newSeq1Index + yChange], " to 1"
#                print "Adding ", "*" * yChange, " to 2"
                self.alseq2 += ("*" * yChange)
                if (i == len(self.route) - 1):
                    yChange += 1
                self.alseq1 += self.seq1[newSeq1Index:
                newSeq1Index + yChange]
            elif(xChange > 0) and (yChange == 0):
                if (self.route[i - 1][1] == 0):
                    newSeq2Index = 0
                else:
                    newSeq2Index = self.route[i - 1][1]
#                print "xChange"
#                print "Adding ", "*" * xChange, " to 1"
#                print "Adding ", self.seq2[newSeq2Index:
#                newSeq2Index + xChange], " to 2"
                self.alseq1 += ("*" * xChange)
                if (i == len(self.route) - 1):
                    xChange += 1
                self.alseq2 += self.seq2[newSeq2Index:newSeq2Index + xChange]
            else:
                print ("Weirdness in the alignment")
#            print "1: ", self.alseq1
#            print "2: ", self.alseq2
        print self.alseq1
        print self.alseq2


class score:

    def __init__(self):
        self.value = 0
        self.base = 0
        self.parent = [-1, -1]
        self.gapNum = 0

    def changeScore(self, newValue, origination):
        self.base = self.value
        self.value = newValue
        self.parent = origination

    def getScore(self):
        return self.value

    def getOrigin(self):
        return self.parent

    def getBase(self):
        return self.base

    def giveOrigin(self, origination):
        self.parent = origination

    def getGaps(self):
        return self.gapNum


dynpro = align_simple()
dynpro.startAlignment(
    "SMTDLLSAEDIKKAIGAFTAADSFDHKKFFQMVGLKKKSADDVKKVFHILDKDKDGFIDEDELGSILKGFSSDARDLSAKETKTLMAAGDKDGDGKIGVEEFSTLVAES",
    "GSHMFMPSDRSTERCETVLEGETISCFVVGGEKRLCLPQILNSVLRDFSLQQINAVCDELHIYCSRCTADQLEILKVMGILPFSAPSCGLITKTDAERLCNALLYG")
print "Score ", dynpro.getDistance()
print "Similarity Score: ", dynpro.getSimilarityScore()
print "Similarity Number: ", dynpro.getSimilarityNumber()
