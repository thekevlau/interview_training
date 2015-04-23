# given a list of unqiue, integers, return all possible subsets
# input: [1, 2, 3]
# output: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1,2,3] []]

# base case, input [], output []
# input [1], output [], [1]
# input [2], output [], [2], [1], [1, 2]
# every time you add the new number to previously existing elements

def subset_list (int_list):
	all_subsets = [[]]

	for integer in int_list:
		# subsets = []
		#for known_subsets in all_subsets:
			# route 1, make a temp version we can manipulate without affecting the original, append to it to make the new combination, then add it to the subset list for this iteration.
			#temp_known_subsets = list(known_subsets)
			#temp_known_subsets.append(integer)

			# route 2, make the integer into a list so we can then add it to known_subsets, which is defined as a new list. this again allows us to concatenate both lists without modifying the original known_subsets in all_subsets
			#list_of_input_int = [integer]
 
			#subsets.append(temp_known_subsets)
		# add that temp storage list to the output list
		#all_subsets += subsets

		# map returns a list
		# map maps a function to an iterable
		# the varaibles passed into lambda come from ONLY the iterable that is passed into the map function.
		# anything else you can just access directly without passing it into lambda, in fact you cannot pass them into lambda. 
		subsets = map(lambda known_subsets: known_subsets + [integer], all_subsets)
		all_subsets += subsets

	return all_subsets

int_list = [1, 2, 3]
print subset_list(int_list)