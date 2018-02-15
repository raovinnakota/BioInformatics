import re

def readFasta(filename):
    sequence = []
    seq = ''
    myFile = open(filename)

    for line in myFile:
        if line.startswith('>'):
            continue
        else:
            seq += line.rstrip()
    if seq:
        sequence.append(seq)
    return sequence

def user_input():
    user_in = raw_input("Are you interested in the nucleotide, protein, or centroid data?\n")
    if (user_in == 'nucleotide'):
        nuc_seq = ''.join(readFasta('sequence.fasta'))
        nucleotide(nuc_seq)

def nucleotide(nuc_seq):
    nuc_len = len(nuc_seq)
    freqA = len(re.findall('[A|a]', nuc_seq))
    freqT = len(re.findall('[T|t]', nuc_seq))
    freqG = len(re.findall('[G|g]', nuc_seq))
    freqC = len(re.findall('[C|c]', nuc_seq))
    #freqOther = len(re.findall(['A|a|T|t|G|g|C|c'], nuc_seq))
    freqOther = nuc_len - (freqA + freqT + freqG + freqC)
    print "TotalLength:%s\nFreqA:%s\nFreqT:%s\nFreqC:%s\nFreqG:%s\nOther:%s"%(nuc_len, freqA, freqT, freqC, freqG, freqOther)

    return(nuc_len, freqA)

user_input()
