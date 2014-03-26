import re
import sys

def main():
  infile = sys.argv[1]
  in1 = open(infile, 'r')
  in2 =open(infile, 'r')

  outfile = sys.argv[2]
  out = open(outfile,'w')

  comment = ''
  seq = ''

  for line in in1:
    #if the line is a sequence
    if re.search("^[A-Z]", line) is not None:
      seq = line
    else 
      comment = line
      
  
if __name__ == "__main__":
    main()


      

  
