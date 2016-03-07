'''Useful tools
'''

import string

def chunk(size, seq):
    '''Iterate over sequence, broken into size chunks.

    >>> list(chunk(5, ''))
    []

    >>> list(chunk(5, string.ascii_lowercase))
    ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']
    '''

    length = len(seq)
    count = (length + size - 1) // size

    prev = 0
    for i in range(1, count + 1):
        curr = i * size
        yield seq[prev:curr]
        prev = curr


class GetChunkView:
    '''Provide item access interface to chunks in a sequence.

    Just enough to allow bisect searching of chunks.

    >>> pairs = GetChunkView(2, '0123456789')
    >>> pairs[0], pairs[1], pairs[2], pairs[3]
    ('01', '23', '45', '67')

    >>> from bisect import bisect_left
    >>> bisect_left(pairs, '23')
    1
    '''

    def __init__(self, size, seq):

        self.size = size
        self.seq = seq

    def __len__(self):

        seq, size = self.seq, self.size
        length = len(seq)
        return (length + size - 1) // size

    def __getitem__(self, index):

        seq, size = self.seq, self.size
        return seq[index * size : (index + 1) * size]


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


base36_digits = string.digits + string.ascii_lowercase

def str_from_bytes36(b):
    '''Return string representation of base 36 bytes.

    >>> str_from_bytes36(bytes(range(36)))
    '0123456789abcdefghijklmnopqrstuvwxyz'

    >>> str_from_bytes36(bytes([36]))
    Traceback (most recent call last):
    IndexError: string index out of range
    '''
    return ''.join(base36_digits[i] for i in b)


def bytes36_from_str(s):
    '''Return bytes, the characters of s as base 36 numbers.

    >>> base36_digits
    '0123456789abcdefghijklmnopqrstuvwxyz'
    >>> list(bytes36_from_str(base36_digits)) == list(range(36))
    True
    >>> list(bytes36_from_str(base36_digits.upper())) == list(range(36))
    True
    '''
    return bytes(int(c, 36) for c in s)
