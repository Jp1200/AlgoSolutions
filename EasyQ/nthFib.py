def getNthFib(n):
    F0 = 0
    F1 = 1
    if n == 1:
        return F0
    elif n == 2:
        return F1
    else:
        return getNthFib(n-2) + getNthFib(n-1)

# very simple algorithm
#  you have a basis which is F0 and F1 remeber that
# fib(1) = 0 & fib(2) = 1 and the algorith works recurisivly:
# so if fib(1) return 0 and if fib(2) return 1 else:
# the nth fib nnumber is equal to fib(n-2) + fib(n-1)
# O(n^2) time and O(n) space

# Fastest way to compute it: O(n) time and O(1) space


def getNthFib2(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


print(getNthFib2(12))
