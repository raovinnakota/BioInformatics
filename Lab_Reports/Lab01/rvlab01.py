#Rao Vinnakota
#Programming for Biology Lab 1

def retranscriptase(rna):
    incoming = ["A", "G", "U", "C"]
    retrans = ["G", "A", "C", "T"]

    rna = rna.upper()
    rna = list(rna)
    for i in range(len(rna)):
        if rna[i] not in incoming:
            raise Exception("Not a Valid Input")
        else:
            rna[i] = retrans[incoming.index(rna[i])]
    rna = ''.join(rna)
    return rna

print(retranscriptase("AGUCgacu"))
