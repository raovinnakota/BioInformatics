import re

NUC_FILE = 'sequence.fasta'
PROTEIN_FILE = 'protein.fasta'
PDB_FILE = '5npa.pdb'

def read_fasta(filename):
    sequence = []
    seq = ''
    my_file = open(filename)

    for line in my_file:
        if line.startswith('>'):
            continue
        else:
            seq += line.rstrip()
    if seq:
        sequence.append(seq)
    my_file.close()
    return sequence

def user_input():
    nuc_seq = ''.join(read_fasta(NUC_FILE))
    protein_seq = ''.join(read_fasta(PROTEIN_FILE))
    print("This is the protein Drosophila melanogaster sepia.")
    user_in = raw_input("Are you interested in the nucleotide, protein, or centroid data?\n")
    if (user_in == 'nucleotide'):
        nucleotide(nuc_seq)
    if (user_in == 'protein'):
        protein_seq = ''.join(read_fasta(PROTEIN_FILE))
        protein(protein_seq)
    if (user_in == 'centroid'):
        calc_centroid(PDB_FILE)

def nucleotide(nuc_seq):
    nuc_len = len(nuc_seq)
    freqA = len(re.findall('[A|a]', nuc_seq))
    freqT = len(re.findall('[T|t]', nuc_seq))
    freqG = len(re.findall('[G|g]', nuc_seq))
    freqC = len(re.findall('[C|c]', nuc_seq))
    #freqOther = len(re.findall(['A|a|T|t|G|g|C|c'], nuc_seq))
    freqOther = nuc_len - (freqA + freqT + freqG + freqC)
    print "TotalLength:%s\nFreqA:%s\nFreqT:%s\nFreqC:%s\nFreqG:%s\nOther:%s"%(nuc_len, freqA, freqT, freqC, freqG, freqOther)

    return(nuc_len, freqA)

def protein(protein_seq):
    user_in = raw_input("What is the motif you're looking for?\n").upper()
    if (user_in == "" or type(user_in) != str):
        raise Exception("Invalid Motif")
    motif = re.compile(user_in)
    allmatch = motif.finditer(protein_seq)
    i = 0
    for match in allmatch:
        i += 1
        print(match.start())
    if (i == 0):
        print ("I'm sorry, there were no matches")

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
            y = float(line[38:46]) #stort up to but NOT INCLUDING end
            z = float(line[46:54])
            xsum += x
            ysum += y
            zsum += z
    myFile.close()
    if (natoms == 0):
        xav = yav = zav = 0
    else:
        xav = x/natoms
        yav = y/natoms
        zav = z/natoms
    print (natoms, xav, yav, zav)
    return (natoms, xav, yav, zav)

user_input()
