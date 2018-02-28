import random

def random_seq(length):
    seq = ""

    for i in range(length):
        seq += random.choice("atgc")
    return seq

def create_deletion(seq):
    removed = random.choice(range(len(seq)))
    ret = seq[0:removed] + seq[removed+1:len(seq)]

    return (ret)

def test_deletion(seq1, seq2):
    if len(seq2) < len(seq1):
        print ("This is a deletion mutation")
    else:
        print ("There is no mutation")


seq1 = random_seq(10)
seq2 = create_deletion(seq1)
test_deletion(seq1, seq2)
