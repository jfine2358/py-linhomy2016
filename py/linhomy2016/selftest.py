'''Run self-test on all modules

Run this as a module and it will perform the self-test.
'''

import doctest
from importlib import import_module


MODULES = [
    '.index',
]

if __name__ == '__main__':

    for name in MODULES:

        mod = import_module(name, package=__package__)
        prefix = mod.__name__.ljust(20)

        print(prefix, doctest.testmod(mod))
