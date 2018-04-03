"""
Lab 05 - Sequence Alignment
Rao Vinnakota

"""
import random

DNA_2 = {'G': { 'G': 1, 'C':-3, 'A':-3, 'T':-3, 'N':0 },
         'C': { 'G':-3, 'C': 1, 'A':-3, 'T':-3, 'N':0 },
         'A': { 'G':-3, 'C':-3, 'A': 1, 'T':-3, 'N':0 },
         'T': { 'G':-3, 'C':-3, 'A':-3, 'T': 1, 'N':0 },
         'N': { 'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N':0 }}



class SequenceVariation:
    def __init__(self, input_seq):
        #check if the input string is empty, Exception if it is
        if (input_seq == ""):
            raise Exception("Can't create class with empty string")
        #create seq1 from input str
        self.seq1 = input_seq
        #call various class methods, starting with valid
        self.validate()
        self.seq2 = self.point_mutations(self.seq1, 10)
        self.seq3, self.seq4 = self.recombination(self.seq1, self.seq2)
        self.seq5 = self.add_variable_copy(self.seq1)
        self.seq6 = self.del_variable_copy(self.seq1)
        self.seq7 = self.transposon(self.seq1, 'ACGTGGTTGCACGT')


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
        return (''.join(input_seq))


    def recombination(self, seq1, seq2):
        #find the halfway point, use min just in case len(1) != len(2)
        mid = int(min(len(seq1), len(seq2)) / 2)
        #first half of seq1 + second half of seq2
        seq3 = seq1[:mid] + seq2[mid:]
        #first half of seq2 + second half of seq1
        seq4 = seq2[:mid] + seq1[mid:]

        #return the pair of sequences
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
        return (seq7)



class SequenceVariationDetection:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        #set mutation type
        self.mut_type = self.test_len()


    def get_seq(self):
        return (self.seq1, self.seq2)


    def test_len(self):
        seq1, seq2 = self.get_seq()

        #If the two are equal, send to point mutations
        if (len(seq1) == len(seq2)):
            mut_type = self.point_mutations()
        #If seq1 < seq2 --> add_mutations
        if (len(seq1) < len(seq2)):
            mut_type = self.add_mutations()
        #If seq1 > seq2 --> it's a variable copy with removal
        if (len(seq1) > len(seq2)):
            mut_type = "Variable Copy with Removal"
        return(mut_type)


    def point_mutations(self):
        seq1, seq2 = self.get_seq()
        mid = int(min(len(seq1)/2, len(seq2)/2))

        #check if the first halves match, or the second halves match
        if ((seq1[:mid] == seq2[:mid]) or (seq1[mid:] == seq2[mid:])):
            #if they do, they're recombination
            return ("Recombination")
        else:
            #otherwise it's a point mutation
            return ("Point Mutations")


    def add_mutations(self):
        seq1, seq2 = self.get_seq()
        len1, len2 = len(seq1), len(seq2)
        max_int = int(min(len1/2, len2/2))

        #try substrings of different lengths
        for i in range(3, max_int + 1):
            for j in range(len(seq1)):
                #if three consecutive subs match, it's variable copy number
                one = seq2[j:j+i]
                two = seq2[j+i:j+(2*i)]
                three = seq2[j+(2*i):j+(3*i)]
                if (one == two == three):
                    return ("Variable Copy with Addition")
        #Otherwise, it's a tranposon insertion
        return ("Transposon Insertion")







seq1 = 'GCACGTATTGATTGGCCTGTACCTA'
Seq = SequenceVariation(seq1)
SeqDet = SequenceVariationDetection(Seq.seq1, Seq.seq7)
print (SeqDet.mut_type)
