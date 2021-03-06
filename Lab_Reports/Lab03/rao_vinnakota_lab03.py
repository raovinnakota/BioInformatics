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
    #constructors - helpful values that I can store and they stay static
    def __init__(self, filename):
        if not filename:
            raise Exception("The Sequence class requires a filepath as the input")
        self.filename = filename
        self.DNA = self.set_fasta()
        self.rev_comp = self.set_rev_comp()
        self.reading_frames = []
        self.amino_acids = []
        self.set_frames()

    #getter methods to return constructors
    def get_filename(self):
        return (self.filename)

    def get_fasta(self):
        return (self.DNA)

    def get_rev_comp(self):
        return (self.rev_comp)

    def get_amino_acids(self):
        return (self.amino_acids)

    def get_reading_frames(self):
        return (self.reading_frames)

    #setter methods to build attributes that aren't filled at initialization
    def add_reading_frame(self, frame):
        self.reading_frames.append(frame)

    def add_amino_acid(self, amino_acid):
        self.amino_acids.append(amino_acid)

    #checker function to validate input
    def validate_fasta(self, seq):
        bases = ['A', 'T', 'C', 'G', 'N']

        #if any part of the fasta sequence isn't in the list of known bases
        #raise exception
        for i in seq:
            if i not in bases:
                raise Exception("Invalid sequence in the input")
        return (1)

    #create a DNA sequence for the constructor
    def set_fasta(self):
        sequence = []
        seq = ''
        my_file = open(self.filename)

        for line in my_file:
            if line.startswith('>'):
                continue
            else:
                seq += line.rstrip()
        if (self.validate_fasta(seq) == 1):
            sequence.append(seq)
        my_file.close()
        return (''.join(sequence))

    #creates the reverse complement of DNA sequence
    def set_rev_comp(self):
        intab = "ATGC"
        outtab = "TACG"
        transtable = maketrans(intab, outtab)
        fasta = self.get_fasta()

        comp = fasta.translate(transtable)
        return comp[::-1]

    #Creates all 6 reading frames to be used for translation
    def set_frames(self):
        frames = []
        fasta = self.get_fasta()
        rev_comp = self.get_rev_comp()

        for i in range(3):
            self.add_reading_frame(fasta[i:])
        for i in range(3):
            self.add_reading_frame(rev_comp[i:])

    #creates a list of codons for any given frame
    def create_frame(self, seq):
        seq = seq.replace('T', 'U')
        codons = []
        i = 0

        while (i < len(seq)):
            codons.append(seq[i:i+3])
            i += 3
        return (codons)

    #translates dna to amino acids
    def dna_to_aa(self):
        fasta = self.get_fasta()
        rev_comp = self.get_rev_comp()
        frames = self.get_reading_frames()
        codons = []
        amino_acids = []

        #for the first three reading frames, use dictionaries to tanslate
        for i in range(6):
            codons = self.create_frame(frames[i])
            amino_acids[:] = []
            amino_acid_seq = ''
            for codon in codons:
                if codon in STANDARD_GENETIC_CODE:
                    amino_acids.append(STANDARD_GENETIC_CODE[codon])
            for amino_acid in amino_acids:
                if amino_acid in AMINO_ACID_CODE:
                    amino_acid_seq += AMINO_ACID_CODE[amino_acid]
            self.add_amino_acid(amino_acid_seq)

    def translateDNA(self):
        self.dna_to_aa()
        user_in = raw_input("Which reading frame (1-6) would you like to use?\n")
        if (user_in == "0"):
            for i in range(6):
                print "Reading Frame #%d: %s\n"%(i+1, self.amino_acids[i])
        elif (int(user_in) > 6):
            raise Exception("Valid input range from 1 to 6")
        else:
            print "Reading Frame #%s:%s"%(user_in, self.amino_acids[int(user_in)-1])

    #start codon: AUG
    #stop codons: UAG, UGA, UAA
    def predictRF(self):
        frames = self.get_reading_frames()
        output = ()

        for frame in frames:
            rframe = frame.replace('T', 'U')
            #uses search and regex to find matches between start/stop codons
            match = re.search(r'AUG\w+(?:UAG|UAA|UGA)', rframe)
            #if a match exists, it adds the substring to the tuple
            if match:
                output = output + (match.group(), )
            else:
                output = output + (None, )
        print output
        return output

    def longestRE(self):
        frames = self.predictRF()
        length = 0
        count = 0

        #creates an indexable list to iterate through tuple
        for i, a in enumerate(frames):
            #check against current length
            if (a and (len(a) > length)):
                length = len(a)
                count = i
                frame = a
        #print and return longest frame
        print("Longest: Frame #%d:%s")%(count, frame)
        return frame

filename = 'rf.fasta'
Seq = Sequence(filename)
Seq.predictRF()
Seq.longestRE()
Seq.translateDNA()
