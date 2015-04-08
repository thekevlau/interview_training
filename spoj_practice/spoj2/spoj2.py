from sys import stdin
# http://www.spoj.com/problems/PRIME1/
# stdin line 1 is number of iterations, followed by that number of pairs of numbers in the form: m (space) n
# N > M , N-M < 100,000
# M > 1
# N < 1,000,000,000
# Find all primes between a given n, m

# returns a list of all the primes in between
def is_divisible (i, some_prime):
    return i % some_prime == 0

def find_primes_between (n, m):
    primes = [2]
    # check all primes
    for i in xrange(2, n+1):
        # in brackets, evaluates is_divisible calculation for a given i against all known primes (denoted by for prime in primes). think about it like the the for loop is being evaluated with the is_divisible function nested within. all of the results are compiled into a list of booleans. this list of boolean values (again, for a given i) is returned to the function 'any', which then checks for if any of those are true. if so, is_composite is set to true.
        is_composite = any(is_divisible(i, prime) for prime in primes)
        # then we say when is_composite is false for a given i, aka its a prime, then we append it to the list of primes
        if not is_composite:
            primes.append(i)
    return primes

num_of_lines = int(stdin.readline())
for i in xrange(num_of_lines):
    m, n = map(int, stdin.readline().split(' '))
    primes = find_primes_between(n, m)
    for prime in primes:
        if prime >= m:
            print (prime)
    print