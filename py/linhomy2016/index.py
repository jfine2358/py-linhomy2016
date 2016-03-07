'''The Index class (for use in linear homology)

'''

from functools import lru_cache

@lru_cache(maxsize=None)
def size(rank, dim):
    '''
    >>> list(size(0, d) for d in range(8))
    [1, 1, 2, 2, 3, 3, 4, 4]
    '''

    if rank * 3 > dim:
        return 0

    if rank == 0:
        return dim // 2 + 1
    else:

        value = 0
        for i in range(dim + 1):
            j = dim - i - 3
            value += size(0, i) * size(rank - 1, j)

        return value
