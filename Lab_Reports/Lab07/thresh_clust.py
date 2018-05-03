# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:22:12 2018

@author: Kerri-Ann Norton
Threshold Clustering
"""
from matplotlib import pyplot

from random import randint, sample

from numpy import array, cov, diag, dot, linalg, ones
from numpy import outer, random, sqrt, vstack, zeros


def euclideanDist(vectorA, vectorB):

  diff = vectorA-vectorB

  return sqrt(dot(diff,diff))


def findNeighbours(data, distFunc, threshold):

  neighbourDict = {}

  n = len(data)
  for i in range(n):
    neighbourDict[i] = []

  for i in range(0,n-1):
    for j in range(i+1,n):
      dist = distFunc(data[i], data[j])

      if dist < threshold:
        neighbourDict[i].append(j)
        neighbourDict[j].append(i)

  return neighbourDict


def simpleCluster(data, threshold, distFunc=euclideanDist):

  neighbourDict = findNeighbours(data, distFunc, threshold)

  clusters = []
  pool = set(range(len(data)))

  while pool:
    i = pool.pop()
    neighbours = neighbourDict[i]
    cluster = set()
    cluster.add(i)

    pool2 = set(neighbours)
    while pool2:
      j = pool2.pop()

      if j in pool:
        pool.remove(j)
        cluster.add(j)
        neighbours2 = neighbourDict[j]
        pool2.update(neighbours2)

    clusters.append(cluster)

  clusterData = []
  for cluster in clusters:
    clusterData.append( [data[i] for i in cluster] )

  return clusterData


def thresh_main(data1, data2, data3):


  print("\nSimple associative clustering\n")

  spread = 0.12
  sizeDims = (100,2)
  data = [data1,
          data2,
          data3]

  data = vstack(data)
  random.shuffle(data) # Randomise order

  clusters = simpleCluster(data, 0.10)

  colors = ['#F2C1B6','#A0B9A2','#F0A050',
            '#C0F0A0','#80A0B0','#B0A0C0']

  markers = ['d','o','s','>','^']

  i = 0
  for cluster in clusters:
     allX, allY = zip(*cluster)

     if len(cluster) > 3:
       color = colors[i % len(colors)]
       marker = markers[i % len(markers)]
       pyplot.scatter(allX, allY, s=30, c=color, marker=marker)
       i += 1

     else:
       pyplot.scatter(allX, allY, s=5, c='black', marker='o')

  pyplot.show()
