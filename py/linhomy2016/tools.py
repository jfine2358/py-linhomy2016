'''Useful tools
'''

def compose_2(n):
    '''Yield pairs (0, n), (1, n - 1), ... (n, 0).

    A special case of composing a number into parts.  The values are
    yielded in lexicographic order.

    >>> list(compose_2(0))
    [(0, 0)]
    >>> list(compose_2(1))
    [(0, 1), (1, 0)]
    >>> list(compose_2(2))
    [(0, 2), (1, 1), (2, 0)]
    >>> list(compose_2(3))
    [(0, 3), (1, 2), (2, 1), (3, 0)]
    '''

    for i in range(n + 1):
        yield i, n - i
