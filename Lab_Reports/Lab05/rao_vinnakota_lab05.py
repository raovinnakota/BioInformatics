"""
Lab 05 - Sequence Alignment
Rao Vinnakota

"""
import random


class SequenceVariation:
    def __init__(self, input_seq):
        if (input_seq == ""):
            raise Exception("Can't create class with empty string")
        self.seq1 = input_seq
        self.seq2 = self.point_mutations(self.seq1, 10)
        self.seq3, self.seq4 = self.recombination(self.seq1, self.seq2)
        self.seq5 = None
        self.validate()

    def get_input_seq(self):
        return (self.seq1)

    def validate(self):
        input_seq = self.get_input_seq()
        valid = ['A', 'G', 'T', 'C', 'N']

        for i in input_seq:
            if i not in valid:
                raise Exception("Not a valid input sequence")
        return (1)

    def point_mutations(self, seq, n):
        input_seq = list(seq)

        if (n > len(input_seq)):
            raise Exception("Impossible to have more mutations than nucleotides")
        for i in range(n):
            mut = random.choice('ACTG')
            loc = random.randint(0, len(input_seq))
            input_seq[loc] = mut
        return (''.join(input_seq))

    def recombination(self, seq1, seq2):
        mid = int(min(len(seq1), len(seq2)) / 2)
        seq3 = seq1[:mid] + seq2[mid:]
        seq4 = seq2[:mid] + seq1[mid:]

        return (seq3, seq4)



seq1 = 'GCACGTATTGATTGGCCTGTACCTA'
Seq = SequenceVariation(seq1)
print (Seq.seq1, Seq.seq2)
print (Seq.seq3, Seq.seq4)
