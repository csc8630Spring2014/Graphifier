import numpy as np
import sys, time


MAXSIZE = 501

align = np.ndarray((MAXSIZE,MAXSIZE), dtype='int16')
Talign = np.ndarray((MAXSIZE,MAXSIZE), dtype='int16')
similarity = np.ndarray((MAXSIZE,MAXSIZE), dtype='int32')

align.fill(-9999)
Talign.fill(-9999)
for i in range(0,MAXSIZE):
  align[i,0] = 0
  Talign[0,i] = 0
  align[0,i]=0
  Talign[i,0]= 0

similarity.fill(0)

class align2:

  blosum = {}

  def __init__(self,filename):
    #put code to read from blosum file here
    f = open(filename)
    data = []
    columns = []
    i=0
    for line in f:
      if i == 0:
        columns = line.split()
      else:
        parts = line.split()
        for j in xrange(1,len(parts)):
          data.append((parts[0],columns[j-1],int(parts[j])))
      i=i+1
    f.close()
    for a,b,val in data:
      self.blosum.setdefault(a, {})[b] = val
    """
    print "testing"
    now = time.time()
    for i in range(0,200*200):
      self.blosum["A"]["A"]
    print "done", time.time()-now
    """

  def gap(self,n):
    if n <= 0:
      return 0
    else:
      return -10 + -1*(n-1)

  def align(self, seq1, seq2):
    global align,Talign,similarity
    #initialize the alignment matrix
    #actually, we don't wans to penalize gaps at the beginning, so this code needs to go away
    #for i in xrange(1,len(seq1)+1):
    #  align[0,i] = align[0,i-1] + blosum[seq1[i-1]]['*']
    #for j in xrange(1,len(seq2)+1):
    #  align[j,0] = align[j-1,0] + blosum[seq2[j-1]]['*']
    #initialize the similarity matrix     
    #find the scores and similarities
    for i in xrange(1,len(seq1)+1):
      for j in xrange(1,len(seq2)+1):
        #alignment = min(D_i-1,j-1 + w(a_i,b_j), D_i-1,j + w(a_i,-), D_i,j-1 + w(-,b_j))
        #the alignment scores here are not right because the blosum scores shoudl be subtracted(?) 
        bmatch = self.blosum[seq1[i-1]][seq2[j-1]]
        a = align[i-1,j-1]+bmatch
        
        subcolumn = Talign[j][:i+1]
        colmax = np.argmax(subcolumn)
        coldist = i-colmax
        if j < len(seq2):
          b=align[colmax,j]+self.gap(coldist)
        else:
          b=align[colmax,j]
        #b = align[i-1,j]+self.blosum[seq1[i-1]]['*']
        
        subrow = align[i][:j+1]
        rowmax = np.argmax(subrow)
        rowdist = j-rowmax
        if i < len(seq1):
          c = align[i,rowmax]+self.gap(rowdist)
        else:
          c = align[i,rowmax]
        #c = align[i,j-1]+self.blosum['*'][seq2[j-1]]
        best = max((a,b,c))
        align[i,j] = best
        Talign[j,i] = best    
        #best_score = max(similarity[i-1,j-1],similarity[i-1,j],similarity[i,j-1])
        if best == a:
          similarity[i,j] = similarity[i-1,j-1]+int(bmatch>0)
        elif b >= c:
          similarity[i,j] = similarity[colmax,j]
        else:
          similarity[i,j] = similarity[i,rowmax]
        #similarity
        #a2 = similarity[i-1,j-1] + self.blosum[seq1[i-1]][seq2[j-1]]
        #b2 = similarity[i-1,j]+self.blosum[seq1[i-1]]['*']
        #c2 = similarity[i,j-1]+self.blosum['*'][seq2[j-1]]
        #similarity[i,j] = max((a2,b2,c2))

    #print align
    #print similarity
    #find max similarity
    #maybe this is supposed to just be the bottom-right element
    #print similarity[len(seq1),len(seq2)]
    #print len(seq1)
    #print len(seq2)
    #print ((float(len(seq1)+len(seq2)))/2.0)
    align.fill(-9999)
    Talign.fill(-9999)
    return float(similarity[len(seq1),len(seq2)])/((float(len(seq1)+len(seq2)))/2.0)

#filename = sys.argv[1]
#a = align2(filename)
#print a.align(sys.argv[2],sys.argv[3])
