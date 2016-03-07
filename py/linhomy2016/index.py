'''The Index class (for use in linear homology)

'''

from functools import lru_cache
from .tools import compose_2
from .tools import str_from_base36


@lru_cache(maxsize=None)
def size(rank, dim):
    '''Return number of indexes with given rank and dimension.

    >>> list(size(0, d) for d in range(12))
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    >>> list(size(1, d) for d in range(12))
    [0, 0, 0, 1, 2, 5, 8, 14, 20, 30, 40, 55]
    >>> list(size(2, d) for d in range(12))
    [0, 0, 0, 0, 0, 0, 1, 3, 9, 19, 39, 69]

    This gives the Fibonacci numbers.
    >>> [sum(size(i, j) for i in range(5)) for j in range(15)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    '''

    # Helps user, and checks against error in the recursion.
    if rank < 0 or dim < 0:
        raise ValueError(rank, dim)

    # Not enough room for the given rank.
    if rank * 3 > dim:
        return 0

    if rank == 0:
        # Root the recursion.
        return dim // 2 + 1

    else:
        # Convolve size(1, i) with size(rank - 1, dim - 3 - i).
        value = 0
        for i, j in compose_2(dim - 3):
            value += size(0, i) * size(rank - 1, j)

        return value


def _data_0(dim):
    '''
    >>> list(_data_0(0))
    [0, 0]
    >>> list(_data_0(1))
    [0, 1]
    >>> list(_data_0(2))
    [0, 2, 1, 0]
    >>> list(_data_0(3))
    [0, 3, 1, 1]
    >>> list(_data_0(4))
    [0, 4, 1, 2, 2, 0]
    '''

    for i in range(size(0, dim)):
        yield i
        yield dim - 2 * i


@lru_cache(maxsize=None)
def _data(rank, dim):
    '''Return data store for all indexes of given rank and dimension.

    >>> str_from_base36(_data(0, 0))
    '00'
    >>> str_from_base36(_data(0, 1))
    '01'
    >>> str_from_base36(_data(0, 10))
    '0a1826344250'

    '''
    length = size(rank, dim)
    value = bytearray(2 * rank * length)

    if rank == 0:
        return bytes(_data_0(dim))
    else:
        raise ValueError        # Not yet implemented.
