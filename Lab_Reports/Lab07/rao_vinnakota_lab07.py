"""
Rao Vinnakota
Programming for Biology
Lab 07
"""
import random
from SequenceVariation import SequenceVariation, random_sequence
from protein_translate import list_convert
from pairwise_score import pairAlignScore, BLOSUM62, DNA_2
from kmeans_commented import k_main
from thresh_clust import thresh_main

#create random sequences of length 20
seq1, seq2, seq3 = random_sequence(20), random_sequence(20), random_sequence(20)
#create the 9 variations of the sequences
Seq1, Seq2, Seq3 = SequenceVariation(seq1), SequenceVariation(seq2), SequenceVariation(seq3)
#create amino acids for all 30 sequences
aa1, aa2, aa3 = list_convert(Seq1.seqs), list_convert(Seq2.seqs), list_convert(Seq3.seqs)

#creating the x,y values, or pairwise scores by comparing altered with base
def create_pairs(base_point, input_list, scoreMatrix):
    scores = []

    i = 0
    while (i < len(input_list)):
        scores.append(pairAlignScore(base_point, input_list[i], scoreMatrix))
        i += 1
    return scores

#creating coordinate pairs from x/y inputs
def create_paired(list1, list2):
    out = []
    i = 0

    if (len(list1) != len(list2)):
        raise Exception("Both lists need to be the same size")
    while (i < len(list1)):
        out.append((list1[i], list2[i]))
        i += 1
    return out

#getting distances
x1, y1 = create_pairs(seq1, Seq1.seqs, DNA_2), create_pairs(seq1, aa1, BLOSUM62)
x2, y2 = create_pairs(seq1, Seq2.seqs, DNA_2), create_pairs(seq1, aa2, BLOSUM62)
x3, y3 = create_pairs(seq1, Seq3.seqs, DNA_2), create_pairs(seq1, aa3, BLOSUM62)
#creating pairs
data1 = create_paired(x1, y1)
data2 = create_paired(x2, y2)
data3 = create_paired(x3, y3)
#k-means clustering
k_main(data1, data2, data3)
#threshold clustering
thresh_main(data1, data2, data3)
