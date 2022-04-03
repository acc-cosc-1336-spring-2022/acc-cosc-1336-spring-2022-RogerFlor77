from strings import get_dna_complement
from strings import get_hamming_distance

decision = int(input("""1 = Hamming Distance 
2 = DNA Compliment 
3 = Exit
Please enter your number: """))

if decision == 1:
    dna1 = str(input('Enter a DNA strand 1: '))
    dna2 = str(input('Enter a DNA strand 2: '))
    get_hamming_distance(dna1, dna2)
    print (get_hamming_distance(dna1, dna2))
elif decision == 2:
    dna = str(input('Enter a DNA strand 1: '))
    get_dna_complement(dna)
    print (get_dna_complement(dna))
elif decision == 3:
    print ("This program has ended")

    int(input("Would you like to do another? Y for yes, N for no:"))



#test