def dna2rna(dna):
    ii = list(dna)

    for i in range(len(ii)):
        if ii[i] == 'T':
            ii[i] = 'U'

    return "".join(ii)


if __name__ == "__main__":
    inp = input('Enter dna sequence :')
    print("The rna for given is :", dna2rna(inp))