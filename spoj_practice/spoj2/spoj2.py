from sys import stdin
from sys import stdout

# http://www.spoj.com/problems/PRIME1/
# stdin line 1 is number of iterations, followed by that number of pairs of numbers in the form: m (space) n
# N > M , N-M < 100,000
# M > 1
# N < 1,000,000,000
# Find all primes between a given n, m

# handle stdin/stdout and unit testing

# returns a list of all the primes in between
def find_primes_between (n, m):
    # divide by all odd numbers, counter it up
    # divide by all primes before it
    # divide by all other primes between n, m
    # make sure we start with an odd number

    # primes to check against
    # 1 is not a prime number, the loop excludes even numbers thus 2 does not need to be added
    primes = [2, 3]
    # check all primes
    for i in xrange(2, n+1):
        # check if number is prime
        for prime in primes:
            # if is not prime, move onto next number i
            if i%prime == 0:
                break
        # if the number is in fact prime,
        else:
            primes.append(i)
    return primes

num_of_lines = int(stdin.readline())
for i in xrange(num_of_lines):
    # numbers = stdin.readline().split(" ")
    # m = numbers[0]
    # n = numbers[1]
    # instead, do:
    m, n = map(int, stdin.readline().split(' '))
    prime = []
    primes = find_primes_between(n, m)
    for prime in primes:
        if prime >= m:
            #stdout.write(str(prime))
            #print
            print (prime)
    else:
        print
    # takes out extra stdoutpace between each iteration
