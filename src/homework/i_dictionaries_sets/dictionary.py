def get_p_distance(dna1, dna2):
    list_dna1 = list(dna1)
    list_dna2 = list(dna2)
    counter = 0
    for i in range(len(list_dna1)):
        if list_dna1[i] != list_dna1[i]:
            counter += .1
    return counter

def get_p_distance_matrix(ddna1, ddna2, ddna3, ddna4):
    list_dna1 = list(ddna1)
    list_dna2 = list(ddna2)
    list_dna3 = list(ddna3)
    list_dna4 = list(ddna4)
    new_dna1 = list(round(float(get_p_distance(list_dna1, list_dna2))), 1), round(float(get_p_distance(list_dna1, list_dna2)), 1)
    round(float(get_p_distance(list_dna1, list_dna3), 1), round(float(get_p_distance(list_dna1, list_dna4), 1)))
    new_dna2 = list((get_p_distance(list_dna2, list_dna1))), (float(get_p_distance(list_dna2, list_dna2))),
    get_p_distance(list_dna2, list_dna3), round(get_p_distance(list_dna2, list_dna4), 1)
    new_dna3 = list((get_p_distance(list_dna3, list_dna1)), get_p_distance(list_dna3, list_dna4))
    new_dna4 = list((get_p_distance(list_dna4, list_dna1), round(get_p_distance(list_dna4, list_dna2)), 2),
    get_p_distance(list_dna4, list_dna3), (float(get_p_distance(list_dna4, list_dna4))))
    return new_dna1, new_dna2, new_dna3, new_dna4