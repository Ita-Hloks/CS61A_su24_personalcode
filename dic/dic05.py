# 突然心血来潮想要备份一下，懒得整理前面了，从 05 开始

# Q2: Repeated
def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    i = 0
    "*** YOUR CODE HERE ***"
    the_list = [next(t) for x in range(k)]
    while True:
        if len(set(the_list)) == 1:
            return the_list[0]
        else:
            del the_list[0]
            the_list.append(next(t))


# Generators
def gen_fib():
    """
    finish this -> ____(______(lambda n: n > 2024, ________)) <-
    >>> print(next(filter(lambda n: n > 2024, gen_fib())))
    2584
    """
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n


# Q3: Something Different
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    last_x = next(t)
    for x in t:
        yield x - last_x
        last_x = x
    # Bad code
    # i = 0
    # the_list = list(t) # 防止迭代器耗尽
    # result = []
    # while i < len(the_list) - 1:
    #     result += [the_list[i + 1] - the_list[i]]
    #     i += 1
    # return iter(result)


# Q4: Primes Generator

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def helper(i):
        if i > (n ** 0.5):  # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)

    return helper(2)


def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    "*** YOUR CODE HERE ***"
    for n in range(n, 1, -1):
        if is_prime(n):
            yield n


# Now that you've done it using a for loop and yield, try using yield from!

def primes_gen2(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen2(n - 1)


# Q5: Partitions
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        for p in partition_gen(n - m, m):
            yield p + ' + ' + str(m)
    if m > 1:
        yield from partition_gen(n, m - 1)
