class preScreen:

    def __init__(self):
        self.sequence1 = ""
        self.sequence2 = ""
        self.seq1counts = []
        self.seq2counts = []
        self.scoreIndex = {'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5,
            'E': 6, 'G': 7, 'H': 8, 'I': 9, 'L': 10, 'K': 11, 'M': 12, 'F': 13,
            'P': 14, 'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19, 'B': 20,
            'Z': 21, 'X': 22}

    ### Will take two sequences in and creates an empty array for the counts
    ### and will call the fillArray function to fiill in the couns of each acid
    def setSequences(self, newSeq1, newSeq2):
        self.sequence1 = newSeq1
        self.sequence2 = newSeq2
        for i in range(24):
            self.seq1counts.append(0)
            self.seq2counts.append(0)
        self.fillArray()

    ### Initializes the 2 arrays to hold the counts of each amino acid
    ### and then fills them in
    def fillArray(self):
        print len(self.sequence1), len(self.sequence2)
        for i in range(0, len(self.sequence1)):
#            print i, " in 1"
            index = self.sequence1[i]
            acid = self.scoreIndex.get(index)
            self.seq1counts[acid] += 1
        for i in range(0, len(self.sequence2)):
#            print i, " in 2"
            index = self.sequence2[i]
            acid = self.scoreIndex.get(index)
            self.seq2counts[acid] += 1

    def compareArrays(self):
        #insert comparison style here
        1


screener = preScreen()
screener.setSequences("SMTDLLSAEDIKKAIGAFTAADSFDHKKFFQMVGLKKKSADDVKKVFHILDKDKDGFIDEDELGSILKGFSSDARDLSAKETKTLMAAGDKDGDGKIGVEEFSTLVAES",
    "GSHMFMPSDRSTERCETVLEGETISCFVVGGEKRLCLPQILNSVLRDFSLQQINAVCDELHIYCSRCTADQLEILKVMGILPFSAPSCGLITKTDAERLCNALLYG")
print screener.seq1counts, screener.seq2counts