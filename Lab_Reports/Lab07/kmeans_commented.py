# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:58:42 2018

@author: Kerri Norton

Commented by Blake, Rao, and Jelani
"""

from matplotlib import pyplot

from random import randint, sample

from numpy import array, cov, diag, dot, linalg, ones
from numpy import outer, random, sqrt, vstack, zeros

# returns euclidean distance
def euclideanDist(vectorA, vectorB):

  diff = vectorA-vectorB # difference between vectorA and vectorB

  return sqrt(dot(diff,diff))


def findNeighbours(data, distFunc, threshold):

  neighbourDict = {}  # empty dict of neighbors

  n = len(data)
  # initialize empty list as value of key i
  for i in range(n):
    neighbourDict[i] = []

  # set dist as euclidean distance between each possible combinations of points
  for i in range(0,n-1):
    for j in range(i+1,n):
      dist = distFunc(data[i], data[j])

      # if that distance is less than the threshold then append to a list of neighbor points
      if dist < threshold:
        neighbourDict[i].append(j)
        neighbourDict[j].append(i)

  # return a dictionary of neighbor connections
  return neighbourDict

def kMeans(data, k, centers=None):

  # set centers equal to an array of lists containing k random elements in data
  if centers is None:
    centers = array( sample(list(data), k) )  # list() not needed in Python 2

  change = 1.0 # define amount of change
  prev = []

  # loop while change between cycles is big enough
  while change > 1e-8:

    clusters = [[] for x in range(k)] # empty array of k many arrays
    # loop through every vector in the array of data
    for vector in data:
      diffs = centers - vector # calculate difference between centers and each vector
      dists = (diffs * diffs).sum(axis=1) # square difference and sum
      closest = dists.argmin() # closest equals index of minimum distance
      clusters[closest].append(vector) # append the vector to closest cluster

    # set change to 0
    change = 0

    # change clusters to be iterable to loop through
    for i, cluster in enumerate(clusters):
      cluster = array(cluster)     # create array of clusters
      center = cluster.sum(axis=0)/len(cluster) # averaging each cluster to find a new center
      diff = center - centers[i] # find the difference between the old and new center

      # set change equal to the sum of squared distances between old and new centers
      change += (diff * diff).sum()
      centers[i] = center # set new center

  # Once change is small enough, return the list of centers and clusters
  return centers, clusters

'''
Here we use this function to make a better guess of the initial centers
by choosing centers that are guranteed to be further apart.
'''
def kMeansSpread(data, k):

  n = len(data) # length of data set
  index = randint(0, n-1) # choose random initial center index
  indices = set([index]) # create a set of indices

  # array of zeros
  influence = zeros(n)

  # loop while the number of centers is less that desired
  while len(indices) < k:
    diff = data - data[index] # find diff between each point and a center
    sumSq = (diff * diff).sum(axis=1) + 1.0 # sum of differences squared
    # this makes it so that the largest distances will make influence small
    influence += 1.0 / sumSq
    index = influence.argmin() # set index equal to the index of the smallest influence

    # change index to another random int
    while index in indices:
      index = randint(0, n-1)

    # Add the index of a center to indices
    indices.add(index)

  # set centers equal to our improved centers
  centers = vstack([data[i] for i in indices])

  # run kmeans using improved centers
  return kMeans(data, k, centers)



def k_main(testData1, testData2, testData3):

  print("\nK-means clustering\n")

  # 1000 points in 2D
  #testDataA = random.random((1000,2)) # No clumps

  # group into 3 random clusters
  #centers, clusters = kMeans(testDataA, 3)

  # here we add two distinct clumps of 2D points
  #testDataB1 = random.normal(0.0, 2.0, (100,2))
  #testDataB2 = random.normal(7.0, 2.0, (100,2))
  testDataB = vstack([testData1, testData2, testData3]) # Two clumps

  centers, clusters = kMeans(testDataB, 3)

  # display graph in colored clusters
  colors = ['#FF0000','#00FF00','#0000FF',
            '#FFFF00','#00FFFF','#FF00FF']

  for i, cluster in enumerate(clusters):
     x, y = zip(*cluster)
     color = colors[i % len(colors)]
     pyplot.scatter(x, y, c=color, marker='o')

  x, y = zip(*centers)
  pyplot.scatter(x, y, s=40, c='black', marker='o')
  pyplot.show()
