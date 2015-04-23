# function returning all permutations of chars of a given string in alphabetical order

from sys import stdin

def find_all_permutations(input_string):   
    all_permutations = set()
    input_string = "".join(sorted(input_string))
    for i, each_char in enumerate(input_string):  
        if len(input_string) > 1:    
            new_string = input_string[:i] + input_string[i+1:]
            for permutation in find_all_permutations(new_string): 
                new_permutation = each_char+permutation
                all_permutations.add(new_permutation)
        else:
            all_permutations.add(input_string)
            return all_permutations
    return all_permutations

for i in xrange(int(stdlin.readline())):
    input_string = str(stdin.readline())
    result = find_all_permutations(input_string)
    print(result)