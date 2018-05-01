"""
Lab 05 - Sequence Alignment
Rao Vinnakota

"""
import random

class SequenceVariation:
    def __init__(self, input_seq):
        #check if the input string is empty, Exception if it is
        if (input_seq == ""):
            raise Exception("Can't create class with empty string")
        #create seq1 from input str
        self.seqs = []
        self.seq1 = input_seq
        self.seqs.append(self.seq1)
        #call various class methods, starting with valid
        self.validate()
        self.seq2 = self.point_mutations(self.seq1, 10)
        self.seq3, self.seq4 = self.recombination(self.seq1, self.seq2)
        self.seq5 = self.add_variable_copy(self.seq1)
        self.seq6 = self.del_variable_copy(self.seq1)
        self.seq7 = self.transposon(self.seq1, 'ACGTGGTTGCACGT')
        self.seq8 = self.deletion_mutation(self.seq1)


    def get_input_seq(self):
        #return the input_seq
        return (self.seq1)


    def validate(self):
        #retrieve input_seq
        input_seq = self.get_input_seq()
        #valid list of bases
        valid = ['A', 'G', 'T', 'C', 'N']

        #iterate through sequence
        for i in input_seq:
            #if encounter an invalid base, raise an Exception
            if i not in valid:
                raise Exception("Not a valid input sequence")
        #1 indicates a valid string
        return (1)


    def point_mutations(self, seq, n):
        #retriev sequence, switch to list format
        input_seq = list(seq)

        #if # of requested mutations > len --> raise exception
        if (n > len(input_seq)):
            raise Exception("Impossible to have more mutations than nucleotides")
        #run point mutation n times
        for i in range(n):
            #choose a random base
            mut = random.choice('ACTG')
            #pick a random location
            loc = random.randint(0, len(input_seq) - 1)
            #set the location to the random chosen element
            input_seq[loc] = mut
        #return mutated sequence as string
        self.seqs.append(''.join(input_seq))
        return (''.join(input_seq))

    def deletion_mutation(self, seq):
        input_seq = seq

        n = random.randint(0, len(input_seq) - 1)
        seq8 = input_seq[:n] + input_seq[n+1:]
        self.seqs.append(seq8)
        return seq8

    def recombination(self, seq1, seq2):
        #find the halfway point, use min just in case len(1) != len(2)
        mid = int(min(len(seq1), len(seq2)) / 2)
        #first half of seq1 + second half of seq2
        seq3 = seq1[:mid] + seq2[mid:]
        #first half of seq2 + second half of seq1
        seq4 = seq2[:mid] + seq1[mid:]

        #return the pair of sequences
        self.seqs.append(seq3)
        self.seqs.append(seq4)
        return (seq3, seq4)


    def add_variable_copy(self, seq1):
        #max length of variable copy substring
        max_int = int(len(seq1) / 2)

        #try substrings of different length, start at 3
        for i in range(3, max_int + 1):
            #iterate through the sequence
            for j in range(len(seq1)):
                #check consecutive substrings
                one = seq1[j:j+i]
                two = seq1[j+i:j+(2*i)]
                #if the two are equal, create the new string
                if (one == two):
                    #new string with variable copy added
                    seq5 = seq1[:j+(2*i)] + one + seq1[j+(2*i):]
        self.seqs.append(seq5)
        return (seq5)


    def del_variable_copy(self, seq1):
        max_int = int(len(seq1) / 2)

        for i in range(3, max_int + 1):
            for j in range(len(seq1)):
                one = seq1[j:j+i]
                two = seq1[j+i:j+(2*i)]
                if (one == two):
                    #new string with one substring removed
                    seq6 = seq1[:j+i] + seq1[j+(2*i):]
        self.seqs.append(seq6)
        return (seq6)


    def transposon(self, seq1, tseq):
        #try various substrings starting with length 3
        for i in range(3, int(len(tseq)/2)):
            #check if start and end of string are equal
            if (tseq[:i] == tseq[-i:]):
                #if equal, save substring, and length
                subseq = tseq[:i]
                sublen = i
        #find the substring in the main seq
        index = seq1.find(subseq)
        #create new sequence with transposon inserted
        seq7 = seq1[:index] + tseq + seq1[index+sublen:]
        self.seqs.append(seq7)
        return (seq7)


seq1 = 'GCACGTATTGATTGGCCTGTACCTA'
Seq = SequenceVariation(seq1)
seqs = [Seq.seq1, Seq.seq2, Seq.seq3, Seq.seq4, Seq.seq5, Seq.seq6, Seq.seq7]
