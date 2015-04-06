from sys import stdin

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
    primes = [3]
    primes_between = []
    
    # unique cases
    if m < 2:
        primes_between.append(2)
    if m <= 3:
        primes_between.append(3)
    
    # check all primes
    for i in xrange(3, n+1, 2):
        # check if number is prime
        for prime in primes:
            # if is not prime, move onto next number i
            if i%prime is 0:
                break
        # if the number is in fact prime,
        else:
            primes.append(i)
            if i >= m:
                primes_between.append(i)
    
    return primes_between 

num_of_lines = int(stdin.readline())
for i in xrange(num_of_lines):
    # numbers = stdin.readline().split(" ")
    # m = numbers[0]
    # n = numbers[1]
    # instead, do:
    m, n = stdin.readline().split(' ')
    m = int(m)
    n = int(n)
    prime = []
    primes = find_primes_between(n, m)
    for prime in primes:
        print (prime)
    # takes out extra space between each iteration
    print ('\n'.strip())