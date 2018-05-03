# -*- coding: utf-8 -*-
"""
Lab 03
Created on Sun Feb 18 2018

@author: Rao Vinnakota
"""

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

#creates the codons from a given sequence
def create_codons(seq):
    codons  = []
    i = 0

    while (i <= len(seq)):
        if (len(seq[i:i+3]) == 3):
            codons.append(seq[i:i+3])
        i += 3
    return (codons)

#translates dna to amino afoids
def dna_to_aa(seq):
    rna = seq.replace('T', 'U')
    amino_acids = []
    codons = create_codons(seq)

    amino_acid_seq = ''
    for codon in codons:
        if codon in STANDARD_GENETIC_CODE:
            amino_acids.append(STANDARD_GENETIC_CODE[codon])
    for amino_acid in amino_acids:
        if amino_acid in AMINO_ACID_CODE:
            amino_acid_seq += AMINO_ACID_CODE[amino_acid]
    return (amino_acid_seq)


def list_convert(dna_list):
    aa_list = []

    for i in dna_list:
        aa_list.append(dna_to_aa(i))
    return aa_list
