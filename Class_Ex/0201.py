# -*- coding: utf-8 -*-
"""
Enzyme functions
Created on Thu Feb  1 13:49:18 2018

@author: Bioinformatics Class
"""
#Ligase
#connects two Strings
#concatenants
from string import maketrans

seq = 'CTTTCGCAATGATA'
seq2 = 'TGGTCAATGCATTTCAA'

#For lab report
#Create a reverse Transcription function
def reverseTransDNA(DNA):
    DNA = DNA.replace('T', 'U')
    intab = "AUCG"
    outtab = "UAGC"
    transTable = maketrans(intab, outtab)
    DNAcomp = DNA.translate(transTable)
    DNArev = DNAcomp[::-1]
    return DNAcomp, DNArev

#validate input
def ligase(sequence, seq2):
#strings (then lists)
    sumseq = sequence +seq2
#compare last element compare ot first seq

    #print output
    print(sumseq)
    #return output
    return sumseq

ligase(seq,seq2)

#validate input
def dnaligase(sequence, seq2):
    validation = ['A','C','T','G']

    #strings (then lists)
    sumseq = sequence +seq2
    #compare last element compare ot first seq
    for el in sumseq:
       if el not in validation:
           raise Exception('Not a volid DNA sequence')

    #print output
    print(sumseq)
    #return output
    return sumseq

#cuts dna
def nuclease(sequence,cutpoint):
    news = sequence[2:cutpoint]
    news2 = sequence[cutpoint:]

    return news, news2

print(reverseTransDNA("CTTTCGCAATGATA"))
