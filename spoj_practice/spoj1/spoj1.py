import sys

for line in sys.stdin:
    if int(line) != 42:
        print (line.strip())
    else:
       break