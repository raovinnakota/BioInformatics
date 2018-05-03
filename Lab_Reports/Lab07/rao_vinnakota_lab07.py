"""
Rao Vinnakota
Programming for Biology
Lab 07
"""
import random
from SequenceVariation import SequenceVariation, random_sequence
from protein_translate import list_convert

seq1, seq2, seq3 = random_sequence(20), random_sequence(20), random_sequence(20)
Seq1, Seq2, Seq3 = SequenceVariation(seq1), SequenceVariation(seq2), SequenceVariation(seq3)
aa1, aa2, aa3 = list_convert(Seq1.seqs), list_convert(Seq2.seqs), list_convert(Seq3.seqs)


print(aa1)
print(aa2)
print(aa3)
