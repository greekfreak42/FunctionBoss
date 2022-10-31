#! /usr/bin/python3

import numpy as np

from function_types.gr_function import PolynomialFunction

def main() -> None:
    f = PolynomialFunction(np.array([-1, 3]), np.array([3, 2]))
    g = f.get_differentiated()

    print(f)
    print(g)


if __name__ == '__main__': main()