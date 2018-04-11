# -*- coding: utf-8 -*-
"""
NeighborTree
Created on Sat Feb 10 14:47:42 2018

@author: Kerri Norton
"""

from math import log, exp

from MultipleAlign import profile, profileAlign
from Sequences import STANDARD_GENETIC_CODE as SGC
from Alignments import DNA_1, BLOSUM62, sequenceAlign, calcSeqSimilarity

#Create sequences 
seqs = ['QPVHPFSV', 'QLVHRFSV', 'QLVHPFS', 'QPVYHFFV']

#calculate distance matrix 
def getDistanceMatrix(seqs, simMatrix):

  n = len(seqs)
  #NbyN
  matrix = [[0.0] * n for x in range(n)]
  
  maxScores = [calcSeqSimilarity(x, x, simMatrix) for x in seqs]

  for i in range(n-1):
    seqA = seqs[i]
  
    for j in range(i+1,n):
      seqB = seqs[j]
      
      score, alignA, alignB = sequenceAlign(seqA, seqB, simMatrix)
      maxScore = max(maxScores[i],maxScores[j])
      dist = maxScore - score
      
      matrix[i][j] = dist
      matrix[j][i] = dist

  return matrix

ourdistMatrix = getDistanceMatrix(seqs, BLOSUM62)
print(ourdistMatrix)

#Tree construction
def getDistToJunction(distMatrix, i, j):
  
  n = len(distMatrix)
  row = distMatrix[i]
  column = distMatrix[j]
 
  dist = distMatrix[i][j] + (sum(row)-sum(column))/(n-2)
  dist *= 0.5

  return dist

#get joinPair
def getJoinPair(distMatrix):
    n = len(distMatrix) 
    minQ = None
    joinPair = None
    
    for i in range(n-1):
        #sums the Rows 
        sumRow = sum(distMatrix[i]) 
        
        #j looks at next row
        for j  in range(i+1,n):
            #sums the next row; same as suming column
            sumNext = sum(distMatrix[j])
            
            #record the distance
            dist = distMatrix[i][j]
            q = (n-2)*dist -sumRow - sumNext
            print(i,j,q)
            
            if (minQ is None) or (q < minQ):
                minQ = q
                joinPair = [i,j]

    return joinPair
    
print(getJoinPair(ourdistMatrix))