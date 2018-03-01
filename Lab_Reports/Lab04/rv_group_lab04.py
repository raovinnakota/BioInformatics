"""
Counting K-Mers
Rao Vinnakota
Liz Miller
Phillippine Alba
Blake Burnley
Jelani Bell-Isaacs
Lillya Galechyan
"""
seq='atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'

def create_reverse_complement(seq):
    intab = "ATGC"
    outtab = "TACG"
    transtable = str.maketrans(intab, outtab)
    fasta = seq

    comp = fasta.translate(transtable)
    return comp[::-1]

def reading_frames(seq):
    frames = []
    seq = seq
    rev = create_reverse_complement(seq)

    for i in range(3):
        frames.append(seq[i:])
    for i in range(3):
        frames.append(rev[i:])
    return frames

def possible_substrings(seq, kmer):
    frames = []
    seq = seq

    for i in range(kmer):
        frames.append(seq[i:])
    return (frames)

def create_codons(frames, k):
    codons = []

    for frame in frames:
        codon = []
        i = 0
        while (i < len(frame)):
            codon.append(frame[i:i+k])
            i += k
        codons.append(codon)
    return (codons)

def create_frame_dictionaries(codons):
    dictionaries = []

    for codon in codons:
        dictionary = {}
        for i in codon:
            if (len(i) % 3 != 0):
                continue
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        print (dictionary)
        dictionaries.append(dictionary)
    return (dictionaries)

def create_dictionary(codons):
    dictionary = {}

    for codon in codons:
        for i in codon:
            if (len(i) % 3 != 0):
                continue
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

def most_freq(dictionary):
    d = dictionary
    v=list(d.values())
    k=list(d.keys())
    highest = max(v)
    keys = []

    for k,v in d.items():
        if v == highest:
            keys.append(k)
    return keys

def frame_by_frame(seq):
    frames = reading_frames(seq)
    occurrences = []

    for i in range (3, 10, 3):
        codons = create_codons(frames, i)
        #dictionary

#frames = possible_substrings(seq, 9)
frames = reading_frames(seq)
codons = create_codons(frames, 3)
#dictionary = create_dictionary(codons)
#print (most_freq(dictionary))
