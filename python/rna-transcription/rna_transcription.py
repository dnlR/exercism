transcriptions = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    rna_strand = ""
    for strand in dna_strand:
        if strand in transcriptions:
            rna_strand += transcriptions[strand]
        else:
            raise ValueError("Invalid dna strand")
    return rna_strand
