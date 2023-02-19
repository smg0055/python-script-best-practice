#! /usr/bin/env python3

"A module for getting the smallest prime factor of an integer."

import sys

def get_smallest_prime_factor(n):
    """
    Returns the smallest integer that is a factor of `n`.

    If `n` is a prime number, `None` will be returned.

    Parameters
    ----------
    n : int
        The integer to be factored.

    Returns
    -------
    int or None
        The smallest integer that is a factor of `n`  
        or
        None if `n` is a prime number.
    
    Examples
    --------
    >>> get_smallest_prime_factor(7)
    >>> get_smallest_prime_factor(8)
    2
    >>> get_smallest_prime_factor(9)
    3
    """
    for i in range(2, n):
        if (n % i) == 0:
            return i
    return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    smallest_prime_factor = None

    for i in range(2, n):
    if (n % i) == 0:
        smallest_prime_factor = i
        break

    if smallest_prime_factor is None:
        print(n)
    else:
        print(smallest_prime_factor)
        
### Having some issues using git commit and push; I recieve an error code regarding password authentication even though this worked for me only a week ago.
