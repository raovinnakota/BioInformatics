# -*- coding: utf-8 -*-
"""
Consensus Multiple Alignment
Created on Fri Feb  2 10:08:02 2018

@author: Kerri Norton
"""

from Alignments import BLOSUM62, DNA_2, sequenceAlign

def consensus(alignment, threshold=0.25):

  #finding length of first sequence
  n = len(alignment[0])
  #number of sequences
  nSeq = float(len(alignment))
  consensus = ''

  #loop through all of the bases in the sequence
  for i in range(n):
    #creates new dictionary
    counts = {}

    #for loop for every sequence in alignment
    for seq in alignment:
      #sets letter to ith nucleotide in sequence
      letter = seq[i]
      #if nucleotide is dash (gap), skip it
      if letter == '-':
        continue
    #sets value of letter to one plus previous
    #if previous doesn't exist, makes new key and sets its value to 1
      counts[letter] = counts.get(letter, 0) + 1
    
    #new list
    fractions = []
    #for every key in dictionary, creates a fraction 
    for letter in counts:
        #take value/number of sequences
      frac = counts[letter]/nSeq
      #appends a list of lists with the fraction and letter
      #frac is the average/percetage of each letter in the sequences
      fractions.append([frac, letter])
      
    #sorts the list in order from leat frequent to most
    fractions.sort()
    #pull out last entry (most frequent) and set for bestFrac, bestLet
    bestFraction, bestLetter = fractions[-1]
    
    #testing if frantion is less than or equal to threshold
    #if so add 'N' - no consensus
    if bestFraction <=  threshold:
      consensus += 'N'
    #otherwise adds bestletter to consensus
    else:
      consensus += bestLetter

  return consensus

#inputs are the seqs, the threshold, and a similarity Matrix
def consensusMultipleAlign(seqs, threshold, simMatrix):
  #counts number of sequences
  n = len(seqs)
  #setting default penalty and new list
  insert = 2;
  extend = 4;
  multipleAlign = []
  
  i = 0
  #looping through sequences
  #set j as i+1 to compare first to second seq
  for j in range(i+1,n):
    #seqB starts as first sequence
    seqB = seqs[j]

    #at the beginning, seqA is our first sequence
    if not multipleAlign:
      seqA = seqs[i]
      #Align our two sequences (with gaps!)
      #outputs: score and two newly aligned sequences
      score, alignA, alignB = sequenceAlign(seqA, seqB, simMatrix,insert, extend)
      #adds newly aligned sequences to our list
      multipleAlign.append(alignA)
      multipleAlign.append(alignB)
      
    
    else:
      # seqA is our consensus sequence and align seqB to our consensus seq
      seqA = consensus(multipleAlign, threshold)
      score, alignA, alignB = sequenceAlign(seqA, seqB, simMatrix,insert, extend)
      #creates new list
      gaps = []
      #for everythin in alignA list, k is index, and letter is value
      for k, letter in enumerate(alignA):
        # if letter is a dash (there's a gap) 
        if letter == '-':
          #appends index to gap
          #keeps track of locations of gaps
          gaps.append(k)
      
      #enumerate through each sequence in multipleAlign
      for k, seq in enumerate(multipleAlign):
        #go through list of gaps
        for gap in gaps:
          # add a dash at each index for each gap
          seq = seq[:gap] + '-' + seq[gap:]
        
        # 
        multipleAlign[k] = seq
      
      #
      multipleAlign.append(alignB)
      
  
  #    
  for k, seq in enumerate(multipleAlign):
    print(k, seq)


if __name__ == '__main__':

  print('\nConsensus sequence')
  
  alignment = ['SRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK',
               'TVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK',
               'HHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIK',
               'HEFSELVIALIIFGVMAGVIGTILFISYGSRRLIK']

#  print(consensus(alignment))
#  
#  seqs = ['SRPAPVVLIILCVMAGVIGTILLISYGIRLLIK',
#          'TVPAPVVIILIILCVMAGIIGTILLLIISYTIRRLIK',
#          'HHFSEPEITLIIFGVMAGVIGTILLLIISYGIRLIK',
#          'HFSELVIALIIFGVMAGVIGTILFISYGSRLIK']


#  print('\nConsensus paired alignment')
#
#  consensusMultipleAlign(seqs, 0.25, BLOSUM62)
  
  seqsn = ['ATTGGC', 'ATTCGC', 'ATTGAC', 'ATTGC']
  consensusMultipleAlign(seqsn, 0.25, DNA_2)

  seqsn = ['ATTGGCTTC', 'ATTCGCC', 'ATTGACTT', 'ATTGTTC']
  consensusMultipleAlign(seqsn, 0.5, DNA_2)
