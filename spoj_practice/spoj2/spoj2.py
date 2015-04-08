from sys import stdin
# http://www.spoj.com/problems/PRIME1/
# stdin line 1 is number of iterations, followed by that number of pairs of numbers in the form: m (space) n
# N > M , N-M < 100,000
# M > 1
# N < 1,000,000,000
# Find all primes between a given n, m

# returns a list of all the primes in between
def find_primes_between (n, m):
    primes = [2]
    # check all primes
    for i in xrange(2, n+1):
        # check if number is prime
        for prime in primes:
            # if is not prime, move onto next number i
            if i % prime == 0:
                break
        # if the number is in fact prime,
        else:
            primes.append(i)
    return primes

num_of_lines = int(stdin.readline())
for i in xrange(num_of_lines):
    m, n = map(int, stdin.readline().split(' '))
    prime = []
    primes = find_primes_between(n, m)
    for prime in primes:
        if prime >= m:
            print (prime)
    print