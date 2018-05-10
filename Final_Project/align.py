DNA_2 = {'G': { 'G': 1, 'C':-3, 'A':-3, 'T':-3, 'N':0 },
         'C': { 'G':-3, 'C': 1, 'A':-3, 'T':-3, 'N':0 },
         'A': { 'G':-3, 'C':-3, 'A': 1, 'T':-3, 'N':0 },
         'T': { 'G':-3, 'C':-3, 'A':-3, 'T': 1, 'N':0 },
         'N': { 'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N':0 }}
"""
def calc_similarity(seqA, seqB, simMatrix):
    #iterate through the smaller sequence
    numPlaces = min(len(seqA), len(seqB))
    totalScore = 0.0

    #iterate through the length of the sequence
    for i in range(numPlaces):
        #set the individual elements
        residueA = seqA[i]
        residueB = seqB[i]
        #increment the total score by the score from the simmatrix
        totalScore += simMatrix[residueA][residueB]
    #return the total score
    return totalScore
"""

def pairAlignScore(alignA, alignB, simMatrix, insert =8, extend = 4):
    #variable for score
    score = 0.0;

    #find the shortest sequence length
    n = min(len(alignA), len(alignB))

    #loop through sequence
    for i in range(n):
        #find each residue in the sequence
        res1 = alignA[i]
        res2 = alignB[i]

        #compare each residue
        #first check whether either is a -
        if '-' not in (res1, res2):
            #add to score
            score += simMatrix[res1][res2]
        #else if '-' not before either of them
        elif(i > 0) and ('-' in (alignA[i-1], alignB[i-1]) ):
            #subtract extend score
            score -= extend

        else:
            #subtract insert score
            score -= insert
    return score


def sequenceAlign(seqA, seqB, simMatrix=DNA_2, insert=8, extend=4):

  numI = len(seqA) + 1
  numJ = len(seqB) + 1

  scoreMatrix = [[0] * numJ for x in range(numI)]
  routeMatrix = [[0] * numJ for x in range(numI)]

  for i in range(1, numI):
    routeMatrix[i][0] = 1

  for j in range(1, numJ):
    routeMatrix[0][j] = 2

  for i in range(1, numI):
    for j in range(1, numJ):

      penalty1 = insert
      penalty2 = insert

      if routeMatrix[i-1][j] == 1:
        penalty1 = extend

      elif routeMatrix[i][j-1] == 2:
        penalty2 = extend

      similarity = simMatrix[ seqA[i-1] ][ seqB[j-1] ]

      paths = [scoreMatrix[i-1][j-1] + similarity, # Route 0
               scoreMatrix[i-1][j] - penalty1, # Route 1
               scoreMatrix[i][j-1] - penalty2] # Route 2

      best = max(paths)
      route = paths.index(best)

      scoreMatrix[i][j] = best
      routeMatrix[i][j] = route

  alignA = []
  alignB = []

  i = numI-1
  j = numJ-1
  score = scoreMatrix[i][j]


  while i > 0 or j > 0:
    route = routeMatrix[i][j]

    if route == 0: # Diagonal
      alignA.append( seqA[i-1] )
      alignB.append( seqB[j-1] )
      i -= 1
      j -= 1

    elif route == 1: # Gap in seqB
      alignA.append( seqA[i-1] )
      alignB.append( '-' )
      i -= 1

    elif route == 2: # Gap in seqA
      alignA.append( '-' )
      alignB.append( seqB[j-1] )
      j -= 1

  alignA.reverse()
  alignB.reverse()
  alignA = ''.join(alignA)
  alignB = ''.join(alignB)

  return score, alignA, alignB


def consensusMultipleAlign(seqs, threshold, simMatrix):

  n = len(seqs)
  multipleAlign = []

  i = 0
  for j in range(i+1,n):
    seqB = seqs[j]

    if not multipleAlign:
      seqA = seqs[i]
      score, alignA, alignB = sequenceAlign(seqA, seqB, simMatrix)
      multipleAlign.append(alignA)
      multipleAlign.append(alignB)

    else:
      score, alignA, alignB = sequenceAlign(seqA, seqB, simMatrix)

      gaps = []
      for k, letter in enumerate(alignA):
        if letter == '-':
          gaps.append(k)

      for k, seq in enumerate(multipleAlign):
        for gap in gaps:
          seq = seq[:gap] + '-' + seq[gap:]

        multipleAlign[k] = seq

      multipleAlign.append(alignB)
  return (multipleAlign)
 # for k, seq in enumerate(multipleAlign):
      #print(k, seq)
