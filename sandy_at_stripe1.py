# IPV4 IP ADDRESS
# 0-255
# write a function that given an IP string, return an array of integers. of four numbers.
# ie. 123.123.123.123, return list = [123, 123, 123, 123]
# 123.134.4.75

ip_string = "123.23.42.33"

def listify_ip_address(ip_string):
    # make simplier sounding local functions
    list_of_ip_numbers = []
    sub_string = ""
    for char in ip_string:
        if char != ".":
            sub_string = sub_string + char
        else:
            list_of_ip_numbers.append(int(sub_string))
            sub_string = ""
    list_of_ip_numbers.append(int(sub_string))
    return list_of_ip_numbers

# if you see something that's bad, acknowledge it and deal with it later
# notice patterns like loop through and do function(x), then do function(x) again after the loop is done. usually in this case there's a better way of doing it.

# think about what you actually care about before making your next action decision. sometimes step back and consider if your actions are really necessary? are you really getting at the heart of the problem? don't make it too convoluted. don't force a generalization. instead of if a, b, c, AND d, then you're good. maybe there's another case z where it's much simpler/obvious what the condition should be

# tracing through function with actual values/numbers/input before you run. good testing practice.

# identify problem.

print listify_ip_address(ip_string)


with ff as open('/tmp/filename.txt', 'r'):
    ff.readlines()

def listify_ip_address(ip_string):
    some_array = map(int, ip_string.split("."))

    # .split returns a list with each of the split portions as an entry

