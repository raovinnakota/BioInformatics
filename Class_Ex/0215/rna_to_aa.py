# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:53:50 2018

@author: Kerri Norton
"""

# -*- coding: utf-8 -*-
"""
Translation
Created on Wed Jan 17 12:39:02 2018

@author: Kerri Norton
"""
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

def reverseTransDNA(DNA):
    DNA = DNA.replace('T', 'U')
    intab = "AUCG"
    outtab = "UAGC"
    transTable = maketrans(intab, outtab)
    DNAcomp = DNA.translate(transTable)
    DNArev = DNAcomp[::-1]
    return DNAcomp, DNArev

def translate(sequence):
    codons = []
    amino_acids = []
    amino_seq = ""
    i = 0

    while (i < len(sequence)):
        codons.append(sequence[i:i+3])
        i+=3
    for codon in codons:
        if codon in STANDARD_GENETIC_CODE:
            amino_acids.append(STANDARD_GENETIC_CODE[codon])
    for amino_acid in amino_acids:
        if amino_acid in AMINO_ACID_CODE:
            amino_seq += AMINO_ACID_CODE[amino_acid]
    print "Incoming RNA: %s\nTranslated Amino Acids: %s"%(sequence, amino_seq)
    return (sequence, amino_seq)

translate("UAUUUAUUGCUUCAUCCA")
