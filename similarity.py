import sys, time
from xml.dom import minidom
from align2 import align2
from multiprocessing import Pool, Queue
from subprocess import call

def seqGen(sequences,pdbids,x):
  output = []
  for i in xrange(0,x):
    s1 = sequences[i]
    p1 = pdbids[i]
    output.append((p1,s1))
  return output

infile = ""

def main():
  #infile = sys.argv[1]

  outfile = "blah.txt"
  out = open(outfile,'w')

  #blosumfile = sys.argv[3]

  all = False
  print len(sys.argv)
  if len(sys.argv) == 5:
    if sys.argv[4] == 'all':
      all = True

  
  now = time.time()
  p = Pool(4)
  p.map(doSeq,range(0,10))
  print "done" ,time.time()-now



def doSeq(x):
  infile = "input_data_ALL.xml"
  blosumfile = "./blosum62"
  outfile = str(x)+".partialResult"
  xmldoc = minidom.parse(infile)
  
  sequences = xmldoc.getElementsByTagName('SEQUENCE')
  seqList = map(lambda x:x.firstChild.data.encode().strip(),sequences)

  pdbids = xmldoc.getElementsByTagName('PDBID')
  pdbList = map(lambda x:x.firstChild.data.encode().strip(),pdbids)
  
  a = align2(blosumfile)

  pdb1, s1 = pdbList[x], seqList[x]
  
  outline = str(pdb1)+",meta"
  with open(outfile,"w") as fp:
    for i in range(0,x):
      pdb2, s2 = pdbList[i], seqList[i]
      sim = a.align(s1,s2)
      outline+=","+str(pdb2)+","+str(sim)
    fp.write(outline)
  return True

      

  


if __name__ == "__main__":
    main()
