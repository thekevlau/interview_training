# function returning all permutations of chars of a given string in alphabetical order

def find_all_permutations (input_string):   
    all_permutations = []
    input_string = "".join(sorted(input_string))
    for i, each_char in enumerate(input_string):  
        if len(input_string) > 1:    
            new_string = input_string[:i] + input_string[i+1:]
            for permutation in find_all_permutations(new_string): 
                new_permutation = each_char+permutation
                all_permutations.append(new_permutation)
        else:
            all_permutations.append(input_string)
            return all_permutations
    return all_permutations

input_string = "sdfa"
result = find_all_permutations(input_string)
print (result)