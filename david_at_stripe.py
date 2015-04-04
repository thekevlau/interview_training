
# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 3

# function that finds the nth fibonnacci number

n = 50

def fib (n):
    if (n==0):
        return 0

    if (n==1):
        return 1

    return fib(n-1) + fib(n-2)


result = fib(n)
print (result)
