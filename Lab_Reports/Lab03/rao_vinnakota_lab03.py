# -*- coding: utf-8 -*-
"""
Lab 03
Created on Sun Feb 18 2018

@author: Rao Vinnakota
"""

class Sequence:
    def __init__(self, filename):
        if not filename:
            raise Exception("The Sequence class requires a filepath as the input")
        self.filename = filename
        self.fasta = ""

    def get_filename(self):
        return (self.filename)

    def get_fasta(self):
        return (self.fasta)

    def set_fasta(self):
        sequence = []
        seq = ''
        my_file = open(self.filename)

        for line in my_file:
            if line.startswith('>'):
                continue
            else:
                seq += line.rstrip()
        if seq:
            sequence.append(seq)
        my_file.close()
        self.fasta += ''.join(sequence)

    def create_frame(self, seq):
        codons = []
        i = 3

        while (i < len(seq)):
            codons.append(seq[i:i+3])
            i += 3
        return (codons)

    def translateDNA(self, )

filename = 'sequence.fasta'
sequence = Sequence(filename)
sequence.set_fasta()
print(sequence.get_fasta())
