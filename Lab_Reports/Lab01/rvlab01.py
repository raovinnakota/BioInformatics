"""
Programming for Biology Lab 01

@author: Rao Vinnakota
"""

#transcribes the incoming rna to dna
def rna_to_dna(incoming, rna_in, dna_in):
    #loops through the incoming sequence
    for i in range(len(incoming)):
        #if the incoming nucleotide is unknown, it passes over it
        if (incoming[i] == "N"):
            continue
        #it changes the item to it's DNA complement
        incoming[i] = dna_in[rna_in.index(incoming[i])]
    #returns edited list
    return incoming

#Transcribes the incoming dna to rna
def dna_to_rna(incoming, rna_in, dna_in):
    #loops through incoming sequence
    for i in range(len(incoming)):
        #if incoming nucleotide is unknown, it passes over it
        if (incoming[i] == "N"):
            continue
            #changes the list item to RNA complement
        incoming[i] = rna_in[dna_in.index(incoming[i])]
    #returns edited list
    return(incoming)

def reverseTransDNA(incoming):
    #sets input type to rna by default
    input_type = "rna"
    #lists containing the 4 bases for rna & dna. The lists are created such
    #that rna_in[0] forms a base pair with dna_in[0]
    rna_in = ["A", "G", "U", "C"]
    dna_in = ["T", "C", "A", "G"]

    #convert the input to upper case
    incoming = incoming.upper()
    #convert input from string to list
    input_str = incoming
    incoming = list(incoming)
    #iterate through created input list
    for i in range(len(incoming)):
        #if input has T & U, it is an invalid string, raise exception
        if ("T" in incoming and "U" in incoming):
            raise Exception("This is not a valid DNA or RNA strand")
        #if unrecognized nucleotide
        if incoming[i] not in rna_in:
            #set type to dna if unrecognized nucleotide is just T in DNA
            if (incoming[i] in dna_in):
                input_type = "dna"
            #otherwise set the the unrecognized nucleotide with "N"
            else:
                incoming[i] = "N"
    #call the right helper function based on the type value
    if (input_type == "dna"):
        dna_to_rna(incoming, rna_in, dna_in)
    else:
        rna_to_dna(incoming, rna_in, dna_in)
    #Reverse the output list, and then joined into a string
    output_str = ''.join(incoming[::-1])
    #print the two strings
    print (input_str, output_str)
    #return the two strings
    return (input_str, output_str)

reverseTransDNA("CUUUCGCAAUGAUAbluacg")
