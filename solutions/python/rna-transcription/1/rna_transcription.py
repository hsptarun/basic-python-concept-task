def to_rna(dna_strand):
    string = ""
    for letter in dna_strand:
        if letter == 'C':
            letter = 'G'
        elif letter == 'G':
            letter = 'C'
        elif letter == 'T':
            letter = 'A'
        elif letter == 'A':
            letter = 'U'
        string += letter

    return string
