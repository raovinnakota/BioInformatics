#Rao Vinnakota
#Programming for Biology Lab 1

def rna_to_dna(incoming, rna_in, dna_in):
    for i in range(len(incoming)):
        if (incoming[i] == "N"):
            continue
        incoming[i] = dna_in[rna_in.index(incoming[i])]
    return incoming

def dna_to_rna(incoming, rna_in, dna_in):
    for i in range(len(incoming)):
        if (incoming[i] == "N"):
            continue
        incoming[i] = rna_in[dna_in.index(incoming[i])]
    return(incoming)

def retranscriptase(incoming):
    input_type = "rna"
    rna_in = ["A", "G", "U", "C"]
    dna_in = ["G", "A", "C", "T"]

    incoming = incoming.upper()
    incoming = list(incoming)
    for i in range(len(incoming)):
        if ("T" in incoming and "U" in incoming):
            raise Exception("This is not a valid DNA or RNA strand")
        if incoming[i] not in rna_in:
            if (incoming[i] in dna_in):
                input_type = "dna"
            else:
                incoming[i] = "N"
    input_str = ''.join(incoming)
    if (input_type == "dna"):
        dna_to_rna(incoming, rna_in, dna_in)
    else:
        rna_to_dna(incoming, rna_in, dna_in)
    output_str = ''.join(incoming)
    print (input_str, output_str)
    return (input_str, output_str)

retranscriptase("AGTTgaTcb")
