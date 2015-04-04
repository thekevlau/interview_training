from sys import stdin

# stdin line 1 is number of iterations, followed by that number of pairs of numbers in the form: m (space) n
# N > M
# M > 1000
# N < 10,000
# Find all primes between a given n, m

def find_primes_between (n, m):
    # divide by all odd numbers, counter it up
    # divide by all primes before it
    # divide by all other primes between n, m

num_of_lines = stdin.readline()

for xrange(num_of_lines):
    # numbers = stdin.readline().split(" ")
    # m = numbers[0]
    # n = numbers[1]
    # instead, do:
    m, n = stdin.readline().split('')
    primes = []
    primes = find_primes_between(n, m)
    print (prime in primes)