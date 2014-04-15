import numpy as np
import sys

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

  def gap(self,n):
    if n <= 0:
      return 0
    else:
      return -10 + -1*(n-1)

  def align(self, seq1, seq2):
    #initialize the alignment matrix
    align = np.ndarray((len(seq1)+1,len(seq2)+1), dtype='int32')
    align.fill(0)
    #actually, we don't wans to penalize gaps at the beginning, so this code needs to go away
    #for i in xrange(1,len(seq1)+1):
    #  align[0,i] = align[0,i-1] + blosum[seq1[i-1]]['*']
    #for j in xrange(1,len(seq2)+1):
    #  align[j,0] = align[j-1,0] + blosum[seq2[j-1]]['*']
    #initialize the similarity matrix 
    similarity = np.ndarray((len(seq1)+1,len(seq2)+1), dtype='int32')
    similarity.fill(0) 
    #find the scores and similarities
    for i in xrange(1,len(seq1)+1):
      for j in xrange(1,len(seq2)+1):
        #alignment = min(D_i-1,j-1 + w(a_i,b_j), D_i-1,j + w(a_i,-), D_i,j-1 + w(-,b_j))
        #the alignment scores here are not right because the blosum scores shoudl be subtracted(?) 
        bmatch = self.blosum[seq1[i-1]][seq2[j-1]]
        a = align[i-1,j-1]+bmatch
        
        subcolumn =align[:,j][:i+1]
        colmax = np.argmax(subcolumn)
        coldist = i-colmax
        if j < len(seq2):
          b=align[colmax,j]+self.gap(coldist)
        else:
          b=align[colmax,j]
        #b = align[i-1,j]+self.blosum[seq1[i-1]]['*']
        
        subrow = align[i,:][:j+1]
        rowmax = np.argmax(subrow)
        rowdist = j-rowmax
        if i < len(seq1):
          c = align[i,rowmax]+self.gap(rowdist)
        else:
          c = align[i,rowmax]
        #c = align[i,j-1]+self.blosum['*'][seq2[j-1]]
        if a > b and a > c:
          align[i,j] = a
          if bmatch > 0:
            similarity[i,j] = similarity[i-1,j-1] +1
          else:
            similarity[i,j] = similarity[i-1,j-1]
        else:
          if b > c:
            align[i,j] = b
            similarity[i,j] = similarity[colmax,j]
          elif c > b:
            align[i,j] = c
            similarity[i,j] = similarity[i,rowmax]  
          else:
            if len(seq1) < len(seq2):
              align[i,j] = c
              similarity[i,j] = similarity[i,rowmax]
            elif len(seq2) < len(seq1):
              align[i,j] = b
              similarity[i,j] = similarity[colmax,j]
            else:
              sl = sorted([seq1,seq2])
              if seq1 == sl[0]:
                align[i,j] = b
                similarity[i,j] = similarity[colmax,j]
              else:
                align[i,j] = c
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
    return float(similarity[len(seq1),len(seq2)])/((float(len(seq1)+len(seq2)))/2.0)

#filename = sys.argv[1]
#a = align2(filename)
#print a.align(sys.argv[2],sys.argv[3])
