"""
Rao Vinnakota
CMSC 220
Final Project
"""
import sys
from align import DNA_2, consensusMultipleAlign, pairAlignScore
from kclass import kNearestNeighbour, euclideanDistance, getFeatureDistance

humanbase = "humanbase.fasta"
cancerbase = "cancerbase.fasta"
#testfile = "test02can.fasta"
#testfile = "test01human.fasta"
#testfile = "test00can.fasta"
testfile = sys.argv[1]
#humfiles = ["humanbase.fasta", "human01.fasta", "human02.fasta", "human03.fasta", "human04.fasta"]
humfiles = ["humanbase.fasta", "human01.fasta", "human03.fasta", "human04.fasta"]
cancerfiles = ["cancerbase.fasta", "cancer01.fasta", "cancer02.fasta", "cancer03.fasta", "cancer04.fasta"]

def read_fasta(filename):
    sequence = []
    seq = ''
    my_file = open(filename)
    for line in my_file:
        if line.startswith('>'):
            continue
        else:
            seq += line.rstrip()
    if (seq):
        sequence.append(seq)
    my_file.close()
    seq = ''.join(sequence)
    return (seq[:100])
    #return (''.join(sequence))

def read_seqs(file_list):
    fastas = []

    for i in file_list:
        fastas.append(read_fasta(i))
    return (fastas)

def total_similarity(baseline, seqs, input_type):
    scores = []

    for i in seqs:
        score = ((pairAlignScore(baseline, i, DNA_2)), input_type)
        scores.append(score)
    return (scores)


humseqs = read_seqs(humfiles)
cancerseqs = read_seqs(cancerfiles)
humbase = read_fasta(humanbase)
cancerbase = read_fasta(cancerbase)
query_seq = read_fasta(testfile)

humaligned = consensusMultipleAlign(humseqs, 0.25, DNA_2)
canceraligned = consensusMultipleAlign(cancerseqs, 0.25, DNA_2)

known = total_similarity(humaligned[0], humaligned, 'human') + total_similarity(humaligned[0], canceraligned, 'cancer')
query_score = pairAlignScore(humaligned[0], query_seq, DNA_2)

result = kNearestNeighbour(known, query_score, k=8)
print('Cell line type:', result)
