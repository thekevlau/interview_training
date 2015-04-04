# f(0) = 0
# f(1) = 1
# f(2) = 1 + 0 = 1
# f(3) = 1 + 1 = 2
# f(4) = 2 + 1 = 3
# f(5) = 3 + 2 = 5




# function that finds the nth fibonnacci number

def fib (n):
    if n==0:
        return 0

    elif (n==1):
        return 1

    previous = 1
    preprevious = 0
    k = 1
    while (k != n):
        current = previous + preprevious
        preprevious = previous
        previous = current
        k=k+1
    return current

print (fib(50))