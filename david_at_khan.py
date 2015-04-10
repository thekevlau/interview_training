# given a regular expression, ie. "hello.*py.?"
# in regex, a period matches any other char. star before it means the char after it can be repeated 0-n times.
# question mark means 'zero or one times'

# you're also given a string, "hello.py" and another one "yellow.py" and "hellokevin.pyc"

# given the reg ex and a string, determine if they match.




def matches (reg_ex, some_string):

	for i, reg_char in enumerate(reg_ex):
		if reg_ex[i] == ".":
			continue
		if reg_ex[i] != some_string[i]:
			return False

		if "?" not in reg_ex and "*" not in reg_ex:
			if len(reg_ex) != len(some_string):
				return False

		if not i > len(reg_ex)-2:
			if reg_ex[i+1] == "?":
				print ("found question mark")
				new_reg_list = reg_ex[i+2:]
				other_reg_list = list(reg_ex[i]) + reg_ex[i+2:]
				new_string= some_string[i:]
				print("executing recurrsion")
				print ("case 1 string is %s" % (new_reg_list))
				print ("case 2 string is %s" % (other_reg_list))
				if matches(new_reg_list, new_string): 
					print ("executed case 1")
					return True
				elif matches(other_reg_list, new_string):
					print ("executed case 2")
					return True
				else:
					return False 
	return True

reg_ex = "hello.kp?ya"
some_string = "hello.kpy"

print (matches (reg_ex, some_string))