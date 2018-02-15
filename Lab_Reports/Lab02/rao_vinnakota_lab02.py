import re

#Create Global variables for input files
NUC_FILE = 'sequence.fasta'
PROTEIN_FILE = 'protein.fasta'
PDB_FILE = '5npa.pdb'

def read_fasta(filename):
    #empty stringgs/list to read into
    sequence = []
    seq = ''
    #open file
    my_file = open(filename)

    #iterate through file
    for line in my_file:
        #ignore non sequence lines
        if line.startswith('>'):
            continue
        else:
            #clean lines, and then add to string seq
            seq += line.rstrip()
    if seq:
        #if the string is not empty, add to list
        sequence.append(seq)
    #close file & return list
    my_file.close()
    return sequence

def user_input():
    #use read_fasta to create string sequence for nucleotides and protein
    nuc_seq = ''.join(read_fasta(NUC_FILE))
    protein_seq = ''.join(read_fasta(PROTEIN_FILE))
    #Ask for user input
    print("This is the protein Drosophila melanogaster sepia.")
    user_in = raw_input("Are you interested in the nucleotide, protein, or centroid data?\n")
    #call nucleotide, protein, or centroid based on user input
    if (user_in == 'nucleotide'):
        nucleotide(nuc_seq)
    if (user_in == 'protein'):
        protein(protein_seq)
    if (user_in == 'centroid'):
        calc_centroid(PDB_FILE)

def nucleotide(nuc_seq):
    #use len for str to find # of nucleotides
    nuc_len = len(nuc_seq)
    #find frequencies of various bases
    freqA = len(re.findall('[A|a]', nuc_seq))
    freqT = len(re.findall('[T|t]', nuc_seq))
    freqG = len(re.findall('[G|g]', nuc_seq))
    freqC = len(re.findall('[C|c]', nuc_seq))
    #freqOther = len(re.findall(['A|a|T|t|G|g|C|c'], nuc_seq))
    #Use process of elimination to count remaining "other" nucleotides
    freqOther = nuc_len - (freqA + freqT + freqG + freqC)
    #print output
    print "TotalLength:%s\nFreqA:%s\nFreqT:%s\nFreqC:%s\nFreqG:%s\nOther:%s"%(nuc_len, freqA, freqT, freqC, freqG, freqOther)
    return(nuc_len, freqA, freqT, freqG, freqC)

def protein(protein_seq):
    #matche index to return
    match_index = []
    #user in to find motif, use upper() to convert all input to uppercase
    user_in = raw_input("What is the motif you're looking for?\n").upper()
    #if invalid input (empty string or not a string), raise Exception
    if (user_in == "" or type(user_in) != str):
        raise Exception("Invalid Motif")
    #create regex using re.compile
    motif = re.compile(user_in)
    #find all matches
    allmatch = motif.finditer(protein_seq)
    #counter for # of matches
    i = 0
    #iterate through matches, counting + printing start of match
    for match in allmatch:
        i += 1
        match_index.append(match.start())
        print("match #%d:%d")%(i, match.start())
    #if counter remains at 0, no matches found,
    if (i == 0):
        print ("I'm sorry, there were no matches")
    else:
        print ("There were %d match(es)")%(i)
    #return all matches
    return (match_index)

def calc_centroid(pdbFile):
    #read in PDB file
    myFile = open(pdbFile)
    #create variables
    natoms = 0 #number of atoms
    xsum = ysum = zsum = 0

    for line in myFile:
        if line[:6] == 'ATOM  ':
            natoms += 1
            x = float(line[30:38]) #convert string to float
            y = float(line[38:46]) #stort up to but NOT INCLUDING en
            z = float(line[46:54])
            xsum += x
            ysum += y
            zsum += z
    myFile.close()
    if (natoms == 0):
        xav = yav = zav = 0
    else:
        #find average using coordinates/# of atoms
        xav = x/natoms
        yav = y/natoms
        zav = z/natoms
    print ("# of atoms:%s\nx-average:%s\ny-average:%s\nz-average:%s")%(natoms, xav, yav, zav)
    return (natoms, xav, yav, zav)

user_input()
