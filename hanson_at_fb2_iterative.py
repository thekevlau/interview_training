# given a list of unqiue, integers, return all possible subsets
# input: [1, 2, 3]
# output: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1,2,3] []]

# base case, input [], output []
# input [1], output [], [1]
# input [2], output [], [2], [1], [1, 2]
# every time you add the new number to previously existing elements

def subset_list (input_list):
	output_list = [[]]

	for in_element in sorted(input_list):
		total_list = []
		for list_within in output_list:
			# put the new element into a list of itself
			storage_list = [in_element]
			# make temp version which we can manipulate without affecting the original
			temp_list_within = list(list_within)
			# join the two to form the next combination of list items
			temp_list_within += storage_list
			# add it to a temp storage list of all combinations for this iteration
			total_list.append(temp_list_within)
		# add that temp storage list to the output list
		output_list += total_list

	return output_list

input_list = [1, 2, 3, 4]
print subset_list(input_list)