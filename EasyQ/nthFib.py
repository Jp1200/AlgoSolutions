def getNthFib(n):
    F0 = 0
      F1 = 1
       if n == 1:
            return F0
        elif n == 2:
            return F1
        else:
            return getNthFib(n-2) + getNthFib(n-1)
    pass
# very simple algorithm
#  you have a basis which is F0 and F1 remeber that
# fib(1) = 0 & fib(2) = 1 and the algorith works recurisivly:
# so if fib(1) return 0 and if fib(2) return 1 else:
# the nth fib nnumber is equal to fib(n-2) + fib(n-1)
