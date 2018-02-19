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
    self.fasta = ''

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

filename = 'sequence.fasta'
sequence = Sequence(filename)
print(sequence.get_fasta())
