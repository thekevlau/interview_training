from sys import stdin

# http://www.spoj.com/problems/PRIME1/
# stdin line 1 is number of iterations, followed by that number of pairs of numbers in the form: m (space) n
# N > M , N-M < 100,000
# M > 1
# N < 1,000,000,000
# Find all primes between a given n, m


n = 100
m = 10

# returns a list of all the primes in between
def find_primes_between (n, m):
    # divide by all odd numbers, counter it up
    # divide by all primes before it
    # divide by all other primes between n, m
    # make sure we start with an odd number
    primes = [3]
    primes_between = []
    for i in xrange(1, n, 2):
        if i is 1 or i is 2 or i is 3:
            continue
        # check if number is prime
        for prime in primes:
            # if is not prime, move onto next number i
            if i%prime is 0:
                break
        # if the number is in fact prime,
        else:
            print ("prime number identified: %s" % (i))
            primes.append(i)
            if i > m:
                print ("prime between n, m identified: %s" % (i))
                primes_between.append(i)
    b = [1, 2]
    primes[:0] = b

    print ("DONE!")
    print ("All primes are as follows:")
    for prime in primes:
        print prime
    print ("DONE!")
    print ("All primes in between are as follows:")
    for prime in primes_between:
        print prime

find_primes_between(n, m)

