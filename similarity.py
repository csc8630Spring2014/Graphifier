import sys
from xml.dom import minidom
from align2 import align2

def main():
  infile = sys.argv[1]

  outfile = sys.argv[2]
  out = open(outfile,'w')

  blosumfile = sys.argv[3]

  all = False
  print len(sys.argv)
  if len(sys.argv) == 5:
    if sys.argv[4] == 'all':
      all = True

  xmldoc = minidom.parse(infile)
  
  sequences = xmldoc.getElementsByTagName('SEQUENCE')
  pdbids = xmldoc.getElementsByTagName('PDBID')

  a = align2(blosumfile)

  i = 0
  for i in xrange(len(sequences)):
    out.write(pdbids[i].firstChild.data.encode().strip())
    out.write(',meta')
    s1 = sequences[i].firstChild.data.encode().strip()
    for j in xrange(len(sequences)):
      if all is False:
        if i != j:
          s2 = sequences[j].firstChild.data.encode().strip()
          sim = a.align(s1,s2)
          #print 'sim = ', sim
          if sim > 0.1:
            pdbid2 = pdbids[j].firstChild.data.encode().strip()
            out.write(',') 
            out.write(pdbid2) 
            out.write(',') 
            out.write(str(sim))
      else:
        s2 = sequences[j].firstChild.data.encode().strip()
        sim = a.align(s1,s2)
        pdbid2 = pdbids[j].firstChild.data.encode().strip()
        out.write(',') 
        out.write(pdbid2) 
        out.write(',')
        out.write(str(sim))
    out.write('\n')
  out.flush()
  out.close()

if __name__ == "__main__":
    main()


      

  
