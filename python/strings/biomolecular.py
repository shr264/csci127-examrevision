
"""
We have the tools to compute how long the out sequence is as well as GC-content 
(the fraction of the sequence that is C and G) which is correlated with the stability of the molecule:

First, we compute the length of the sequence.
Next, we count the number of 'C' and number of 'G'.
Next, we add the number of 'C' and number of 'G' together, and divide by the length.
Then, we convert to a percentage by multiplying by 100 and print out the answer.
"""


insulin = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC"

# Compute the length, and store in variable to use again:
l = len(insulin)
print("The length is", l)

# Compute amount of C and G in the sequence:
numC = insulin.count('C')
numG = insulin.count('G')
print('Number of C nucleotides', numC)
print('Number of G nucleotides', numG)

# Compute the GC-content:
gc = (numC + numG) / l
# Convert to percentage by multiplying by 100:
gcPercent = gc * 100
print('GC-content is', gcPercent)
