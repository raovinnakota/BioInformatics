"""
Counting K-Mers
Rao Vinnakota
Liz Miller
Phillippine Alba
Blake Burnley
Jelani Bell-Isaacs
Lillya Galechyan
"""
from string import maketrans
import operator

seq='atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'

def create_reverse_complement(seq):
    intab = "ATGC"
    outtab = "TACG"
    transtable = maketrans(intab, outtab)
    fasta = seq

    comp = fasta.translate(transtable)
    return comp[::-1]

def create_frames(seq):
    frames = []
    seq = seq;
    rev = create_reverse_complement(seq)

    for i in range(3):
        frames.append(seq[i:])
    for i in range(3):
        frames.append(rev[i:])
    return frames

def create_codons(frames, k):
    codons = []

    for frame in frames:
        codon = []
        i = 0
        while (i < len(frame)):
            codon.append(frame[i:i+k])
            i += k
        codons.append(codon)
    return (codons)
'''
def create_dictionary(codon):
    dictionary = {}

    for i in codon:
        if (len(i) < 3):
            continue
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

def compile_dictionaries(codons):
    dictionaries = []

    for codon in codons:
        dictionary = create_dictionary(codon)
        dictionaries.append(dictionary)
    return dictionaries
'''
def create_dictionary(codons):
    dictionary = {}

    for codon in codons:
        for i in codon:
            if (len(i) % 3 != 0):
                continue
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary
#dictionary = {}
#dictionary[codon[0]] = 0


frames = create_frames(seq)
codons = create_codons(frames, 6)
dictionary = create_dictionary(codons)
print(max(dictionary.iteritems(), key=operator.itemgetter(1))[0])
