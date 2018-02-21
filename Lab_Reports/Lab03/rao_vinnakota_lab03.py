# -*- coding: utf-8 -*-
"""
Lab 03
Created on Sun Feb 18 2018

@author: Rao Vinnakota
"""
import re
from string import maketrans

#Dictionary for AA
STANDARD_GENETIC_CODE = {
          'UUU':'Phe', 'UUC':'Phe', 'UCU':'Ser', 'UCC':'Ser',
          'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys',
          'UUA':'Leu', 'UCA':'Ser', 'UAA':'Stop','UGA':'Stop',
          'UUG':'Leu', 'UCG':'Ser', 'UAG':'Stop','UGG':'Trp',
          'CUU':'Leu', 'CUC':'Leu', 'CCU':'Pro', 'CCC':'Pro',
          'CAU':'His', 'CAC':'His', 'CGU':'Arg', 'CGC':'Arg',
          'CUA':'Leu', 'CUG':'Leu', 'CCA':'Pro', 'CCG':'Pro',
          'CAA':'Gln', 'CAG':'Gln', 'CGA':'Arg', 'CGG':'Arg',
          'AUU':'Ile', 'AUC':'Ile', 'ACU':'Thr', 'ACC':'Thr',
          'AAU':'Asn', 'AAC':'Asn', 'AGU':'Ser', 'AGC':'Ser',
          'AUA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
          'AUG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
          'GUU':'Val', 'GUC':'Val', 'GCU':'Ala', 'GCC':'Ala',
          'GAU':'Asp', 'GAC':'Asp', 'GGU':'Gly', 'GGC':'Gly',
          'GUA':'Val', 'GUG':'Val', 'GCA':'Ala', 'GCG':'Ala',
          'GAA':'Glu', 'GAG':'Glu', 'GGA':'Gly', 'GGG':'Gly'}

AMINO_ACID_CODE = {
          'Ala':'A', 'Cys':'C', 'Asp':'D', 'Glu':'E',
          'Phe':'F', 'Gly':'G', 'His':'H', 'Ile':'I',
          'Lys':'K', 'Leu':'L', 'Met':'M','Asn':'N',
          'Pro':'P', 'Gln':'Q', 'Arg':'R','Ser':'S',
          'Thr':'T', 'Val':'V', 'Trp':'W', 'Tyr':'Y',
          'Stop':'_',
        }

class Sequence:
    def __init__(self, filename):
        if not filename:
            raise Exception("The Sequence class requires a filepath as the input")
        self.filename = filename
        self.fasta = ""
        self.rev_comp = ""
        self.amino_acids = []

    def get_filename(self):
        return (self.filename)

    def get_fasta(self):
        return (self.fasta)

    def get_rev_comp(self):
        return (self.rev_comp)

    def get_amino_acids(self):
        return (self.amino_acids)

    def set_amino_acids(self, amino_acid):
        self.amino_acids.append(amino_acid)

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

    def set_rev_comp(self):
        intab = "ATGC"
        outtab = "TACG"
        transtable = maketrans(intab, outtab)

        self.set_fasta()
        comp = self.fasta.translate(transtable)
        self.rev_comp = comp[::-1]

    def create_frame(self, seq):
        seq = seq.replace('T', 'U')
        codons = []
        i = 3

        while (i < len(seq)):
            codons.append(seq[i:i+3])
            i += 3
        return (codons)

    def dna_to_aa(self):
        fasta = self.get_fasta()
        rev_comp = self.get_rev_comp()
        codons = []

        for i in range(3):
            codons = self.create_frame(fasta[i:])
            amino_acids = []
            amino_acid_seq = ""
            for codon in codons:
                if codon in STANDARD_GENETIC_CODE:
                    amino_acids.append(STANDARD_GENETIC_CODE[codon])
            for amino_acid in amino_acids:
                if amino_acid in AMINO_ACID_CODE:
                    amino_acid_seq += AMINO_ACID_CODE[amino_acid]
            self.set_amino_acids(amino_acid_seq)
        for i in range(3):
            codons = self.create_frame(rev_comp[i:])
            amino_acid = []
            amino_acid_seq = ""
            for codon in codons:
                if codon in STANDARD_GENETIC_CODE:
                    amino_acids.append(STANDARD_GENETIC_CODE[codon])
            for amino_acid in amino_acids:
                if amino_acid in AMINO_ACID_CODE:
                    amino_acid_seq += AMINO_ACID_CODE[amino_acid]
            self.set_amino_acids(amino_acid_seq)


    def translateDNA(self):
        self.set_fasta()
        fasta = self.get_fasta()
        self.dna_to_aa()
        user_in = raw_input("Which reading frame (1-6) would you like to use?\n")
        if (user_in == "0"):
            for i in range(6):
                print "Reading Frame #%d: %s\n"%(i+1, self.amino_acids[i])
        else:
            print "Reading Frame #%s:%s"%(user_in, self.amino_acids[int(user_in)-1])

filename = 'sequence.fasta'
Seq = Sequence(filename)
Seq.translateDNA()
