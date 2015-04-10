# given a list of strings, determine which are anagrams and group them together.
# return a list of lists of anagrams

# input ['cat', 'act', 'dog', 'god', 'def']
# output [['cat', 'act'], ['dog', 'god'], ['def']]

# lists are assigned by reference, so list1 = list2, list 1 points to list 2
# to clone a list, you want to do list1 = list(list2)

# sorted(string) = list of chars of string
# sort(list) = modifies list in-place
# ''.join(list), joins each element of the list together with '' (no space) in between


def find_anagrams (some_list):
	grouped_words = {}
	for word in some_list:
		sorted_word = ''.join(sorted(word))
		print sorted_word
		#if grouped_words[sorted_word]:
		if sorted_word in grouped_words:
			print ("%s is already a key" % (sorted_word))
			temp_list = [word]
			grouped_words[sorted_word] += temp_list
			# grouped_words[sorted_word] = grouped_words[sorted_word].append(word)
			# ^ append modifies the original list, and this somehow messes with things.....i do not understand
		else:
			grouped_words[sorted_word] = [word]
	return list(grouped_words.values())


input_list = ['cat', 'act', 'dog', 'god', 'def', 'lol', 'oll']
print find_anagrams(input_list)