"""
Rao Vinnakota
Programming for Biology
Lab 07
"""
import random
from SequenceVariation import SequenceVariation, random_sequence
from protein_translate import list_convert
from pairwise_score import pairAlignScore, BLOSUM62, DNA_2
#from kmeans_commented import k_main

seq1, seq2, seq3 = random_sequence(20), random_sequence(20), random_sequence(20)
Seq1, Seq2, Seq3 = SequenceVariation(seq1), SequenceVariation(seq2), SequenceVariation(seq3)
aa1, aa2, aa3 = list_convert(Seq1.seqs), list_convert(Seq2.seqs), list_convert(Seq3.seqs)

def create_pairs(input_list, scoreMatrix):
    scores = []

    i = 1
    while (i < len(input_list)):
        scores.append(pairAlignScore(input_list[0], input_list[i], scoreMatrix))
        i += 1
    return scores

def create_paired(list1, list2):
    out = []
    i = 0

    if (len(list1) != len(list2)):
        raise Exception("Both lists need to be the same size")
    while (i < len(list1)):
        out.append((list1[i], list2[i]))
        i += 1
    return out


x1, y1 = create_pairs(Seq1.seqs, DNA_2), create_pairs(aa1, BLOSUM62)
x2, y2 = create_pairs(Seq2.seqs, DNA_2), create_pairs(aa2, BLOSUM62)
x3, y3 = create_pairs(Seq3.seqs, DNA_2), create_pairs(aa3, BLOSUM62)
data1 = create_paired(x1, y1)
data2 = create_paired(x2, y2)
data3 = create_paired(x3, y3)

print(data1)
print(data2)
print(data3)
