#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:31:46 2018

@author: philippinealba
"""
import random
#Want to create an insertion point mutation

#create a random DNA sequence
def create_seq(length):
    ranges = length
    sequence = ''.join(random.choice('ACTG') for i in range(ranges))
    return sequence

#define a random mutation point
def mutation_point(length):
    seql = length
    mutationpoint = random.randint(0, seql)
    return mutationpoint

#define mutation insertion nucleotide
def insertion_mutation(length):
    sequence = create_seq(length)
    mutlocation = mutation_point(length)
    mutation = random.choice('ATCG')
    first = sequence[:mutlocation]
    last = sequence[mutlocation:]
    newseq = '{}{}{}'.format(first, mutation, last)
    print('Original Seq: ', sequence)
    print('Mutated Seq: ', newseq)
    
#test mutation function
#test mutation test    
insertion_mutation(10)
seq1 = 'ATCTACTCATCAT'
seq2 = 'ATCGACTACGACTA'

#test the mutation type:
def test_mutation(originalseq, newseq):
    original = len(originalseq)
    outcome = len(newseq)
    testlength = outcome - 1
    if original == testlength:
        print('Mutation type: Insertion')
    else:
        print('Mutation type: Unknown')
test_mutation(seq2, seq1)       
    