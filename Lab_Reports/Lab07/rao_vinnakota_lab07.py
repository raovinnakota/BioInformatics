"""
Rao Vinnakota
Programming for Biology
Lab 07
"""
import random
from SequenceVariation import SequenceVariation

def random_sequence(len):
    seq = ''
    i = 0

    if (len < 0):
        raise Exception("Not a valid length")
    while (i < len):
        seq += random.choice('ATCG')
        i += 1
    return seq

seq1, seq2, seq3 = random_sequence(10), random_sequence(10), random_sequence(10)
Seq1, Seq2, Seq3 = SequenceVariation(seq1), SequenceVariation(seq2), SequenceVariation(seq3)

print (Seq1.seqs)
print (Seq2.seqs)
print (Seq3.seqs)
