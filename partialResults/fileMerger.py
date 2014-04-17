
outfile = "out.csv"
with open(outfile,"w") as out:
        for i in xrange(0,2400)
                chunkfile = str(i)+".partialResult"
                try:
                        with open(chunkfile) as fp:
                                out.write(fp.read())
                        out.write("\n")
                except Exception:
                        break