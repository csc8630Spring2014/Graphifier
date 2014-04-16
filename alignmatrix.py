class alignMatrix(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.vals = [None]*(width*height)
    def getloc(self,x,y):
        return self.width*x + y

    def put(self,val,x,y):
        self.vals[self.getloc(x,y)] = val

    def get(self,x,y):
        return self.vals[self.getloc(x,y)]

    def MaxCol(self,x,y):
        collocs = [(j,y) for j in range(0,y)]
        colMax = max(collocs, key=lambda x: self.get(*x))
        colVal = self.get(*colMax)
        return colMax[0],colVal

    def MaxRow(self,x,y):
        rowlocs = [(x,j) for j in range(0,x)]
        rowMax = max(rowlocs, key=lambda x: self.get(*x))
        rowVal = self.get(*rowMax)
        return rowMax[1],rowVal



def align(self, seq1, seq2): #get alignment score of 2 seqs
    align = alignMatrix(len(seq1)+1,len(seq2)+1) #score at points
    score = alignMatrix(len(seq1)+1,len(seq2)+1) #cumulative score
    for i in xrange(1,len(seq1)+1):
        for j in xrange(1,len(seq2)+1):
            bmatch = self.blosum[seq1[i-1]][seq2[j-1]] 
            diagonal_match = align.get(i-1,j-1)+bmatch
            colmaxLoc, colMax = align.MaxCol(i,j)
            col_match = colMax + self.gap(i-colmaxLoc)

            rowmaxLoc, rowMax = self.MaxRow(i,j)
            row_match = rowMax + self.gap(i-rowmaxLoc)

            best = max((diagonal_match, col_match, row_match))
            ParentScore = max((score.get(i-1,j-1),score.get(i,j-1),score.get(i,j-1)))
            align.put(best,i,j)
            score.put(best+ParentScore,i,j)
    return float(similarity.get(len(seq1),len(seq2)))/((float(len(seq1)+len(seq2)))/2.0)