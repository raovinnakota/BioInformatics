# Rao Vinnakota
# CMSC 220
# Class Exercise 0201

###Ligase###
seq = "CTTTCGCAATGATA"
seq2 = "TGGTCAATBGCATTCAA"

def dnaligase(seq, seq2):
    valid = ['C', 'G', 'T', 'A']
    sumseq = seq + seq2

    for el in sumseq:
        if el not in valid:
            raise Exception("That's not valid input")
    print(sumseq)
    return (sumseq)

def nuclease(sequence, brkpoint):
    new = sequence[:brkpoint]
    new2 = sequence[brkpoint:]

    return new, new2

print(nuclease(seq, 4))
