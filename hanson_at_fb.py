# given a list of strings, determine which are anagrams and group them together.
# return a list of lists of anagrams

# input ['cat', 'act', 'dog', 'god', 'def']
# output [['cat', 'act'], ['dog', 'god'], ['def']]

# lists are assigned by reference, so list1 = list2, list 1 points to list 2
# to clone a list, you want to do list1 = list(list2)

# sorted(string) returns a list of chars of string in sorted order
# list.sort() modifies list in-place, returning None. note that the .sort() function is only used on lists
# ''.join(list), joins each element of the list together with '' (no space) in between
# when you append to a list, you also modify the list in-place. thus it returns None as well
# thus instead of 			\
	#temp_list = [word]
	#grouped_words[sorted_word] += temp_list
	# you can just do grouped_words[sorted_word].append(word)

#def find_anagrams (some_list):
#	grouped_words = {}
#	for word in some_list:
#		# sorted returns a list
#		sorted_word = ''.join(sorted(word))
#		print sorted_word
#		#if grouped_words[sorted_word]:
#		# instead of checking for existance of value at key sorted_word, just check for existance of key in the dict
#		if sorted_word in grouped_words:
#			print ("%s is already a key" % (sorted_word))
#			grouped_words[sorted_word].append(word)
#		else:
#			grouped_words[sorted_word] = [word]
#	return list(grouped_words.values())

from collections import defaultdict

def find_anagrams (some_list):
	grouped_words = defaultdict(list)
	for word in some_list:
		sorted_word = ''.join(sorted(word))
		grouped_words[sorted_word].append(word)
	return list(grouped_words.values())

input_list = ['cat', 'act', 'dog', 'god', 'def', 'lol', 'oll']
print find_anagrams(input_list)
