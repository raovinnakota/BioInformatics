"""
Enzyme functions
Created on Thu Feb  1 13:49:18 2018

@author: raovinnakota
"""

class ChainSeq(object):
    def __init__(self):
        self.name = ""
        self.fastaN = ""
        self.fastaAA = ""
        self.protein = ""

    def return_sequence(self):
        user_in = raw_input("Are you interested in the nucleotide, protein, or centroid data?\n")
        if (user_in == "nucleotide"):
            self.readFasta("dna")
