import sys, time
from xml.dom import minidom
from align2 import align2
from multiprocessing import Process, Queue
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
  NUM_TO_DO = 64
  NUM_OF_PROCESSES = 64
  processes = []
  todo = Queue()
  for i in range(0,NUM_OF_PROCESSES):
    p = Process(target=worker, args=(todo,))
    processes.append(p)
    p.start()
  for i in range(0,NUM_TO_DO):
    todo.put(i)
  for i in range(0,NUM_OF_PROCESSES):
    todo.put(-1) #tell all the processes they are done
  for p in processes:
    p.join()#wait for them all to stop

  print "DONE!",time.time()-now

  os.system("cd partialResults")
  os.system("cat *.partialResult > output.txt")
  

def worker(inQueue):
  infile = "input_data_ALL.xml"
  blosumfile = "./blosum62"
  xmldoc = minidom.parse(infile)
  
  sequences = xmldoc.getElementsByTagName('SEQUENCE')
  seqList = map(lambda x:x.firstChild.data.encode().strip(),sequences)

  pdbids = xmldoc.getElementsByTagName('PDBID')
  pdbList = map(lambda x:x.firstChild.data.encode().strip(),pdbids)
  
  a = align2(blosumfile)

  done = False
  while not done:
    x = inQueue.get(True)
    if x == -1:
      done = True
      break
    else:
      doSeq(x,seqList,pdbList,a)


def doSeq(x,seqList,pdbList,a):
  
  pdb1, s1 = pdbList[x], seqList[x]
  outfile = "partialResults//"+str(x)+".partialResult"
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
