
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

    
    print(nuc_len)
    return(nuc_len)

user_input()
