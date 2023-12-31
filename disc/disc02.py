#### Question 1
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    # >>> def is_even(x):
    # ... # Even numbers have remainder 0 when divided by 2.
    # ... return x % 2 == 0
    # >>> keep_ints(is_even, 5)
    # 2
    # 4
    #"""
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0


keep_ints(is_even, 5)


#### Question 2
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    # >>> def is_even(x):
    # ... # Even numbers have remainder 0 when divided by 2.
    # ... return x % 2 == 0
    # >>> make_keeper(5)(is_even)
    2
    4
    """

    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return f


make_keeper(5)(is_odd)

#### Question 3
def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    # >>> def square(x):
    # ... return x * x
    # >>> new_square = and_add(square, 3)
    # >>> new_square(4) # 4 * 4 + 3
    19
    """

    def g(x):
        return f(x) + n

    return g


def square(x):
    return x * x


new_square = and_add(square, 3)
print(new_square(4))
