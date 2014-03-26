class scorer:

    def __init__(self):
        1

    def scoreSequences(self, seq1, seq2):
        score = len(seq1)
        for index in range(0, len(seq1)):
                if seq2[index] != seq1[index]:
                    score -= 1
        return score

test = scorer()
print test.scoreSequences("tat","agtagtagt")