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

#creates a reverse complement
def create_reverse_complement(seq):
    intab = "ATGC"
    outtab = "TACG"
    #maketrans to find the complement
    transtable = str.maketrans(intab, outtab)
    fasta = seq

    comp = fasta.translate(transtable)
    #return the reverse of the complement
    return comp[::-1]

def reading_frames(seq):
    #creates reading frames 1-6
    frames = []
    seq = seq
    rev = create_reverse_complement(seq)

    #first three reading frames using sequence
    for i in range(3):
        frames.append(seq[i:])
    #second three reading frames using reverse complement
    for i in range(3):
        frames.append(rev[i:])
    return frames

#helps find all possible substrings by creating frames,
#based on length of substring/kmer
def possible_substrings(seq, kmer):
    frames = []
    seq = seq

    #use the sequence slicing to create each possible frame
    for i in range(kmer):
        frames.append(seq[i:])
    return (frames)

#slice strings into substrings of size of kmer
def create_codons(frames, k):
    codons = []

    for frame in frames:
        #iterate through all the frames
        codon = []
        i = 0
        #slice the substring
        while (i < len(frame)):
            codon.append(frame[i:i+k])
            i += k
        #add list of sliced substring to nested list of substrings by frame
        codons.append(codon)
    return (codons)

#creates dictionaries for each independent frame
def create_frame_dictionaries(codons):
    #list of dictionaries to be returned
    dictionaries = []

    #iterate through nested list of codons
    for codon in codons:
        dictionary = {}
        for i in codon:
            #Assemble dictionary, key = substring, value = count
            if (len(i) % 3 != 0):
                continue
            #if substring in dictionary, increase count, else create key/value
            #pair
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        #append dictionary for the frame to list of dictionaries
        dictionaries.append(dictionary)
    return (dictionaries)

#creates one entire dictionary independent of frames
def create_dictionary(codons):
    dictionary = {}

    for codon in codons:
        #Assemble dictionary
        for i in codon:
            if (len(i) % 3 != 0):
                continue
            #if substring recognized, increase count, else add substring as
            #new key value pair
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

#returns a list of most frequent substrings
def most_freq(dictionary):
    #split dictionary into keys and values, each as a list
    d = dictionary
    v=list(d.values())
    k=list(d.keys())
    #set a max value, by taking the maximum of the list of values
    highest = max(v)
    keys = []

    #if max <= 1, no substring reoccurrs
    if (max(v) <= 1):
        return keys
    #iterate through the dictionary
    for k,v in d.items():
        #if value is one of the highest, append to list of keys
        if v == highest:
            keys.append(k)
    #returning assembled list of substrings
    return (keys, highest)

#returns nested list of
def frame_by_frame(seq, kmer):
    frames = reading_frames(seq)
    occurrences = []

    codons = create_codons(frames, kmer)
    dictionaries = create_frame_dictionaries(codons)
    for dictionary in dictionaries:
        occurrence = []
        occurrence.append(dictionaries.index(dictionary) + 1)
        if (most_freq(dictionary) == []):
            occurrence.append("No recurring substrings")
        else:
            occurrence.append(most_freq(dictionary))
        occurrences.append(occurrence)
    return (occurrences)

#prints substring that occurrs most based on size
def return_kmer(seq, kmer):
    #create dictionary
    frames = possible_substrings(seq, kmer)
    codons = create_codons(frames, kmer)
    dictionary = create_dictionary(codons)
    #call most_freq to print most ocurring
    print(most_freq(dictionary))

for i in range(1,4):
    return_kmer(seq, 3*i)
#print(frame_by_frame(seq, 3))
rows3 = frame_by_frame(seq, 3)
rows6 = frame_by_frame(seq, 6)
rows9 = frame_by_frame(seq, 9)
print (rows3)
print (rows6)
print (rows9)
