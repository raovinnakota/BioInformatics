"""
Rao Vinnakota
CMSC 220
Final Project
"""
import random

#similarity matrix for DNA_2
DNA_2 = {'G': { 'G': 1, 'C':-3, 'A':-3, 'T':-3, 'N':0 },
         'C': { 'G':-3, 'C': 1, 'A':-3, 'T':-3, 'N':0 },
         'A': { 'G':-3, 'C':-3, 'A': 1, 'T':-3, 'N':0 },
         'T': { 'G':-3, 'C':-3, 'A':-3, 'T': 1, 'N':0 },
         'N': { 'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N':0 }}

file1 = "humanbase.fasta"
file2 = "cancerbase.fasta"

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
        return (''.join(sequence))

print(humanbase)
