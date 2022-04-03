from re import A, T

def get_hamming_distance(dna1, dna2):
    total = 0
    dna1_list = list(dna1)
    dna2_list = list(dna2)
    if dna1[0] != dna2[0]:
        total += 1
    if dna1[1] != dna2[1]:
        total += 1
    if dna1[2] != dna2[2]:
        total += 1
    if dna1[3] != dna2[3]:
        total += 1
    if dna1[4] != dna2[4]:
        total += 1
    if dna1[5] != dna2[5]:
        total += 1
    if dna1[6] != dna2[6]:
        total += 1
    if dna1[7] != dna2[7]:
        total += 1
    if dna1[8] != dna2[8]:
        total += 1
    if dna1[9] != dna2[9]:
        total += 1
    if dna1[10] != dna2[10]:
        total += 1
    if dna1[11] != dna2[11]:
        total += 1
    if dna1[12] != dna2[12]:
        total += 1
    if dna1[13] != dna2[13]:
        total += 1
    if dna1[14] != dna2[14]:
        total += 1
    if dna1[15] != dna2[15]:
        total += 1
    if dna1[16] != dna2[16]:
        total += 1
    return total

def string_reverse_dna(string):
    string_1 = ""
    index = len(string)
    while index > 0:
        string_1 += string[index - 1]
        index - index - 1
    return string_1

def list_to_string(string_2):
    string_2 = ""
    for ele in string_2:
        str1 += ele
    return string_2

def get_dna_complement(dna):
    reverse = string_reverse_dna(dna)
    dna_list = list(reverse)
    dna_list.reverse()
    if dna_list[0] == "A":
        dna_list[0] = "T"
    elif dna_list[0] == "T":
        dna_list[0] = "A"
    elif dna_list[0] == "G":
        dna_list[0] = "C"
    elif dna_list[0] == "C":
        dna_list[0] = "G"
    if dna_list[1] == "A":
        dna_list[1] = "T"
    elif dna_list[1] == "T":
        dna_list[1] = "A"
    elif dna_list[1] == "G":
        dna_list[1] = "C"
    elif dna_list[1] == "C":
        dna_list[1] = "G"
    if dna_list[2] == "A":
        dna_list[2] = "T"
    elif dna_list[2] == "T":
        dna_list[2] = "A"
    elif dna_list[2] == "G":
        dna_list[2] = "C"
    elif dna_list[2] == "C":
        dna_list[2] = "G"
    if dna_list[3] == "A":
        dna_list[3] = "T"
    elif dna_list[3] == "T":
        dna_list[3] = "A"
    elif dna_list[3] == "G":
        dna_list[3] = "C"
    elif dna_list[3] == "C":
        dna_list[3] = "G"
    if dna_list[4] == "A":
        dna_list[4] = "T"
    elif dna_list[4] == "T":
        dna_list[4] = "A"
    elif dna_list[4] == "G":
        dna_list[4] = "C"
    elif dna_list[4] == "C":
        dna_list[4] = "G"
    if dna_list[5] == "A":
        dna_list[5] = "T"
    elif dna_list[5] == "T":
        dna_list[5] = "A"
    elif dna_list[5] == "G":
        dna_list[5] = "C"
    elif dna_list[5] == "C":
        dna_list[5] = "G"
    if dna_list[6] == "A":
        dna_list[6] = "T"
    elif dna_list[6] == "T":
        dna_list[6] = "A"
    elif dna_list[6] == "G":
        dna_list[6] = "C"
    elif dna_list[6] == "C":
        dna_list[6] = "G"
    if dna_list[7] == "A":
        dna_list[7] = "T"
    elif dna_list[7] == "T":
        dna_list[7] = "A"
    elif dna_list[7] == "G":
        dna_list[7] = "C"
    elif dna_list[7] == "C":
        dna_list[7] = "G"
    if dna_list[8] == "A":
        dna_list[8] = "T"
    elif dna_list[8] == "T":
        dna_list[8] = "A"
    elif dna_list[8] == "G":
        dna_list[8] = "C"
    elif dna_list[8] == "C":
        dna_list[8] = "G"
    if dna_list[9] == "A":
        dna_list[9] = "T"
    elif dna_list[9] == "T":
        dna_list[9] = "A"
    elif dna_list[9] == "G":
        dna_list[9] = "C"
    if dna_list[9] == "C":
        dna_list[9] = "G"
    return dna

#test